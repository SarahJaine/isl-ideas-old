from django.db import models


class Idea(models.Model):
    # user = models.ForeignKey(User)
    title = models.CharField(max_length=255,unique=True)
    description = models.TextField()
    tags = (
        # (WRB,   'wearable'),
        # (BIO,   'biohacking'),
        # (MUS,   'music'),
        # (TRV,   'travel'),
        # (EDU,   'education'),
        # (HOM,   'home automation'),
        # (AST,   'assistive technology'),
        # (OSS,   'open-source'),
        # (SMC,   'social media'),
        # add other tags
        )
    date = models.DateTimeField()
    votes = models.IntegerField()
    slug = models.SlugField(unique=True)

class Vote():
        vote = models.BooleanField()


class Comment(models.Model):
    # user = models.ForeignKey(User)
    idea = models.ForeignKey(Idea)
    description = models.TextField()
    date = models.DateTimeField()

    slug = models.SlugField(unique=True)


# class User(models.Model):
    # profile information from API
