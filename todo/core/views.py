from django.shortcuts import get_object_or_404, redirect, render 
from django.views import View 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from .forms import UserCreateForm
from django.contrib.auth import login , authenticate 
from django.contrib.auth.forms  import AuthenticationForm 
from django.contrib import messages
from .forms import TaskFrom
from .models import Task
from .decorators import notAuth
from django.contrib.auth.models import User
from verify_email.email_handler import send_verification_email

class logout( LoginRequiredMixin,LogoutView) :
    redirect_field_name = None 
    next_page = 'login'

class Login(View) :
     @notAuth
     def get( self, request) :
        return  render(request  , "log/login.html" , {'form': AuthenticationForm()})

     def post( self, request) : 
            form  = AuthenticationForm(request.POST)
            auth = authenticate(username = request.POST["username"] , password = request.POST["password"] )

            if auth is not None: 
                login(request , auth)
                return redirect("home")
            else  : 
                messages.warning(request , "Username Or Password Invalid")
                return redirect("login")


class Register(View): 
    @notAuth
    def get(self  , request) :
        print(request.user)
        form = UserCreateForm()
        return render(request , 'log/register.html', locals())
    
    def post (self, request) : 
        form =UserCreateForm(request.POST)
        if form.is_valid(): 
            inactive_user = send_verification_email(request, form )
            return redirect('home')
        else : 
            return redirect('register')
        


class DeleteAcc (LoginRequiredMixin , View): 

    def get(slef  ,request) : 
        return render(request , 'log/delete.html')
    
    def post(slef,request) :
        user = User.objects.get(pk = request.user.pk)
        checkPass = user.check_password(raw_password=request.POST.get('pass'))
        if checkPass : 
            user.delete()
            messages.success(request, 'Account has been deleted')
            return redirect('login')
        else :
            messages.error(request, 'Password is wrong')
            return redirect('deleteACC')



class Home (LoginRequiredMixin,View ): 
    def get(self , request ): 
        tasks = request.user.tasks.filter(user=request.user)
        return render(request , 'home.html' , locals())

    def post(self, request): 
        form = TaskFrom(request.POST)
        if form.is_valid(): 
            Task(user =request.user  , task=form.cleaned_data['task'] , finish_at = form.cleaned_data['finish_at']).save()
            messages.success(request  , 'Task has been add')
            return redirect('home')
        else : 
            messages.error(request  , 'something invalid')
            return redirect('home')

class DeleteTask(  LoginRequiredMixin, View):
    def get(self , request , pk ): 
        return render(request , 'delete.html')
    
    def post(self ,request , pk): 
         task = get_object_or_404(request.user.tasks , pk=pk)
         task.delete()
         messages.success(request  , 'task has been deleted')
         return redirect('home')
    
class UpdateTask(  LoginRequiredMixin, View):
    def get(self , request , pk ): 
        task = get_object_or_404(request.user.tasks , pk=pk)
        form = TaskFrom(instance=task)
        return render(request , 'update.html' , locals())
    
    def post(self ,request , pk): 
         task = get_object_or_404(request.user.tasks , pk=pk)
         form = TaskFrom( request.POST, instance=task)
         form.save()
         messages.success(request  , 'task has been update')
         return redirect('home')
    




