from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250, unique=True)

	class Meta:
		ordering = ('pk',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name


class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	date_posted = models.DateTimeField(default= timezone.now)
	author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
	image = models.ImageField(default='default.jpg', upload_to='post_pics')
	def __str__(self):
		return self.title


class Tutorial(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

	def __str__(self):
		return self.title