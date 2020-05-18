from django.shortcuts import render
from .models import SiteUser
from .forms import UserCreationForm
# Create your views here.

def create_user(request):
    form = UserCreationForm()
    context = {"form" : form}
    return render(request, "createuser.html", context)

def user_created(request):
    new_user = UserCreationForm(request.POST)
    new_user.save()
    created_user = SiteUser.objects.order_by('id').last()
    user_name = created_user.first_name + " " + created_user.last_name
    context = {"user" : user_name}

    return render(request, "home.html", context)
