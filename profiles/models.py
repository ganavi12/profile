from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    boi = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    Ivatar = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.user.username
    
class ProfileStatus(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status_content = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "status"

    def __str__(self):
        return str(self.user_profile)
