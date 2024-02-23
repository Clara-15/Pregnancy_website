from django.shortcuts import render
from.models import Article

def home_screen(request):
    articles=Article.objects.all()
    return render(request,'base.html',{'articles':articles})
# Create your views here.
