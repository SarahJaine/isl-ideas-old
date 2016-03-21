from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from islideas.ideas.forms import IdeaForm, CommentForm
from islideas.ideas.models import Idea, Tag, Comment, Vote


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


class IdeaDetail(DetailView):
    model = Idea


    ## This is the original way I was creating all my objects
    # idea = Idea.objects.get(idea=idea)
    # related_tags = Tag.objects.filter(idea=idea)
    # related_comments = Comment.objects.filter(idea=idea)
    # related_votes = Vote.objects.filter(idea=idea)
    # related_votes_total = related_votes.count()

    ## Both return all comments, not just comment on idea
    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super(IdeaDetail, self).get_context_data(**kwargs)
    #     context['posted_comments'] = Comment.objects.all()
    #     return context

    # def comments(self):
    #     return Comment.objects.all

##############################
## Original def edit_idea ##
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
## Original def new_idea ##
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
