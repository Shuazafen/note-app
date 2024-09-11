from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import *

@login_required(login_url='/login')
def home(request):
    notes = Note.objects.filter(created_by=request.user)
    return render(request, 'index.html', {'notes':notes, "user":request.user})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(username, email, password1)
            user.save()
            auth.login(request, user)
            return redirect('home')
        return render(request,'login.html',{'success':'Account'})
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(user)
            auth.login(request, user)
            print("user login")
            return redirect('home')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def create(request):
    form = Note.objects.all()
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        image = request.POST['image']
        form_info = Note(title=title, content=content, image=image)
        form_info.created_by = request.user
        form_info.save()
        return redirect('home')
    else:
        print('Not sent')
    return render(request, 'new.html',{'form':form})   

def delete_note(request, pk):
    notes = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        notes.delete()
        return redirect('home')
    return render(request, 'delete.html', {'note': notes})

def update_note(request, pk):
    note = get_object_or_404(Note, pk=pk) 

    if request.method == 'POST':
        new_title = request.POST.get('title', '')
        new_content = request.POST.get('content', '')
        new_image = request.FILES.get('image')
        
        # Validate form data
        if not new_title:
            return render(request, 'edit.html', {"note": note, "error": "Title is required."})

        if not new_content:
            return render(request, 'edit.html', {"note": note, "error": "Content is required."})

        if not new_image:
            return render(request, 'edit.html', {"note": note, "error": "Image is required."})

        note.title = new_title
        note.content = new_content
        note.image = new_image
        note.save()

        return redirect('note_list')

    return render(request, 'edit.html', {"note": note})
