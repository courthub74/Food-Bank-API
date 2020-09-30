from django.db import models

class FoodBank(models.Model):
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=2)
	zipcode = models.CharField(max_length=200)
	phone = models.CharField(max_length=20)
	details = models.CharField(max_length=200)
	weblink = models.CharField(max_length=200)
	photo = models.ImageField(null=True, blank=True, upload_to="images/")

	def __str__(self):
		return self.name

