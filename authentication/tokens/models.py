from django.db import models

# Create your models here.
from django.contrib.auth.models import User, AbstractUser
from django.db import models

# Токен сессии пользователя
class Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
