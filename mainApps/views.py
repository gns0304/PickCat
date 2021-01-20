from django.shortcuts import render, redirect, get_object_or_404
from .models import *
import base64
from mainApps.models import User
from django.contrib import auth


CDN_URL = "https://akamai-img.scdn.pw"
# Create your views here.
def main(request):
    return render(request,'main.html')

def map(request):
    return render(request,'map.html')

def mypage(request):
    return render(request,'mypage.html')

def register(request):
    return render(request,'register.html')

def register_cat(request):
    if(request.method == 'POST'):
        post = Cat()
        post.name = request.POST['name']
        post.breed = request.POST['breed']
        post.isNeutered = request.POST['isNeutered']
        post.gender = request.POST['gender']
        post.feature = request.POST['feature']
        post.image = request.FILES['uploadedImage']
        post.save()
        post.favoriteKitchen.add(Kitchen.objects.get(pk=request.POST['kitchenid']))

    return render(request, 'register_cat.html')

def register_kitchen(request):
    if(request.method == "POST"):
        kitchen = Kitchen()
        kitchen.name = request.POST['name']
        kitchen.longitude = request.POST['longitude']
        kitchen.latitude = request.POST['latitude']
        kitchen.address = request.POST['address']
        kitchen.description = request.POST['description']
        kitchen.image = request.FILES['uploadedImage']
        kitchen.save()

    return render(request, 'register_kitchen.html')

def chatting(request):
    return render(request,'chatting.html')

def image_test(req):
    if req.method == 'POST':
        image = ImageTest()
        image.image = req.FILES['image']
        image.save()
        url = base64.b64encode(image.image.url.encode("UTF-8")).decode("UTF-8")
        url = f"{CDN_URL}/s:300:300/rt:fill/{url}"
        return redirect(url)
    else:
        return render(req,'image_test.html')

def sign_up(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            nickname = request.POST["nickname"]
            email = request.POST["email"]
            password = request.POST["password"]
            phoneNumber = request.POST["phoneNumber"]
            longitude = request.POST["longitude"]
            latitude = request.POST["latitude"]
            address = request.POST["address"]
            user = User.objects.create_user(email, nickname, phoneNumber, longitude, latitude, address, password)
            user.save()
            return redirect("main")
        return render(request, "sign_up.html")
    return redirect("main")

def sign_in(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            email = request.POST["email"]
            password = request.POST["password"]
            user = auth.authenticate(email=email, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("main")
        return render(request, 'sign_in.html') #로그인 틀리면 어디로?
    return redirect("main")

def sign_out(request):
    auth.logout(request)
    return redirect("main")