from django.shortcuts import render, HttpResponse

# Create your views here.
#重要，前端界面相关

def index(request):
    return HttpResponse("欢迎使用")


def user_list(request):
    return HttpResponse("用户列表")


def user_add(request):
    return render(request,"user_add.html")