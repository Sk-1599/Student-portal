from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Inside models.py file we created Notes database table and table is bind to > form page and this form is imported to view file
class Notes(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	description = models.TextField()

	def __str__(self):
		return self.title

# Use to display data correctly in django administration
	class Meta:
		verbose_name = "notes"
		verbose_name_plural = "Notes"

class Homework(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	subject = models.CharField(max_length=50)
	title = models.CharField(max_length=100)
	description = models.TextField()
	due = models.DateTimeField()
	is_finished = models.BooleanField(default=False)

	def __str__(self):
		return self.title

class Todo(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	is_finished = models.BooleanField(default=False)

	def __str__(self):
		return self.title