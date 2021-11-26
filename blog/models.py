from django.contrib.auth.models import User, AbstractUser
from django.db import models

# Create your models here.
class CRYPTO(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cryptocurrency = models.CharField(max_length=150, blank=True, null=True)
    price = models.PositiveIntegerField()


    def __str__(self):
        return str(self.user)
