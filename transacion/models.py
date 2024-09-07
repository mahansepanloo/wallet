from django.db import models
from accounts.models import Walet
class Transaction(models.Model):
    user = models.ForeignKey(Walet , on_delete=models.PROTECT)
    title = models.CharField(max_length=25)
    date = models.DateTimeField(auto_now=True)
    amount = models.FloatField()


