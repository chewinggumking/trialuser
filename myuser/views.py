from django.shortcuts import render

from .forms import UserCreationForm
# Create your views here.

def create_user(request):
    form = UserCreationForm()
    context = {"form" : form}
    return render(request, "createuser.html", context)
