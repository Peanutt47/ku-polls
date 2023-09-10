import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    """A question for the poll."""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('date ended', null=True, blank=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        """Return True if the question was published within the last day."""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    def is_published(self):
        """Return True if the question is published."""
        now = timezone.localtime(timezone.now())
        return self.pub_date <= now
    
    def can_vote(self):
        """Return True if the question can be voted on."""
        now = timezone.localtime(timezone.now())
        if self.end_date is None:
            return self.pub_date <= now
        else:
            return self.pub_date <= now <= self.end_date


class Choice(models.Model):
    """A choice for a question in the poll."""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text