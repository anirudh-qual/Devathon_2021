from django.http import request
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.decorators import login_required
from .models import Application, Student, Scholarship
import datetime

from .forms import StudentForm,ScholarshipForm

# Create your views here.
def college(request):
    scholarships = Scholarship.objects.all()
    return render(request, "student\\home.html", {'scholarship':scholarships})

def scholarship(request, myid):
    details = Scholarship.objects.filter(id=myid).first()
    
    return render(request, "student\\scholarship.html", {'details':details})


def application_form(request,id):
    if not request.user.is_authenticated:
        return redirect("/login")
    
   
    
    student=Student.objects.get(user=request.user)
    scholarship=Scholarship.objects.get(id=id)
    application=Application(user=student,scholarship=scholarship)
    application.save()
    
    return render(request,"student\\application_form.html")

def create_user(request):
    if request.method=="POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            
            student.save()
            return redirect("/home")
    else:
        form=StudentForm()
    return render(request, "student\\profile_form.html", { 'form':form})




def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=="POST":   
            username = request.POST['username']
            email = request.POST['email']
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            
            if password1 != password2:
                messages.error(request, "Passwords do not match.")
                return redirect('/register')
            
            user = User.objects.create_user(username, email, password1)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return render(request, 'student\\login.html')   
    return render(request, "student\\register.html")
            
def interface(request):
    if not request.user.is_superuser:
        return redirect('/home')
    return redirect('/handle_admin')      
            



def loggedin(request):
    if request.user.is_authenticated:
        return interface(request)
    else:
        if request.method=="POST":
            username = request.POST['username']
            password = request.POST['password']
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, "Successfully Logged In")
                return interface(request)
            else:
                messages.error(request, "Invalid Credentials")
            return render(request, 'student\\home.html')   
    return render(request, "student\\login.html")

def loggedout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/login')


def status(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    
    student=Student.objects.get(user=request.user)
    application = Application.objects.filter(user=student) 
    return render(request, "student\\status.html", {'application':application})

def elgibility(student,scholarship):
    if student.caste not in scholarship.caste:
        return 0
    if student.branch not in scholarship.branch:
        return 0
    if datetime.date.today()<scholarship.openingtime or datetime.date.today()>scholarship.closingtime:
        return 0
    return 1

def display_scholarship(request,id):
    student=Student.objects.get(user=request.user)
    scholarship=Scholarship.objects.get(id=id)
    elgibile=elgibility(student,scholarship)
    return render(request,"student\\scholarship.html",{'scholarship':scholarship,'elgibility':elgibile})

def handle_admin(request):
    if not request.user.is_superuser:
        return redirect("/login")
    
    approve = Application.objects.filter(Application_Status='Approved').count
    reject = Application.objects.filter(Application_Status='Rejected').count
    pending = Application.objects.filter(Application_Status='Pending').count
    return render(request, "student\\adminhome.html", {'approve':approve, 'reject':reject, 'pending':pending})

def approved_applications(request):
    if not request.user.is_superuser:
        return redirect("/login")
    approved = Application.objects.filter(Application_Status="Approved")
    return render(request, "student\\approved_applications.html", {'approved':approved})

def pending_applications(request):
    if not request.user.is_superuser:
        return redirect("/login")
    pending = Application.objects.filter(Application_Status="Pending")
    return render(request, "student\\pending_applications.html", {'pending':pending})

def rejected_applications(request):
    if not request.user.is_superuser:
        return redirect("/login")
    rejected = Application.objects.filter(Application_Status="Rejected")
    return render(request, "student\\rejected_applications.html", {'rejected':rejected})

def student_application(request, myid):
    if not request.user.is_superuser:
        return redirect("/login")
    application = Application.objects.filter(id=myid)
    return render(request, "student\\student_application.html", {'application':application[0]})

def updateaccept(request,myid):
    application=Application.objects.get(id=myid)
    
    application.Application_Status='Approved'
    
    application.save()
    
    return redirect('/handle_admin') 

def updatereject(request,myid):
    application=Application.objects.get(id=myid)
    
    application.Application_Status='Rejected'
    
    application.save()
    
    return redirect('/handle_admin') 

def CreateScholarship(request):
     if request.method=="POST":
        form = ScholarshipForm(request.POST, request.FILES)
        if form.is_valid():
            scholarship = form.save()
            
            scholarship.save()
            return redirect("/handle_admin")
     else:
        form=ScholarshipForm()
     return render(request, "student\\scholarship_form.html", { 'form':form})
