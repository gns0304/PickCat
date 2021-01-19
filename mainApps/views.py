from django.shortcuts import render

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