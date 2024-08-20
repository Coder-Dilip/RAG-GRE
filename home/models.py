from django.db import models
from django.contrib.auth.models import User

class UserVocabulary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vocab = models.TextField()

    def __str__(self):
        return f"{self.user.username}: {self.vocab[:50]}..."  
