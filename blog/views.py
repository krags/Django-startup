from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
from django.views import View
from django.http import HttpResponse
from .forms import InputForm
from .models import Page
from .forms import ContactForm

def temp(request):
    return render(request, 'blog/index.html')

def home(request):
    # pagename = '/' + pagename
    # pg = get_object_or_404(Page, permalink=pagename)
    # context = {
    #     'title': pg.title,
    #     'content': pg.bodytext,
    #     'last_updated': pg.update_date,
    #     'page_list': Page.objects.all(),
    # }
    # assert False
    return render(request, 'blog/page.html')