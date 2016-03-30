from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

# @receiver(pre_save, sender=Tag)
# def tag_idea(sender, instance, *args, **kwargs):
#     instance.idea.tags.append(instance.name.filter(True))
#     instance.idea.tags.save()


class Idea(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('idea_detail', kwargs={'slug': self.slug})


@receiver(pre_save, sender=Idea)
def slug_catch(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)


class Vote(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    idea = models.ForeignKey(Idea)
    vote_1 = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
            ordering = ["idea", "-date"]


@receiver(post_save, sender=Vote)
def vote_total(sender, instance, *args, **kwargs):
    instance.idea.votes = instance.idea.vote_set.filter(vote_1=True).count()
    instance.idea.save()


class Comment(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    idea = models.ForeignKey(Idea)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["idea", "-date"]


# class User(models.Model):

    # profile information from API
