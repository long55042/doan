from django.shortcuts import render
from .models import avatar
# Create your views here.
def list(request):
    Data = {'Posts': avatar.objects.all().order_by('-date')}
    return render(request, 'blog.html', Data)

def post(request, id):
    post = avatar.objects.get(id=id)
    return render(request, 'post.html', {'post': post})


# Create your views here.
