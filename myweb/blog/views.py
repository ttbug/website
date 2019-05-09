from django.shortcuts import render
from .models import Entry

# Create your views here.
def index(request):
    entries = Entry.objects.all()
    return render(request, 'blog/index.html', {'entrys':entries})

def detail(request, blog_id):
    entry = Entry.objects.get(id=blog_id)
    entry.increase_visiting()
    return render(request, 'blog/detail.html', locals())