from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http  import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
  if request.method != "POST":
    form = UserCreationForm()
  else:
    form = UserCreationForm(data=request.POST)
    if form.is_valid():
      new_user = form.save()
      login(request, new_user)
      return redirect("app_name:index")
  context = {"form": form}
  return render(request, "registration/register.html", context)

