from contextlib import nullcontext
from math import e
from multiprocessing import context
from pyexpat.errors import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import students,modretur
from django.urls import reverse
from django.template import loader
from .forms import modraturForm



def index(request):

   return render(request,"home.html")






global userName
userName=""
global password
password=0
def index2(request):
    if request.method == 'POST':
         if 'gender' in request.POST:
            userName =request.POST['userName']
            password =request.POST['password']
            gender =request.POST['gender']
            Email =request.POST['email']
            user=modretur(userName=userName,password=password,gender=gender,Email=Email)
            user.save()
            return redirect('index3')
         else:
            userName =request.POST['userName']
            password =request.POST['password']
            user=modretur.objects.get(userName=userName,password=password)
            print("hello")

            if(user):
               return redirect('index3')
            else:
                return render(request,'home.html')
    else:
        
        form = modraturForm()
        
    return render(request,'home_page.html',{'form':form})




def index3(request):
    
     return render(request,"home_registred.html")


def index4(request):
    if request.method == 'POST':
            name =request.POST['name']
            id1 =request.POST['ID']
            birthday =request.POST['birthday']
            gpa=request.POST['gpa']
            gender =request.POST['gender']
            level =request.POST['level']
            status=request.POST['status']
            depart=request.POST['department']
            email=request.POST['email']
            mobile=request.POST['mobile']
            user=students(name=name,id1=id1,birthday=birthday,gpa=gpa,gender=gender,
            level=level,status=status,depart=depart,email=email,mobile=mobile)
            user.save()
            
    else:
        
        form = modraturForm()
    
    return render(request,'new_student.html')



def index5(request):
    user=students()
    if request.method == 'POST':
            name =request.POST['name1']
            user=students.objects.get(name=name)
    context={'myobj':user}
    return render(request,"depart_sign.html",context)


def index6(request):
    
    if request.method == 'POST':
           
           
           oldid =request.POST['OldID']
           user=students.objects.get(id1=oldid)

           if 'delete' in request.POST:
               user.delete()
            


           name = request.POST['name']
           if(name!=''):
               user.name=name

           id1 = request.POST['id1']
           if(id1!=''):
               user.id1=id1  
               user.save()

           birthday= request.POST['birthday']
           if(birthday!=''):
                user.birthday=birthday
                user.save()

           gpa= request.POST['gpa']
           if(gpa!=''):
                user.gpa=gpa
                user.save()

           gender= request.POST['gender']
           if(gender!=''):
                user.gender=gender
                user.save()

           level= request.POST['level']
           if(level):
                user.level=level
                user.save()
        

           status= request.POST['status']
           if(status):
                user.status=status
                user.save()
        
           
    
           email= request.POST['email']
           if(email!=''):
                user.email=email
                user.save()
                
           mobile= request.POST['mobile']
           if(mobile!=''):
                user.mobile=mobile
                user.save()
             
         
            
    else:
        
        form = modraturForm()
    
    
    return render(request,"update_page.html")


def index7(request):
  id1=0
  user=students()
  if request.method == 'POST':
   id1 =request.POST['id1']
   user=students.objects.get(id1=id1)
  
   
  context={
     'myobj':user
  }
   
    
  return render(request,"student_info.html",context)


def index8(request):
    if request.method == 'POST':
            name =request.POST['name']
            status =request.POST['status']
            user=students.objects.get(name=name)
            user.status=status
            user.save()
    user2=students.objects.all()        
    context={
        'myobj':user2
    }


    return render(request,"table_act.html",context)


def index9(request):
    user=students()        
    if request.method == 'POST':
            name =request.POST['name2']
            user=students.objects.filter(name=name)
            

    return render(request,"tables (2).html",{'myobj':user})


def index10(request):
    user=modretur.objects.get(userName=userName)

    context={'myobj':user}

    return render(request,"profile Page.html",context)