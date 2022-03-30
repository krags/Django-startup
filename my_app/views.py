from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Keith',
        'title': 'Blog post 1',
        'content': 'First post',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Ted',
        'title': 'Blog post 2',
        'content': 'Second post',
        'date_posted': 'August 28, 2018'
    },

]

def my_app(request):
    context = {'posts': posts}
    return render(request, 'my_app/my_app.html', context)

def about(request):
    return render(request, 'my_app/about.html', {'title': 'Test'})

def test(request):
    blue = 4
    test_var= {
        'var1': 'Value',
        'var2': [1, 2, 3],
        'fox': 'grey',
        "blue": blue,
        'posts': posts,
        }
    return render(request, 'my_app/test.html', test_var)

def mypost(request):
    return render(request, 'my_app/mypost.html')

# def media(request):
#     return render(request, 'my_app/media.html')
