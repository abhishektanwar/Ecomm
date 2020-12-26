from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
   	# auto_now_add is only used when creating and auto_now is used when updating

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # changing the title of the data which is show in the admin panel
	# from Category object(1) to 'name' entered in the field
    def __str__(self):
        return self.name
