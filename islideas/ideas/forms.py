from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from islideas.ideas.models import Idea, Comment, Vote, Tag


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


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)
