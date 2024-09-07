from django.db import models
from accounts.models import Walet
class Plan(models.Model):
    user = models.ForeignKey(Walet,on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    description = models.TextField()
    req_budget = models.FloatField()
    sat_budget = models.FloatField()
    status = models.CharField(max_length=10)


