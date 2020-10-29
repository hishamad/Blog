from .models import Category, Tutorial

def category(request):
	return { 'categories': Category.objects.all() }
	
def tutorial(request):
	return { 'tutorials': Tutorial.objects.all() }