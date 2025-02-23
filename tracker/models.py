from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Redactor(AbstractUser):
    years_of_experience = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(70)],
    )

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["username"]
