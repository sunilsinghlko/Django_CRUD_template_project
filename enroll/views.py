from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from django.views.generic.base import View
from .models import User
# Create your views here.

class UserAddShow(View):
     def get(self,request):
          fm=StudentRegistration()
          stud=User.objects.all()
          return render(request,'enroll/addandshow.html',{'stu':stud,'form':fm})
     def post(self,request):
          fm=StudentRegistration(request.POST)
          if fm.is_valid():
               fm.save()
               return HttpResponseRedirect('/')
          



# def userAddShow(request):
#     if request.method=='POST':
#         fm = StudentRegistration(request.POST)
#         if fm.is_valid():
#                 fm.save()
#                 return HttpResponseRedirect('/')
        
#     fm = StudentRegistration()
#     stud = User.objects.all()
#     return render(request, 'enroll/addandshow.html', {'stu': stud,'form':fm})    
            

class UserUpdateView(View):
    def get(self, request, id):
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
        return render(request, 'enroll/updatestudent.html', {'form': fm})

    def post(self, request, id):
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
        return render(request, 'enroll/updatestudent.html', {'form': fm})
    

def deleteuser(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect('/')
