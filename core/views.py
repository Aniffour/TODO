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

class logout( LoginRequiredMixin,LogoutView) :
    redirect_field_name = None
    next_page = 'login'

class Login(View) :
     def get( self, request) :
            form  = AuthenticationForm()
            return  render(request  , "log/login.html" , locals())

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
    def get(self  , request) :
        print(request.user)
        form = UserCreateForm()
        return render(request , 'log/register.html', locals())
    
    def post (self, request) : 
        form =UserCreateForm(request.POST)
        if form.is_valid(): 
            user = form.save() 
            login(request ,user )  
            return    redirect('home')
        else : 
            return redirect('register')
        



class Home (View , LoginRequiredMixin): 
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