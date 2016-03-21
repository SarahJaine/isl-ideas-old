from django.forms import ModelForm
from islideas.ideas.models import Idea, Comment, Vote


class IdeaForm(ModelForm):
    class Meta:
        model = Idea
        fields = ('title', 'description', 'tags',)


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('description',)


class VoteForm(ModelForm):
    class Meta:
        model = Vote
        fields = ('vote_1',)
