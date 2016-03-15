from django.shortcuts import render
from django.http import HttpResponse
# from django.db.models import Sum
from django.views.generic import View, ListView, DetailView
from islideas.ideas.models import Idea, Tag, Comment, Vote


def index(request):
    ideas = Idea.objects.all().order_by('-date')
    return render(request, 'ideas/index.html', {
        'ideas': ideas,
        })


def idea_detail(request, slug):
    # grab the object...
    idea = Idea.objects.get(slug=slug)
    related_comments = Comment.objects.filter(idea=idea)
    related_votes = Vote.objects.filter(idea=idea)
    # and pass to the template
    return render(request, 'ideas/idea_detail.html', {
        'idea': idea,
        'related_comments': related_comments,
        'related_votes': related_votes,
    })

# class MyView(View):
#     def get(self, request, *args, **kwargs):
#         return HttpResponse("Hello, World")
