from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
	def seed_data(apps, schema_editor):
		user = CustomUser(name="abhishek",
						email="a@a.com",
						is_staff=True,
						is_superuser=True,
						phone="123456789",
						gender="Male"
					)
		user.set_password("12345")
		user.save()

	dependencies = [

	]

	operations = [
		migrations.RunPython(seed_data),
	]