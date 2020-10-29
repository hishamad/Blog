from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tutorial
from django.core.paginator import Paginator

class CategoryDetailView(DetailView):
	model = Category

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		page = self.request.GET.get('page')
		posts = paginator = Paginator(Post.objects.filter(category_id=self.kwargs.get('pk')).order_by('-date_posted'), 2)
		context['posts'] = posts.get_page(page)
		return context


class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 3


class PostDetailView(DetailView):
	model = Post

class TutorialListView(ListView):
	model = Tutorial
	template_name = 'blog/tutorials.html'

class TutorialDetailView(DetailView):
	model = Tutorial
