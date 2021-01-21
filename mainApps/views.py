from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
import base64
from mainApps.models import User
from django.contrib import auth

# todo https://xd.adobe.com/view/643f99fe-c8cd-4ea8-9a20-0f9c4019409a-316c/

CDN_URL = "https://akamai-img.scdn.pw"
# Create your views here.


@login_required
def main(request):
    #Todo 좋아하는 고양이랑 장소가 없을 때 각각 예외처리 해주기
    userObject = User.objects.get(email=request.user)
    favoriteCats = userObject.favoriteCat.all()
    favoriteKitchens = userObject.favoriteKitchen.all()
    tempMentions = Mention.objects.none()

    if favoriteCats:
        for cat in favoriteCats:
            tempCat = cat.catmention_set.all()
            tempEmergency = cat.emergencymention_set.all()
            for catmention in tempCat:
                tempMentions = tempMentions.union(Mention.objects.filter(pk=catmention.mention.id))

            for emergencymention in tempEmergency:
                tempMentions = tempMentions.union(Mention.objects.filter(pk=emergencymention.mention.id))

    if favoriteKitchens:
        for kitchen in favoriteKitchens:
            tempKitchen = kitchen.kitchenmention_set.all()
            for kitchenmention in tempKitchen:
                tempMentions = tempMentions.union(Mention.objects.filter(pk=kitchenmention.mention.id))

    tempMention = tempMentions.order_by('-createdAt')[:10]


    return render(request, 'main.html',
                      {'Cats': favoriteCats, 'Kitchens': favoriteKitchens, 'recentMention' : tempMention})

    # mentionTarget.longitude등으로 접근가능
    # mentionTarget.breed등으로도 접근가능

    # Todo 사진 없으면 오류나니 디폴트 혹은 분기설정해서 오류안나게 하기


def map(request):
    return render(request, "map.html")


def intro(request):
    return render(request, "intro.html")


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

    catPost = CatPost.objects.filter(cat=catInfo)

    if not catPost:
        return render(request, 'info_cat.html', {"isFavorite": isFavorite, "catInfo": catInfo, "catFeatures": catFeatures, })
    else:
        catPhoto = catPost.catphoto_set.all()

    return render(
        request,
        "info_cat.html",
        {
            "isFavorite": isFavorite,
            "catInfo": catInfo,
            "catFeatures": catFeatures,
            "catPhoto": catPhoto,
        },
    )


def addFavoriteCat(request, thisCat_id):

    user = get_object_or_404(User, email=request.user)
    cat = get_object_or_404(Cat, pk=thisCat_id)
    user.favoriteCat.add(cat)

    return redirect("info_cat", thisCat_id)


def removeFavoriteCat(request, thisCat_id):
    user = get_object_or_404(User, email=request.user)
    cat = get_object_or_404(Cat, pk=thisCat_id)
    user.favoriteCat.remove(cat)

    return redirect("info_cat", thisCat_id)


def addFavoriteKitchen(request, thisKitchen_id):

    user = get_object_or_404(User, email=request.user)
    kitchen = get_object_or_404(Kitchen, pk=thisKitchen_id)
    user.favoriteKitchen.add(kitchen)

    return redirect('info_kitchen', thisKitchen_id)


def removeFavoriteKitchen(request, thisKitchen_id):
    user = get_object_or_404(User, email=request.user)
    kitchen = get_object_or_404(Kitchen, pk=thisKitchen_id)
    user.favoriteKitchen.remove(kitchen)

    return redirect('info_kitchen', thisKitchen_id)



def mention_kitchen(request, thisKitchen_id):

    kitchen = get_object_or_404(Kitchen, pk=thisKitchen_id)

    return render(request, 'mention_kitchen.html', {"kitchen": kitchen})


def info_kitchen(request, kitchen_id):
    kitchenInfo = get_object_or_404(Kitchen, pk=kitchen_id)
    isFavorite = False

    user = get_object_or_404(User, email=request.user)
    if user.favoriteKitchen.filter(pk=kitchen_id):
        isFavorite = True

    return render(request, 'info_kitchen.html',
                  {"isFavorite": isFavorite, "kitchenInfo": kitchenInfo})



def mypage(request):

    user = get_object_or_404(User, email=request.user)
    print(user.favoriteCat.all())

    attendanceBadge = False
    if user.checkIn >= 10:
        attendanceBadge = True

    return render(request, "mypage.html", {"user" : user, "attendaceBadge" : attendanceBadge})


def register(request):
    return render(request, "register.html")


@login_required
def register_cat(request):
    if request.method == "POST":
        post = Cat()
        post.name = request.POST["name"]
        post.breed = request.POST["breed"]
        post.isNeutered = request.POST["isNeutered"]
        post.gender = request.POST["gender"]
        post.feature = request.POST["feature"]
        post.image = request.FILES["uploadedImage"]
        post.save()
        post.favoriteKitchen.add(
            Kitchen.objects.get(pk=request.POST["kitchenid"]))

    return render(request, "register_cat.html")



@login_required
def register_kitchen(request):
    if request.method == "POST":
        kitchen = Kitchen()
        kitchen.name = request.POST["name"]
        kitchen.longitude = request.POST["longitude"]
        kitchen.latitude = request.POST["latitude"]
        kitchen.address = request.POST["address"]
        kitchen.description = request.POST["description"]
        kitchen.image = request.FILES["uploadedImage"]
        kitchen.save()

    return render(request, "register_kitchen.html")


def chatting(request):
    return render(request, "chatting.html")


def image_test(req):
    if req.method == "POST":
        image = ImageTest()
        image.image = req.FILES["image"]
        image.save()
        url = base64.b64encode(image.image.url.encode("UTF-8")).decode("UTF-8")
        url = f"{CDN_URL}/s:300:300/rt:fill/{url}"
        return redirect(url)
    else:
        return render(req, "image_test.html")





def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            email = request.POST["email"]
            password = request.POST["password"]
            user = auth.authenticate(email=email, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("main")
        return render(request, "login.html")  # TODO 로그인 틀리면 어디로?
    return redirect("main")


def sign_out(request):
    auth.logout(request)
    return redirect("main")


def join1(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            email = request.POST["email"]
            password = request.POST["password"]
            phoneNumber = request.POST["phoneNumber"]
            user = User.objects.create_user(
                email, None, phoneNumber, None, None, None, password
            )
            user.save()
            auth.login(request, user)
            return render(request, "join2.html")
        return render(request, "join1.html")
    return redirect("main")


def join2(request):

    if request.method == "POST":
        user = get_object_or_404(User, email=request.user.email)
        user.nickname = request.POST["nickname"]
        user.image = request.POST.get("image")
        user.save()

        return render(request, "join3.html")
    return render(request, "join2.html")


def join3(request):
    if request.method == "POST":
        user = get_object_or_404(User, email=request.user.email)
        print(request.user.email)
        print(request.user.email)
        print(request.POST["longitude"])
        user.longitude = request.POST["longitude"]
        user.latitude = request.POST["latitude"]
        user.save()
        return render(request, "join4.html")
    return render(request, "join3.html")


def join4(request):
    return render(request, "join4.html")


def read_qr(req):
    return render(req, 'qr_reader.html')

def readQRdetail(request, kitchen_id):
    user = User.objects.get(email=request.user.email)
    kitchen = Kitchen.objects.get(pk=kitchen_id)
    user.checkIn = user.checkIn + 1
    kitchen.checkIn = kitchen.checkIn + 1
    user.recentCheckin = kitchen
    user.save()
    kitchen.save()
    return redirect("info_kitchen", kitchen_id)


def newchat(req):
    return render(req, 'newchat.html')
