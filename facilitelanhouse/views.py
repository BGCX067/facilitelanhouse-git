# -*- coding: utf-8 -*-

from django.shortcuts import redirect

def home(request):
	if request.user.is_authenticated():
		next = 'private.views.index'
	else:
		next = 'public.views.index'

	return redirect(next)