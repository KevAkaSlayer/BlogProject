from django.shortcuts import render,redirect
from . import forms  
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post
# Create your views here.

# def add_author(request):
#     if request.method == 'POST':
#         author_form =forms.AuthorForm(request.POST)
#         if author_form.is_valid():
#             author_form.save()
#             return redirect('add_author')
        
#     else :
#         author_form =forms.AuthorForm()

#     return render(request,'add_author.html',{'form':author_form})


def register(request):
    if request.method == 'POST':
        register_form =forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Account created Successfully')
            return redirect('user_login')
        
    else :
        register_form =forms.RegistrationForm()

    return render(request,'register.html',{'form':register_form,'type':'register'})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username= user_name,password = user_pass)
            if user is not None :
                messages.success(request,'Logged in Successfully')
                login(request,user)
                return redirect('profile')
            else:
                messages.warning(request,'Login information incorrect')
                return redirect('user_login')
    else :
        form = AuthenticationForm()
        return render(request,'register.html',{'form':form,'type':'login'})
    


def user_logout(request):
    logout(request)
    return redirect('user_login')    



@login_required
def profile(request):
    data = Post.objects.filter(author=request.user)
    return render(request,'profile.html',{'data':data})

@login_required
def profile_upd(request):
    if request.method == 'POST':
        profile_form =forms.ChangeUserForm(request.POST,instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,'Profile Updated Successfully')
            return redirect('profile')
        
    else :
        profile_form =forms.ChangeUserForm(instance = request.user)

    return render(request,'updateprofile.html',{'form':profile_form,})


def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password Updated Successfully')
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request,'passchng.html',{'form':form})

