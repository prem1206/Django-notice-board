from .models import Notice, Board
from .forms import UserLoginForm, UserRegisterForm, NoticeForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,get_user_model,login,logout
from django.contrib.auth.decorators import login_required




#@login_required
def list_notice(request, id):

    no = Board.objects.get(pk=id)
    notices = no.notice_set.all()
    return render(request, 'notices.html', {'notices': notices})

@login_required
def create_notice(request):
    form = NoticeForm(request.POST or None)
    if form.is_valid():
        form.save()
        ob = form.cleaned_data['topic']
        return redirect('list_notices',ob.id)
    return render(request, 'notices-form.html', {'form': form})

@login_required
def update_notice(request,id):
    notice = Notice.objects.get(id=id)
    form = NoticeForm(request.POST or None, instance=notice)

    if form.is_valid():
        form.save()
        ob = form.cleaned_data['topic']
        return redirect('list_notices',ob.id)
    return render(request, 'update_notices.html', {'form': form, 'notice': notice})


def register_user(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None, )
    if form.is_valid() :
        user = form.save(commit=False)
        role = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password,role=role)
        login(request, new_user)
        if next :
            return redirect(next)
        return redirect('/')

    context = {
        'form' : form,
    }
    return render(request, "signup.html", context)

@login_required
def delete_notice(request, id):
    notice = Notice.objects.get(id=id)
    obj = Board.objects.get(name=notice.topic)
    notice.delete()
    return redirect('list_notices',obj.id)



def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "login.html", context)




def logout_view(request):
    logout(request)
    return redirect('login')


