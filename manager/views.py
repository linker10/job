from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required()
def manager(request):
    user = request.user
    return render(request, 'manager/manager.html')


@login_required
def deactivate(request):
    return render(request, 'manager/deactivate.html')   

@login_required
def deactivate_account(request):
    user = request.user
    user.is_active = False
    user.save()

    return redirect('home:index') 