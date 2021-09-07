from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# inherits from the built in Model class
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # passing in the django utils timezone now function
    # note: it is not instantiated
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    # returns the path to a specific post
    def get_absolute_url(self):
        # reverse() returns the full path as a string
        return reverse('post-detail', kwargs={'pk':self.pk})
