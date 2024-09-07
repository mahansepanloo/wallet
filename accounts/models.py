from django.db import models
from django.contrib.auth.models import User
class Walet(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    wallet = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.user.username


class Walet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet = models.IntegerField(null=True, blank=True, default=0)  # مقدار پیش‌فرض 0

    def add_amount(self, amount):
        if amount > 0:
            self.wallet += amount
            self.save()
        else:
            raise ValueError("Amount must be positive.")

    def __str__(self):
        return self.user.username