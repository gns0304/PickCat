from django.shortcuts import render, redirect
from .models import CatMention, KitchenMention, EmergencyMention, Cat, Kitchen, Mention, User
from django.contrib.auth.decorators import login_required
from .sms import *
from django.http import HttpResponse


@login_required
def newCatMention(req):
    if req.method == 'POST':
        m = CatMention()
        m.user = req.user
        m.cat = Cat.objects.filter(pk=req.POST.catid)
        m.mention = req.POST.mention
        m.save()
        return redirect('/')
    else:
        pass

def newKitchenMention(req):
    pass

@login_required
def newEmergencyMention(req):
    if req.method == 'POST':
        mention = Mention()
        mention.user = req.user
        mention.mention = req.POST['mention']
        mention.type = 'EMERGENCY'
        mention.save()
        m = EmergencyMention()
        kitchen = Kitchen.objects.get(pk=req.POST['kid'])
        m.target = kitchen
        m.mention = mention
        m.save()
        sms_user = User.objects.filter(favoriteKitchen=kitchen)
        to = []
        for a in sms_user:
            to.append(a.phoneNumber)
        text = f"{kitchen.name}에서 아래 내용의 긴급 메시지가 등록되었습니다.\n{mention.mention}"
        print(sms(to,text))
        return HttpResponse(str(to))
    else:
        return render(req,'emergency.html')

def getCatMentions(req):
    Cat.objects.filter(pk=req.POST.catid).CatMention.order_by('-id')[:10]

def getKitchenMentions(req):
    pass

def getEmergencyMentions(req):
    pass