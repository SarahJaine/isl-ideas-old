from django.db import models
from datetime import datetime
from django.db.models import Count
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Idea(models.Model):
    # user = models.ForeignKey(User)
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    ## Maybe this should be date = models.DateTimeField(auto_now=True)?
    date = models.DateTimeField(default=datetime.now, blank=True)
    votes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Idea)
def slug_catch(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)


class Vote(models.Model):
    # user = models.ForeignKey(User)
    idea = models.ForeignKey(Idea)
    vote_1 = models.BooleanField()
    date = models.DateTimeField(default=datetime.now, blank=True)

## Vot tallying not working yet
# @receiver(pre_save, sender=Vote)
# def vote_total(sender, instance, *args, **kwargs):
#     instance.vote = Count(instance.vote_1)

# add __str to all
# add subclass Meta for default ordering etc for all


class Comment(models.Model):
    # user = models.ForeignKey(User)
    idea = models.ForeignKey(Idea)
    description = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ["date"]

    # def __str__(self):
    #     return self.description

# class User(models.Model):
    # profile information from API
