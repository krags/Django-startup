# https://www.w3schools.com/bootstrap/tryit.asp?filename=trybs_img_thumbnail2&stacked=h

# https://www.geeksforgeeks.org/python-uploading-images-in-django/?ref=lbp

# https://www.youtube.com/watch?v=N0D0A4Lb4w4

from django.shortcuts import render
from .models import Photo

def photo_carousel(request):
    queryset = Photo.objects.all()
    context = {
        "photos": queryset,
    }
    return render(request, 'resume_pics/photo_carousel.html', context)
