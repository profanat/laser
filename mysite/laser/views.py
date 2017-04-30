from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
	context = {'categories': Category.objects.all(),'newsarticles':NewsArticle.objects.filter(is_published=True)[0:3]}
	return render(request, 'index.html',context)

def category_view(request, category_id):
	context = {'category': Category.objects.get(pk = category_id), 'categories': Category.objects.all()}
	return render(request, 'category_view.html',context)

def subcategory_view(request, category_id, subcategory_id):
	context = {'category': Category.objects.get(pk = category_id), 
			   'categories': Category.objects.all(),
			   'subcategory': SubCategory.objects.get(pk=subcategory_id)
			   }
	return render(request, 'subcategory_view.html',context)

def item_view(request, category_id, subcategory_id, item_id):
	context = {'category': Category.objects.get(pk = category_id), 
			   'categories': Category.objects.all(),
			   'subcategory': SubCategory.objects.get(pk=subcategory_id),
			   'item': Item.objects.get(pk=item_id),
			   }
	return render(request, 'item_view.html',context)

def all_news(request):
	context = {'categories': Category.objects.all(),'newsarticles':NewsArticle.objects.filter(is_published=True)}
	return render(request, 'all_news.html',context)

def newsarticle_view(request, newsarticle_id):
	context = {'categories': Category.objects.all(),'newsarticle':NewsArticle.objects.get(pk=newsarticle_id)}
	return render(request, 'newsarticle_view.html',context)

def new_items(request):
	context = {'categories': Category.objects.all(),'new_items':Item.objects.filter(is_new = True)}
	return render(request, 'new_items.html',context)