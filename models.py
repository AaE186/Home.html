#models

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # свои доп. поля, если есть
    pass
