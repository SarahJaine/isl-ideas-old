from django.db import models
# from django.db.models import Sum

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    # TAGS = (
    #     ('WRB',   'wearable'),
    #     ('BIO',   'biohacking'),
    #     ('MUS',   'music'),
    #     ('TRV',   'travel'),
    #     ('EDU',   'education'),
    #     ('HOM',   'home automation'),
    #     ('AST',   'assistive technology'),
    #     ('OSS',   'open-source'),
    #     ('SMC',   'social media'),
    #     # add other tags
    #     )


class Idea(models.Model):
    # user = models.ForeignKey(User)
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    date = models.DateTimeField()
    votes = models.IntegerField()
    slug = models.SlugField(unique=True)


class Vote(models.Model):
    # user = models.ForeignKey(User)
    idea = models.ForeignKey(Idea)
    vote_1 = models.BooleanField()
    date = models.DateTimeField()


class Comment(models.Model):
    # user = models.ForeignKey(User)
    idea = models.ForeignKey(Idea)
    description = models.TextField()
    date = models.DateTimeField()


# class User(models.Model):
    # profile information from API
