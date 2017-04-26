from django.shortcuts import render

from django.http import HttpResponse

from .models import Show
def index(request):
	data = Show.objects.get(pk=1)
	return render(request,'index/show.html',{'data':data})
	
def daoru(request):
	test = 'test'
	return render(request,'index/daoru.html',{'test':test})