# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from solemne2.models import Post

# Create your views here.
def index(request):
  #return render(request, 'index.html', {})
	data = {}
	data['object_list'] = Post.objects.all().order_by('-id')
	template_name = 'index.html'
	return render(request, template_name, data)