from django.shortcuts import render,get_object_or_404,redirect
from .models import  Post
from django.views.generic import ListView






class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    pagainate_by = 5
    template_name = 'blog/post/list.html'



def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, 
                             status='published', 
                            publish__year=year, 
                            publish__month=month, 
                            publish__day=day)
    
    return render(request, 'blog/post/detail.html', {'post': post})






# def post_create_view(request):
#     form = PostForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return redirect('post_list') 
   
        
#     return render(request, 'post_create.html', {'form': form})



# def post_list_view(request):
#     posts = Post.published.all()
#     print(posts.query)
#     return render(request, 'post_list.html', {'posts': posts})

