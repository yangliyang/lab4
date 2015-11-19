from django.db import models
<<<<<<< HEAD


=======
#
# Create your models here.
>>>>>>> C4
class Book(models.Model):
	ISBN=models.CharField(max_length=10)
	Title=models.CharField(max_length=10)
	AuthorID=models.CharField(max_length=10)
	Publisher=models.CharField(max_length=20)
	PublishDate=models.DateField()
	Price=models.CharField(max_length=10)
class Author(models.Model):
	AuthorID=models.CharField(max_length=10)
	Name=models.CharField(max_length=30)
	Age=models.CharField(max_length=3)
	Country=models.CharField(max_length=20)