from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Michal',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 02, 2019',
    },
    {
        'author': 'Artur',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 02, 2019',
    },
]


#odbieranie requestów
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
