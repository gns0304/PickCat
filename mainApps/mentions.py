from django.shortcuts import render, redirect
from .models import CatMention, KitchenMention, EmergencyMention, Cat, Kitchen, Mention, User, Chat
from django.contrib.auth.decorators import login_required
from .sms import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@login_required
def newCatMention(req):
    if req.method == 'POST':
        mention = Mention()
        mention.user = req.user
        mention.mention = req.POST['mention']
        mention.type = 'CAT'
        mention.save()
        m = CatMention()
        cat = Cat.objects.get(pk=req.POST['id'])
        m.target = cat
        m.mention = mention
        m.save()
        return None
    else:
        return None


@login_required
def newKitchenMention(req):
    if req.method == 'POST':
        mention = Mention()
        mention.user = req.user
        mention.mention = req.POST['mention']
        mention.type = 'KITCHEN'
        mention.save()
        m = KitchenMention()
        kitchen = Kitchen.objects.get(pk=req.POST['id'])
        m.target = kitchen
        m.mention = mention
        m.save()
        return None
    else:
        return None


@login_required
def newEmergencyMention(req):
    if req.method == 'POST':
        mention = Mention()
        mention.user = req.user
        mention.mention = req.POST['mention']
        mention.type = 'EMERGENCY'
        mention.save()
        m = EmergencyMention()
        cat = Cat.objects.get(pk=req.POST['id'])
        m.target = cat
        m.mention = mention
        m.save()
        sms_user = User.objects.filter(favoriteCat=cat)
        to = []
        for a in sms_user:
            to.append(a.phoneNumber)
        text = f"'{cat.name}'냥이에 대해 아래 내용의 긴급 메시지가 등록되었습니다.\n\n{mention.mention}"
        print(sms(to, text))
        return HttpResponse(str(to))
    else:
        return render(req, 'emergency.html')


def checkUser(req, user):
    if req.user == user:
        return True
    return False


@login_required
def getCatMentions(req):
    latest = req.GET.get('latest')
    if not latest:
        latest = 0
    mentions = CatMention.objects.filter(target_id=req.GET['id']).filter(
        id__gt=latest).order_by('-id')[:30]
    a = []
    for m in mentions:
        d = {
            'id': m.id,
            'name': m.target.name,
            'link': f"/info_cat/{m.target_id}",
            'image': m.target.image_url,
            'text': m.mention.mention,
            'is_me': checkUser(req, m.mention.user)
        }
        a.append(d)
    a = {
        'count': len(a),
        'data': a
    }
    return JsonResponse(a)


@login_required
def getKitchenMentions(req):
    latest = req.GET.get('latest')
    if not latest:
        latest = 0
    mentions = KitchenMention.objects.filter(
        target_id=req.GET['id']).filter(id__gt=latest).order_by('-id')[:30]
    a = []
    for m in mentions:
        d = {
            'id': m.id,
            'name': m.target.name,
            'link': f"/info_kitchen/{m.target_id}",
            'image': m.target.image_url,
            'text': m.mention.mention,
            'is_me': checkUser(req, m.mention.user)
        }
        a.append(d)
    a = {
        'count': len(a),
        'data': a
    }
    return JsonResponse(a)


@login_required
def getEmergencyMentions(req):
    pass


@csrf_exempt
@login_required
def newChat(req):
    if req.method == 'POST':
        c = Chat()
        c.user = req.user
        c.message = req.POST['message']
        c.save()
    return render(req, 'newchat.html')


def getChat(req):
    latest = req.GET.get('latest')
    if not latest:
        latest = 0
    chat = Chat.objects.filter(id__gt=latest).order_by('-id')[:30]
    a = []
    for m in chat:
        d = {
            'id': m.id,
            'name': m.user.nickname,
            'image': m.user.image_url,
            'text': m.message,
            'is_me': checkUser(req, m.user)
        }
        a.append(d)
    a = {
        'count': len(a),
        'data': a
    }
    return JsonResponse(a)
