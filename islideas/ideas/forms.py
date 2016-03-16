from django.forms import ModelForm
from islideas.ideas.models import Idea, Comment


class IdeaForm(ModelForm):
    class Meta:
        model = Idea
        fields = ('title', 'description', 'tags',)


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('description',)
