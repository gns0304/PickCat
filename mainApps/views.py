from django.shortcuts import render
from .models import *
# Create your views here.
def main(request):
    return render(request,'main.html')

def map(request):
    return render(request,'map.html')

def mypage(request):
    return render(request,'mypage.html')

def register(request):
    return render(request,'register.html')

def chatting(request):
    return render(request,'chatting.html')

def image_test(req):
    if req.method == 'POST':
        image = ImageTest()
        image.image = req.FILES['image']
        image.save()
        return render (req, 'image_test.html')
    else:
        return render(req,'image_test.html')