# -*- coding: utf-8 -*-

from django.shortcuts import redirect

def home(request):
	if request.user.is_authenticated():
		next = 'private.views.home'
	else:
		next = 'public.views.home'

	return redirect(next)