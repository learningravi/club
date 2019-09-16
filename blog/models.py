from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(("Just Another Post"), max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now=False, auto_now_add=True)
    author = models.ForeignKey(User, verbose_name=(""), on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.title 
    