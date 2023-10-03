import random, string, datetime
from uuid import uuid4
from slugify import slugify

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.CharField(max_length=32, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_activity_at = models.DateTimeField(auto_now=True)
    
    # Информация о пользователе
    email = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)
    full_name = models.CharField(max_length=128, null=False)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "users"

    def __str__(self):
        return f"User: {self.username}"

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = slugify(self.full_name[:30], separator="")

        if not self.secret_hash:
            letters = string.ascii_lowercase
            self.secret_hash = self.username[:6] + ''.join(random.choice(letters) for i in range(18))

        self.updated_at = datetime.utcnow()
        return super().save(*args, **kwargs)

    def to_dict(self):
        return {
            "id": str(self.id),
            "username": self.username,
            "full_name": self.full_name,
            "bio": self.bio,
            "created_at": self.created_at.isoformat(),
        }