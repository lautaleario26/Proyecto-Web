from .models import Post 
from django.views.generic import ListView, DeleteView
# Create your views here.



class PostListView(ListView):
    model = Post
    template_name = "posts.html"
    context_object_name = "posts"

class PostDetailView(DeleteView):
    model = Post
    template_name = "posts/pot_individual.html"
    context_object_name = "posts"
    pk_url_kwarg = "id"
    queryset = Post.objects.all()