from django.db import models

# Create your models here.
class Mylife(models.Model):
	englishname=models.CharField(max_length=20)
	age=models.DecimalField(max_digits=6,decimal_places = 0)
	birthday=models.CharField(max_length=20)
	constellation=models.CharField(max_length=3)
	likefood=models.CharField(max_length=50)
	likecountry=models.CharField(max_length=50)
	likesong=models.CharField(max_length=50)
	likemovietype=models.CharField(max_length=50)
	things=models.CharField(max_length=100)

	def __str__(self):
		return self.englishname


		
