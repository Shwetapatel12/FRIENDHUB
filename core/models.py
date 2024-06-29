from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='staics/images/book-icon.png')
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.get_username
    
    