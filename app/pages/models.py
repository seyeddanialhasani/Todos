from django.db import models
from django.urls import reverse


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("author-detail", kwargs={"pk": self.pk})


class Tweets(models.Model):
    text = models.CharField(max_length=256)

    def __str__(self):
        return self.text
