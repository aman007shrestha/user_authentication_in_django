from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
	return render(request, 'home/home.html')


@login_required
def about(request):
	return render(request, 'home/about.html')