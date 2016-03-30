from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from islideas.ideas.forms import IdeaForm, CommentForm, VoteForm, TagForm
from islideas.ideas.models import Idea, Tag, Comment
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.utils.text import slugify
from django.core.urlresolvers import reverse_lazy


class IdeaList(ListView):
    model = Idea
    queryset = Idea.objects.order_by('-date')
    template_name = 'ideas/idea_list.html'

    def get_queryset(self):
        queryset = super(IdeaList, self).get_queryset()

        q = self.request.GET.get('q')
        if q:
            return queryset.filter(Q(title__icontains=q) |
                                   Q(description__icontains=q) |
                                   Q(tags__name=q))
        return queryset


class ActionMixin(object):

    @require_http_methods(["POST"])
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(ActionMixin, self).form_valid(form)


class IdeaCreate(CreateView):
    model = Idea
    form_class = IdeaForm

    def get_context_data(self, **kwargs):
        context = super(IdeaCreate, self).get_context_data(**kwargs)
        context['tag_form'] = TagForm()
        context['idea_form'] = IdeaForm()
        return context

    def post(self, request, *args, **kwargs):
        tag_form = TagForm(request.POST)
        idea_form = IdeaForm(request.POST)
        # If tag is valid, save tag
        if tag_form.is_valid():
            new_tag = tag_form.save()
            messages.success(request, '"{0}" was added as a new tag!'.format(new_tag.name))
            # If idea was valid, add new tag to idea
            if idea_form.is_valid():
                new_idea = idea_form.save()
                new_idea.tags.add(new_tag.id)
                messages.success(request, '"{0}" was added!'.format(new_idea.title))
                return redirect('home')
            # If idea was invalid, reload form
            else:
                messages.error(request, 'Sorry, your idea could not be added.')
                return redirect('idea_form')
        # If tag was invalid, try to process idea
        else:
            # If just the idea was valid, save idea
            if idea_form.is_valid():
                idea_form.save()
                messages.success(request, '"{0}" was added!'.format(new_idea.title))
                return redirect('home')
            # If idea was invalid too, reload form
            else:
                messages.error(request, 'Sorry, your idea could not be added.')
                return redirect('idea_form')


class IdeaUpdate(ActionMixin, UpdateView):
    model = Idea
    form_class = IdeaForm
    template_name_suffix = '_update_form'
    success_url = '/idea/{slug}'
    success_msg = "Idea successfully edited!"


class IdeaDelete(ActionMixin, DeleteView):
    model = Idea
    success_url = 'home'
    success_msg = "Idea successfully deleted!"


# Doesn't work :(
class CommentDelete(ActionMixin, DeleteView):
    model = Comment
    success_url = 'home'

    def get_context_data(self, **kwargs):
        context = super(CommentDelete, self).get_context_data(**kwargs)
        context['idea'] = self.idea
        return context


class IdeaDetail(DetailView):
    model = Idea
    form_class = IdeaForm

    def get_context_data(self, **kwargs):
        context = super(IdeaDetail, self).get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['vote_form'] = VoteForm()
        return context

    def post(self, request, *args, **kwargs):
        idea = get_object_or_404(Idea, slug=kwargs['slug'])

        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.idea = idea
            new_comment.save()
            messages.success(request, 'Your comment was added!')

        vote_form = VoteForm(request.POST)
        if vote_form.is_valid():
            new_vote = vote_form.save(commit=False)
            # Only save VoteForm data if vote was added
            if new_vote.vote_1:
                new_vote.idea = idea
                new_vote.save()
                messages.success(request, 'Your vote was tallied!')
                # success_msg = "Vote tallied!"
        return redirect('idea_detail', idea.slug,)

#
# Original def edit_idea ####
#

# # EditView
# def edit_idea(request, slug):
#     # grab the object
#     idea = Idea.objects.get(slug=slug)
#     # set the form we're using
#     form_class = IdeaForm
#     # if we're coming to this view from a submitted form
#     if request.method == 'POST':
#         # grab the data from the submitted form
#         form = form_class(data=request.POST, instance=idea)
#         if form.is_valid():
#             # save the new data
#             idea = form.save(commit=False)
#             idea.slug = slugify(idea.title)
#             return redirect('idea_detail', slug=idea.slug)
#     # otherwise just create the form
#     else:
#         form = form_class(instance=idea)
#     # and render the template
#     return render(request, 'ideas/edit_idea.html', {
#         'idea': idea,
#         'form': form,
#     })

##############################
# Original def new_idea #####
##############################

# # CreateView
# def new_idea(request):
#     # set the form we're using
#     form_class = IdeaForm
#     # if we're coming to this view from a submitted form
#     if request.method == 'POST':
#         # grab the data from the submitted form
#         form = form_class(request.POST)
#         if form.is_valid():
#             # save the new data
#             # everyone hates this part because form.save() will usually save ManyToMany,but it won't with commit=False

#             idea = form.save(commit=False)
#             idea.slug = slugify(idea.title)
#             idea.save()
#             return redirect('idea_detail', slug=idea.slug)
#     # otherwise just create the form
#     else:
#         form = form_class()
#     # and render the template
#     return render(request, 'ideas/new_idea.html', {
#         'form': form,
#     })

##############################
# Original def idea_detail ##
##############################

# def idea_detail(request, slug):
#     # grab the object...
#     idea = Idea.objects.get(slug=slug)
#     related_tags = Tag.objects.filter(idea=idea)
#     #idea.comment.all
#     related_comments = Comment.objects.filter(idea=idea)
#     related_votes = Vote.objects.filter(idea=idea)
#     #Ideas.votes.all
#     related_votes_total = related_votes.count()
#     #get_context_data
#     #CreateView
#     form_class = CommentForm
#     # if we're coming to this view from a submitted form
#     if request.method == 'POST':
#         # grab the data from the submitted form
#         form = form_class(request.POST)
#         if form.is_valid():
#             # save the new data
#             comment = form.save(commit=False)
#             comment.idea = idea
#             comment.save()
#             return redirect('idea_detail', slug=idea.slug)

#     # otherwise just create the form
#     else:
#         form = form_class()
#     # and render the template
#     return render(request, 'ideas/idea_detail.html', {
#         'form': form,
#         'idea': idea,
#         'related_tags': related_tags,
#         'related_comments': related_comments,
#         'related_votes': related_votes,
#         'related_votes_total': related_votes_total,
#     })
