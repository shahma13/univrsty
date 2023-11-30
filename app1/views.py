from django.shortcuts import render,redirect
from .models import Courses,StudentDetails,Teacher
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
import os

# Create your views here.
def login1(request):
    return render(request,'login1.html')


def home(request):
    return render(request,'home.html')

@login_required(login_url='login1')
def thome(request):
    return render(request,'thome.html')

def signup1(request):
    p=Courses.objects.all()
    return render(request,'signup1.html',{'course':p})

def sign(request):
    return redirect('signup1')

@login_required(login_url='login1')
def add_course(request):
    return render(request,'add_course.html')

@login_required(login_url='login1')
def add_stud(request):
    y=Courses.objects.all()
    return render(request,'add_stud.html',{'course':y})


@login_required(login_url='login1')
def table1(request):
    a=StudentDetails.objects.all()
    return render(request,'table1.html',{'pr':a})

@login_required(login_url='login1')
def table2(request):
    a=Teacher.objects.all()
    return render(request,'table2.html',{'ps':a})

@login_required(login_url='login1')
def edit_st(request,pk):
    z=StudentDetails.objects.get(id=pk)
    p=Courses.objects.all()
    return render(request,'edit_st.html',{'pro':z,'cc':p})

@login_required(login_url='login1')
def edit(request):
    z=Teacher.objects.get(user=request.user)
    p=Courses.objects.all()
    return render(request,'edit.html',{'pp':z,'cs':p})

@login_required(login_url='login1')
def add(request):
    if request.method=='POST':
        cname=request.POST['course']
        fee=request.POST['fee']
        x=Courses(course_name=cname,fee=fee)
        x.save()
        return redirect('add_stud')

@login_required(login_url='login1')  
def std_add(request):
    if request.method=='POST':
        sname=request.POST['name']
        address=request.POST['addr']
        age=request.POST['age']
        doj=request.POST['date']
        cs=request.POST['crs']
        z=Courses.objects.get(id=cs)
        x=StudentDetails(student_name=sname,address=address,age=age,doj=doj,course=z)
        x.save()
        return redirect('table1')
   
@login_required(login_url='login1')
def edit_page(request,pk):
    if request.method=='POST':
        student=StudentDetails.objects.get(id=pk)
        student.student_name=request.POST.get('name')
        student.age=request.POST.get('age')
        student.address=request.POST.get('addr')
        student.doj=request.POST.get('date')
        d=request.POST['crs']
        e=request.POST['fee']
        f=Courses.objects.get(id=d)
        f.fee=e
        f.save()
        student.course=f
        student.save()
        return redirect('table1')
    return render(request,'edit.html')

@login_required(login_url='login1')
def delete(request,pk):
    h=StudentDetails.objects.get(id=pk)
    h.delete()
    return redirect('table1')

@login_required(login_url='login1')
def deletes(request,pk):
    h=Teacher.objects.get(user=pk)
    k=User.objects.get(id=pk)
    h.delete()
    k.delete()
    return redirect('table2')

@login_required(login_url='login1')
def logout(request):
    auth.logout(request)
    return redirect('login1')

def adminlog(request):
    if request.method=='POST':
        username=request.POST['user']
        password=request.POST['pass']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('home')
            else:
                login(request,user)
                auth.login(request,user)
                return redirect('thome')
        else:
            messages.info(request,'invalid username or password')
            return redirect('/')
    return render(request,'login1.html')


def th_add(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=request.POST['user']
        passw=request.POST['pass']
        cpass=request.POST['repeat']
        email=request.POST['mail']
        address=request.POST['addr']
        age=request.POST['age']
        contact=request.POST['phone']
        image=request.FILES.get('img')
        cs=request.POST['crs']
        if passw==cpass:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'the username already exist')
                return redirect('/')
            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,username=uname,password=passw,email=email)
                user.save()
                z=Courses.objects.get(id=cs)
                u=User.objects.get(id=user.id)
             
                tr=Teacher(address=address,age=age,contact=contact,img=image,user=u,course=z)
                tr.save()
                return redirect('login1')
        else:
            messages.info(request,'password doesnt match')
            return redirect('signup1')

@login_required(login_url='login1')
def edit_page(request,pk):
    if request.method=='POST':
        student=StudentDetails.objects.get(id=pk)
        student.student_name=request.POST.get('name')
        student.age=request.POST.get('age')
        student.address=request.POST.get('addr')
        student.doj=request.POST.get('date')
        d=request.POST['crs']
        e=request.POST['fee']
        f=Courses.objects.get(id=d)
        f.fee=e
        f.save()
        student.course=f
        student.save()
        return redirect('table1')
    return render(request,'edit_st.html')

@login_required(login_url='login1')
def edit_pages(request,pk):
    if request.method=='POST':
        t=Teacher.objects.get(user=request.user)
        user=User.objects.get(id=pk)
        user.first_name=request.POST.get('fname')
        user.last_name=request.POST.get('lname')
        user.username=request.POST.get('user')
        user.email=request.POST.get('mail')
        t.address=request.POST.get('addr')
        t.age=request.POST.get('age')
        t.contact=request.POST.get('phone')
        # t.img=request.FILES.get('img')
        newimg=request.FILES.get('img')
        if newimg:
            if t.image:
                os.remove(t.img.path)
                t.img=newimg
        d=request.POST['crs']
        f=Courses.objects.get(id=d)
        f.save()
        t.course=f
        t.save()
        user.save()
        return redirect('thome')
    return render(request,'edit.html')

@login_required(login_url='login1')
def profile(request):
    return redirect('card')

# def scard(request):
#     z=Teacher.objects.get(user=request.user)
#     p=Courses.objects.all()
#     return render(request,'card.html',{'pp':z,'cs':p})
    
@login_required(login_url='login1')
def card(request):
    z=Teacher.objects.get(user=request.user)
    p=Courses.objects.all()
    return render(request,'card.html',{'pp':z,'cs':p})

@login_required(login_url='login1')
def goback(request):
    return redirect('thome')

@login_required(login_url='login1')
def sedit(request):
    return redirect('edit')