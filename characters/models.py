from django.db import models
from django.contrib.auth.models import User

class CharacterSheet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    character_name = models.CharField(max_length=100)
    character_class = models.CharField(max_length=100)

    def __str__(self):
        return self.character_name