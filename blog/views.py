from django.shortcuts import render
from .models import Post    #O ponto antes de models significa diretório atual ou aplicativo atual. Tanto views.py como models.py
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'blog/post_list.html', {'posts': posts}})
