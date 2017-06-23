# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from solemne2.models import Post
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
def index(request):
  #return render(request, 'index.html', {})
	data = {}
	data['object_list'] = Post.objects.all().order_by('-id')
	template_name = 'index.html'
	return render(request, template_name, data)

def noticia_detalle(request, pk):
	#data = {}
	#data['object_list'] = Post.objects.all().order_by('-id')
	posts = get_object_or_404(Post, pk=pk)
	template_name = 'noticia_detalle.html'
	return render(request, template_name,{'posts': posts})