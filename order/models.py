from django.db import models
from django.utils import timezone


class Order(models.Model):
    team = models.CharField(max_length=200)
    team_leader = models.CharField(max_length=200)
    quest = models.ForeignKey('quest.Quest')
    code = models.CharField(max_length=200)
    email = models.EmailField()
    vk = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    status = models.IntegerField()
    date = models.DateField()
    sent_date = models.DateField()

    def send(self):
        self.sent_date = timezone.now()
        self.save()

    def __str__(self):
        return self.team + ' (' + self.quest + ')'

