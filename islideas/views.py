from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.template.defaultfilters import slugify
from islideas.ideas.forms import IdeaForm, CommentForm
from islideas.ideas.models import Idea, Tag, Comment, Vote


class IdeaList(ListView):
    model = Idea
    context_object_name = 'posted_ideas'


# def index(request):
#     ideas = Idea.objects.all().order_by('-date')
#     return render(request, 'ideas/index.html', {
#         'ideas': ideas,
#     })


def idea_detail(request, slug):
    # grab the object...
    idea = Idea.objects.get(slug=slug)
    related_tags = Tag.objects.filter(idea=idea)
    related_comments = Comment.objects.filter(idea=idea)
    related_votes = Vote.objects.filter(idea=idea)
    related_votes_total = related_votes.count()

    form_class = CommentForm
    # if we're coming to this view from a submitted form
    if request.method == 'POST':
        # grab the data from the submitted form
        form = form_class(request.POST)
        if form.is_valid():
            # save the new data
            comment = form.save(commit=False)
            comment.idea = idea
            comment.save()
            return redirect('idea_detail', slug=idea.slug)

    # otherwise just create the form
    else:
        form = form_class()
    # and render the template
    return render(request, 'ideas/idea_detail.html', {
        'form': form,
        'idea': idea,
        'related_tags': related_tags,
        'related_comments': related_comments,
        'related_votes': related_votes,
        'related_votes_total': related_votes_total,
    })


def edit_idea(request, slug):
    # grab the object
    idea = Idea.objects.get(slug=slug)
    # set the form we're using
    form_class = IdeaForm
    # if we're coming to this view from a submitted form
    if request.method == 'POST':
        # grab the data from the submitted form
        form = form_class(data=request.POST, instance=idea)
        if form.is_valid():
            # save the new data
            idea = form.save(commit=False)
            idea.slug = slugify(idea.title)
            return redirect('idea_detail', slug=idea.slug)
    # otherwise just create the form
    else:
        form = form_class(instance=idea)
    # and render the template
    return render(request, 'ideas/edit_idea.html', {
        'idea': idea,
        'form': form,
    })


def new_idea(request):
    # set the form we're using
    form_class = IdeaForm
    # if we're coming to this view from a submitted form
    if request.method == 'POST':
        # grab the data from the submitted form
        form = form_class(request.POST)
        if form.is_valid():
            # save the new data
            idea = form.save(commit=False)
            idea.slug = slugify(idea.title)
            idea.save()
            return redirect('idea_detail', slug=idea.slug)
    # otherwise just create the form
    else:
        form = form_class()
    # and render the template
    return render(request, 'ideas/new_idea.html', {
        'form': form,
    })


# def new_comment(request):
#     # set the form we're using
#     form_class = CommentForm
#     # if we're coming to this view from a submitted form
#     if request.method == 'POST':
#         # grab the data from the submitted form
#         form = form_class(request.POST)
#         if form.is_valid():
#             # save the new data
            # comment = form.save(commit=False)
#             comment.save()
#             # return redirect(refresh)
#     # otherwise just create the form
#     else:
#         form = form_class()
#     # and render the template
#     return render(request, 'ideas/new_detail.html', {
#         'form': form,
#     })
# class MyView(View):
#     def get(self, request, *args, **kwargs):
#         return HttpResponse("Hello, World")
