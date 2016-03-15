from django.contrib import admin
from islideas.ideas.models import Idea, Tag, Comment, Vote


# Register your models here.
class IdeaAdmin(admin.ModelAdmin):
    model = Idea
    list_display = ('title', 'description', 'date', 'votes',)
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)


class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_display = ('name',)


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('idea', 'description', 'date',)


class VoteAdmin(admin.ModelAdmin):
    model = Vote
    list_display = ('idea', 'vote_1', 'date',)


admin.site.register(Idea, IdeaAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Vote, VoteAdmin)
