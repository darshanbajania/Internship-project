from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models her
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg',upload_to='profile_pic')
    pdf = models.FileField(default='user.pdf',upload_to='props/pdfs')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs')

    def __str__(self):
        return self.title


class Proposal(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to="proposals/pdfs")

    def __str__(self):
        return self.title