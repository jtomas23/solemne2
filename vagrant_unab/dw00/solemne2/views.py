# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from solemne2.models import Post
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

# Create your views here.
def index(request):
  #return render(request, 'index.html', {})
	data = {}
	data['object_list'] = Post.objects.all().order_by('-id')
	template_name = 'index.html'
	return render(request, template_name, data)

def noticia_detalle(request, pk):
  #return render(request, 'index.html', {})
	#data = {}
	#data['object_list'] = Post.objects.all().order_by('-id')
	template_name = 'noticia_detalle.html'
	data = get_object_or_404(Post, pk=pk)


	return render(request, template_name, data)