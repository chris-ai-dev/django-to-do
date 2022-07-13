from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import *

# Create your views here.
# @csrf_exempt
def index(request):
    # if request.method == "POST":
    return render(request,'to_do_app/index.html')

@csrf_exempt
def todos_new(request):
    if request.method == "POST":
        print("this is post:", request.POST)
        print("this is post:", request.POST.get('title'))
        print("this is post:", request.POST.get('title')[0])
        todo = Item(title=request.POST.get('title'), description=request.POST.get('description'), due_date =request.POST.get('due_date'))
        todo.save()
        return HttpResponse("test")
    elif request.method == "GET":
        print("this is get:",request.GET)
        return render(request,'to_do_app/todos_new.html')
        
# from blog.models import Blog
#  b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
# >>> b.save()
# class Item(models.Model):
#     title = models.CharField(max_length=50)
#     description = models.TextField()
#     due_date = models.DateField()
    
# @csrf_exempt
# def sign_up(request):
#     try:
#         body = json.loads(request.body)
#         User.objects.create_user(username=body['username'], password=body['password'], email=body['username'])
#     except Exception as e:
#         print('oops!')
#         print(str(e))
#     return HttpResponse('hi')