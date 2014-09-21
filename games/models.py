from django.db import models


class PANTSGame(models.Model):
    session_id = models.CharField(max_length=30)
    place = models.CharField(max_length=300, null=True, blank=True)
    animal = models.CharField(max_length=300, null=True, blank=True)
    name = models.CharField(max_length=300, null=True, blank=True)
    thing = models.CharField(max_length=300, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.session_id

    def score(self):
        score = 0
        if self.place:
            score += 10
        if self.animal:
            score += 10
        if self.name:
            score += 10
        if self.thing:
            score += 10

        return score
