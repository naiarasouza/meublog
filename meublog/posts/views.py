from django.shortcuts import render

from django.http import HttpResponse
def index(request):
	return HttpResponse('Olá, estamos na view do app posts')