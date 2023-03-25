from django.shortcuts import render


def single_blog(request):
    return render(request, 'pages/single-blog.html' )
