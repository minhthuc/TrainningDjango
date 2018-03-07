from django.http import HttpResponse
from user.models import User
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    user = User.objects.order_by("FullName")[:10]
    return render(request, "users/index.html",user)