from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Student

# Create your views here.

def index(request):
    return render(request, "index.html")


def homePage(request):
    return HttpResponse("""<h1>this is home page</h1>""")


def mainPage(request):
    return render(request, "main.html", {"name":"mahesh", "rool_no":30})


def register(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        address = request.POST.get('address')

        std = Student()
        std.username = username
        std.email = email
        std.phone_number = phone_number
        std.address = address
        std.save()

        return redirect('/showdata/')
    return render(request, "registration.html")



def getStudentDetails(request):
    students = Student.objects.all()
    return render(request, "showdata.html", {"students": students})


def showUserData(request,id):
    std = Student.objects.get(id = id)
    print(std)
    return render(request, 'showuserdata.html', {'student': std})



def deleteUserData(request,id):
    std = Student.objects.get(id=id)
    std.delete()
    return redirect('/showdata/')


def updateData(request,id):
    std = Student.objects.get(id = id)
    if request.method == 'POST':
        std.username = request.POST.get('username')
        std.email = request.POST.get('email')
        std.phone_number = request.POST.get('phone')
        std.address = request.POST.get('address')
        std.save()
        return redirect('/showdata/')

    return render(request, 'update.html', {'student':std})