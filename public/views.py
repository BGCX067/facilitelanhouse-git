# -*- coding: utf-8 -*-

# Create your views here.
from django.shortcuts import render_to_response

def home(request):
	title = 'Página inicial pública'
	return render_to_response('base.html', locals())
