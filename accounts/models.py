from django.db import models

# Create your models here.

class Token(models.Model):
    token = models.CharField(max_length=500 , null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.token
