from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

from .forms import FormNewTask
from .models import task

# Create your views here.

def signUp(req):
    form = UserCreationForm
    if req.method == 'POST':
        if req.POST['password1'] == req.POST['password2']:
           try:
                user = User.objects.create_user(username=req.POST['username'], password=req.POST['password1'])
                user.save()
                login(req, user)
                return redirect('home')
           except IntegrityError:
              return render(req, 'formSignUp.html', {
                'formSignUp': form,
                'error': 'Usuario ya existe'
             })
           
        else:
             return render(req, 'formSignUp.html', {
                'formSignUp': form,
                'error': 'Las contraseñas no son iguales'
             })
    
    return render(req, 'formSignUp.html', {
        'formSignUp': form
    })

@login_required
def singOut(req):
    
    logout(req)
    return redirect('signin')

def signIn(req):
    if req.method == 'POST':
        user = authenticate(req, username=req.POST['username'], password=req.POST['password'] )
        if user is None:
            return render(req, 'signin.html', {
                'formSingIn':  AuthenticationForm,
                'error': 'Usuario o contraseña incorrectos'
            })
        else:
            login(req, user)
            return redirect('home')
                        
    return render( req, 'signin.html', {
        'formSingIn':  AuthenticationForm
    })
@login_required
def home(req):
    task_list = task.objects.filter(email = req.user)
    
    return render(req, 'home.html', {
        'task_list': task_list
    })
@login_required
def newtask(req):
    
    if req.method == 'POST':
        try:
            form = FormNewTask(req.POST)
            new_task = form.save(commit=False)
            new_task.email = req.user
            new_task.save()
            return redirect('home')
        except ValueError:
            return render(req, 'formSignUp.html', {
                'formSignUp': form,
                'error': 'Error al crear tarea'
             })
    
    return render(req, 'formnewtask.html', {
        'formNewTask': FormNewTask
    })
@login_required   
def updatetask(req, task_id):
    task_update = get_object_or_404(task, pk=task_id, email = req.user)
    if req.method == 'GET': 
        form = FormNewTask(instance=task_update)
        return render(req, 'formUpdateTask.html', {
                'task': task_update,
                'formUpdate': form
        })     
    else:
       try:
            form = FormNewTask(req.POST, instance= task_update)
            form.save()
            return redirect('home') 
       except ValueError:
            return render(req, 'formUpdateTask.html', {
                'formUpdate': form,
                'error': 'Error al actualizar la tarea'
        }) 
@login_required           
def deletetask(req, task_id):
    task_delete = get_object_or_404(task, pk=task_id, email = req.user)
    if req.method == 'POST': 
            task_delete.delete()
            return redirect('home')
           
        
  
    
    
        
    
    


