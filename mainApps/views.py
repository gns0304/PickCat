from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
import base64
from mainApps.models import User
from django.contrib import auth
from .mentions import *
#todo https://xd.adobe.com/view/643f99fe-c8cd-4ea8-9a20-0f9c4019409a-316c/

CDN_URL = "https://akamai-img.scdn.pw"
# Create your views here.

@login_required
def main(request):
    #Todo 좋아하는 고양이랑 장소가 없을 때 각각 예외처리 해주기
    userObject = User.objects.get(email=request.user)
    favoriteCats = userObject.favoriteCat.all()
    favoriteKitchens = userObject.favoriteKitchen.all()
    tempMentions = Mention.objects.none() #멘션들을 저장할 리스트 임시변수

    if not favoriteCats:
        for cat in favoriteCats:
            tempCat = cat.catmention_set.all()
            for catMention in tempCat:
                tempMentions = tempMentions.union(catMention.mention.all())

    if not favoriteKitchens:
        for kitchen in favoriteKitchens:
            tempKitchen = kitchen.kitchenmention_set.all()
            for kitchenMention in tempKitchen:
                tempMentions = tempMentions.union(kitchenMention.mention.all())

    if not tempMentions:
        return render(request, 'main.html', {'Cats': favoriteCats, 'Kitchens': favoriteKitchens})
    else:
        tempMention = tempMentions.order_by('-createdAt')[0]

        if tempMention.type == "K":
            mentionTarget = tempMention.kitchenmention_set.first().target
        elif tempMention.type == "C":
            mentionTarget = tempMention.catmention_set.first().target

        return render(request, 'main.html',
                      {'Cats': favoriteCats, 'Kitchens': favoriteKitchens, 'recentMention': tempMention.mention,
                       "mentionTarget": mentionTarget})

    # mentionTarget.longitude등으로 접근가능
    # mentionTarget.breed등으로도 접근가능

    # Todo 사진 없으면 오류나니 디폴트 혹은 분기설정해서 오류안나게 하기




def map(request):
    return render(request,'map.html')

def intro(request):
    return render(request,'intro.html')

def info_cat(request, cat_id):
    catInfo = get_object_or_404(Cat, pk=cat_id)
    catFeatures = []
    isFavorite = False

    user = get_object_or_404(User, email=request.user)

    if user.favoriteCat.filter(pk=cat_id):
        isFavorite = True

    if not catInfo.feature == "":
        catFeatures = catInfo.feature.strip()
        catFeatures = catFeatures.replace(" ", "")
        catFeatures = catFeatures.split("#")
        catFeatures.pop(0)

        for i in range(len(catFeatures)):
            catFeatures[i] = "#" + catFeatures[i]

    catPost = get_object_or_404(CatPost, cat=catInfo)
    catPhoto = catPost.catphoto_set.all()



    return render(request,'info_cat.html', {"isFavorite":isFavorite, "catInfo": catInfo, "catFeatures": catFeatures, "catPhoto" : catPhoto})


def addFavoriteCat(request, thisCat_id):

    user = get_object_or_404(User, email=request.user)
    cat = get_object_or_404(Cat, pk=thisCat_id)
    user.favoriteCat.add(cat)

    return redirect('info_cat', thisCat_id)

def removeFavoriteCat(request, thisCat_id):
    user = get_object_or_404(User, email=request.user)
    cat = get_object_or_404(Cat, pk=thisCat_id)
    user.favoriteCat.remove(cat)

    return redirect('info_cat', thisCat_id)

def mention_kitchen(request):
    return render(request,'mention_kitchen.html')

def info_kitchen(request):
    return render(request,'info_kitchen.html')


def mypage(request):
    return render(request,'mypage.html')

def register(request):
    return render(request,'register.html')

@login_required
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

@login_required
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

def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            email = request.POST["email"]
            password = request.POST["password"]
            user = auth.authenticate(email=email, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("main")
        return render(request, 'login.html') #TODO 로그인 틀리면 어디로?
    return redirect("main")

def sign_out(request):
    auth.logout(request)
    return redirect("main")



def join1(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            password = request.POST["password"]
            phoneNumber = request.POST["phoneNumber"]
            print(password)
            print(1)
            return render(request, "join2.html", {'password': password, 'phoneNumber':phoneNumber})
        return render(request, "join1.html")
    return redirect("main")


def join2(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            image = request.POST["image"]
            nickname = request.POST["nickname"]
            print(password)
            return render(request, 'join3.html', {
        'password': password, 'phoneNumber':phoneNumber,\
            'nickname': nickname, 'image':image})
        return render(request, "join2.html")
    return redirect("main")
    

def join3(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            longitude = request.POST["longitude"]
            latitude = request.POST["latitude"]
            return render(request, 'join4.html', {
        'password': password, 'phoneNumber':phoneNumber,'nickname': nickname, \
            'image':image, 'longitude':longitude, 'latitude':latitude})
        return render(request, "join3.html")
    return redirect("main")

def join4(request):
    return render(request,'join4.html')

