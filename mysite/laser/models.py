from django.db import models

# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length = 200, verbose_name="Название")
	def __str__(self):
		return self.name
	class Meta:
		ordering = ['name']
		verbose_name = "Категории"
		verbose_name_plural = "Категории"

class SubCategory(models.Model):
	category = models.ForeignKey(Category)
	name = models.CharField(max_length = 200, verbose_name="Название")
	def __str__(self):
		return self.name
	class Meta:
		ordering = ['name']
		verbose_name = "Подкатегория"
		verbose_name_plural = "Подкатегории"

class Item(models.Model):
	subcategory = models.ForeignKey(SubCategory)
	name = models.CharField(max_length = 200, verbose_name="Название")
	price = models.IntegerField(blank = True, null = True)
	description = models.TextField(blank = True, null = True)
	image = models.FileField(upload_to='',blank = True, null = True)
	is_new = models.BooleanField(default = False)
	def __str__(self):
		return self.name
	def get_price(self):
		return str(self.price) + " руб." if self.price else "По договоренности"
	class Meta:
		ordering = ['name']
		verbose_name = "Товар"
		verbose_name_plural = "Товары"

class NewsArticle(models.Model):
	create_dt = models.DateTimeField(auto_now_add = True)
	title = models.CharField(max_length=200)
	body = models.TextField()
	is_published = models.BooleanField(default=False)
	image = models.FileField(upload_to='',blank = True, null = True)
	def __str__(self):
		return self.title
	class Meta:
		ordering = ['-create_dt']
		verbose_name = "Новость"
		verbose_name_plural = "Новости"