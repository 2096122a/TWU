from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

class Score(models.Model):
    player = models.ForeignKey(User)
    score = models.IntegerField(default=0)
    timestamp = models.DateField()

    def save(self, *args, **kwargs):
        if self.score <0:
            self.score*=(-1)
        super(Score, self).save(*args, **kwargs)

    def _unicode_(self):
        return self.score

