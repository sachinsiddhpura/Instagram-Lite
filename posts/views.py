from django.shortcuts import render

# Create your views here.
from .mixins import FormMixin,OwnerMixin
from .models import Posts
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
                CreateView,
                DetailView,
                DeleteView, 
                ListView, 
                UpdateView
                )

class PostDetail(DetailView):
	queryset = Posts.objects.all()

class PostCreate(FormMixin,CreateView):
	form_class = PostForm
	template_name = 'create.html'

class PostUpdate(LoginRequiredMixin,OwnerMixin,UpdateView):
	queryset = Posts.objects.all()
	form_class = PostForm
	template_name = 'update.html'

class PostDelete(LoginRequiredMixin,DeleteView):
	model = Posts
	template_name = 'delete.html'
	success_url = reverse_lazy('posts:list')

class PostList(LoginRequiredMixin,ListView):

	def get_queryset(self):
		qs = Posts.objects.all()
		query = self.request.GET.get('q')
		if query is not None:
			qs = qs.filter(Q(content__icontains=query),
							Q(user__username__icontains=query))
		return qs 

	def get_context_data(self,*args,**kwargs):
		context = super(PostList,self).get_context_data(*args,**kwargs)
		context['create_form'] = PostForm()
		context['craete_url'] = reverse_lazy('posts:create')
		return context
