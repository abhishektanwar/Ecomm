from django.db import models
# importing abstract user class
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
	name = models.CharField(max_length=50, default='Anonymous')
	email = models.EmailField(max_length=50, unique=True)
	username = None

	# signing up the user on the basis of email instead of username
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	phone = models.CharField(max_length=20,blank=True, null = True)
	gender = models.CharField(max_length=10,blank=True, null = True)

	session_token = models.CharField(max_length=10, default=0)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
