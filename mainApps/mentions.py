from django.shortcuts import render, redirect
from .models import CatMention, KitchenMention, EmergencyMention, Cat, Kitchen
from django.contrib.auth.decorators import login_required
import .sms

@login_required
def newCatMention(req):
    if req.method == 'POST':
        m = CatMention()
        m.user = req.user
        m.cat = Cat.objects.filter(pk=req.POST.catid)
        m.mention = req.POST.mention
        m.save()
        return redirect '/'
    else 

def newKitchenMention(req):
    pass

def newEmergencyMention(req):
    pass

def getCatMentions(req):
    Cat.objects.filter(pk=req.POST.catid).CatMention.order_by('-id')[:10]

def getKitchenMentions(req):
    pass

def getEmergencyMentions(req):
    pass