from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, FormMixin, ProcessFormView

from islideas.ideas.forms import IdeaForm, CommentForm
from islideas.ideas.models import Idea, Tag, Comment, Vote
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django import forms
from django.utils.text import slugify


class IdeaList(ListView):
    model = Idea
    queryset = Idea.objects.order_by('-date')


class IdeaCreate(CreateView):
    model = Idea
    form_class = IdeaForm
    success_url = '/idea/{slug}'


class IdeaUpdate(UpdateView):
    model = Idea
    form_class = IdeaForm
    template_name_suffix = '_update_form'
    success_url = '/idea/{slug}'


class CommentCreate(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'ideas/idea_detail.html'
    success_url = '/idea/{slug}'

##############################
### Detail View 2.0- shows detail, commentform-
#### Problems: comment saves orphaned from idea
#### from https://docs.djangoproject.com/en/1.9/topics/class-based-views/mixins/#an-alternative-better-solution

# # Get View
# class IdeaDisplay(DetailView):
#     model = Idea

#     def get_context_data(self, **kwargs):
#         context = super(IdeaDisplay, self).get_context_data(**kwargs)
#         context['form'] = CommentForm()
#         return context

# # Post view
# class CommentInterest(SingleObjectMixin, FormView):
#     template_name = 'ideas/idea_detail.html'
#     form_class = CommentForm
#     model = Idea

#     def post(self, request, *args, **kwargs):
#         if not request.user.is_authenticated():
#             return HttpResponseForbidden()
#         self.object = self.get_object()
#         form = CommentForm(request.POST)
#         form.save()
#         ### what it was supposed to be
#         # return super(CommentInterest, self).post(request, *args, **kwargs)
#         ### what I did for error checking
#         return HttpResponse("at post")


#     def get_success_url(self):
#         ### what it was supposed to be
#         # return reverse('author-detail', kwargs={'pk': self.object.pk})
#         ### what I did for error checking
#         return HttpResponse("at success")

# # Traffic sort
# class IdeaDetail(View):

#     def get(self, request, *args, **kwargs):
#         view = IdeaDisplay.as_view()
#         return view(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         view = CommentInterest.as_view()
#         return view(request, *args, **kwargs)

# ##############################
# ### Detail View 1.0- shows detail, commentform-
# #### Problems: submit loads blank pg, console error "405 (Method not allowed)"

class IdeaDetail(DetailView, FormMixin):
    model = Idea
    template_name = 'ideas/idea_detail.html'
    form_class = CommentForm
    success_url = '/idea/{slug}'


##############################
## Original def edit_idea ####
##############################

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
## Original def new_idea #####
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
## Original def idea_detail ##
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

