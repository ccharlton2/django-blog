from django.db import models
# import the built in Django User model to allow extending
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    # specifying a one to one relationship with the User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # example of overriding the save method of a model
    def save(self, *args, **kwargs):
        # run the save method of the parent class using super()
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)