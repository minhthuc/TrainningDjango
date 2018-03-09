from user.models import User, Role, Group
from django.shortcuts import render, get_object_or_404
from pdb import set_trace as byebug
from django.http import JsonResponse
from django.core import serializers


def index(request):
    users = User.objects.order_by("FullName")[:10]
    for user in users:
        if user.FullName == "":
            user.FullName = user.firstName + " " + user.lastName
            user.save()

    context = {
        'users' : users,
    }
    return render(request, "users/index.html", context)


def detail(request, user_id):
    user = get_object_or_404(User, pk = user_id)
    context = {
        'title' : user.FullName,
        'user' : user
    }
    return render(request, "users/detail.html", context)


def create(request):
    firstName = request.POST['firstname']
    lastName = request.POST['lastname']
    PassWord = request.POST['password']
    BirthDay = request.POST['birthday']
    Hobbies = request.POST['hobbies']
    Description = request.POST['description']
    # byebug()
    if len(firstName) < 3:
        return JsonResponse({
            'failure': 'The first name can not be empty'
        })
    if len(lastName) < 3:
        return JsonResponse({
            'failure': 'The last name can not be empty'
        })
    if len(PassWord) < 8:
        return JsonResponse({
            'failure': 'The PassWord can not be empty'
        })
    if validateDateTime(BirthDay):
        return JsonResponse({
            'failure': 'The BirthDay can not be empty or wrong format'
        })
    if Hobbies == '':
        return JsonResponse({
            'failure': 'The Hobbies name can not be empty'
        })
    if Description == '':
        return JsonResponse({
            'failure': 'The Description name can not be empty'
        })
    new_user = User(
        firstName=request.POST['firstname'],
        lastName=request.POST['lastname'],
        PassWord=request.POST['password'],
        BirthDay=request.POST['birthday'],
        Hobbies=request.POST['hobbies'],
        Description=request.POST['description'],
    )
    # byebug()
    new_user.save()
    if(new_user.pk > 0):
        return JsonResponse({
            'success': 'Create a new user successfully'
        })
    else:
        return JsonResponse({
            'failure' : 'Something wrong on creation user'
        })


def update(request, user_id):
    firstName = request.POST['firstname']
    lastName = request.POST['lastname']
    PassWord = request.POST['password']
    BirthDay = request.POST['birthday']
    Hobbies = request.POST['hobbies']
    Description = request.POST['description']
    if len(firstName) < 3:
        return JsonResponse({
            'failure': 'The first name can not be empty'
        })
    if len(lastName) < 3:
        return JsonResponse({
            'failure': 'The last name can not be empty'
        })
    if len(PassWord) < 8:
        return JsonResponse({
            'failure': 'The first name can not be empty'
        })
    if validateDateTime(BirthDay):
        return JsonResponse({
            'failure': 'The BirthDay can not be empty or wrong format'
        })
    if Hobbies == '':
        return JsonResponse({
            'failure': 'The Hobbies name can not be empty'
        })
    if Description == '':
        return JsonResponse({
            'failure': 'The Description name can not be empty'
        })
    try:
        user = User.objects.get(pk = user_id)
    except:
        return JsonResponse({
            'failure': 'User does not exist'
        })

    user.firstName = firstName
    user.lastName = lastName
    user.PassWord = PassWord
    user.BirthDay = BirthDay
    user.Hobbies = Hobbies
    user.Description = Description

    user.save()

    if (user.pk > 0):
        return JsonResponse({
            'success': 'Update successfully'
        })
    else:
        return JsonResponse({
            'failure': 'Something wrong on updating user'
        })


def delete(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except:
        return JsonResponse({
            'failure': 'Can not find user_id: %s' % user_id,
        })
    try:
        user.delete()
        return JsonResponse ({
            'success': 'Delete successfully'
        })
    except:
        return JsonResponse({
            'failure': 'Can not find user_id: %s' % user_id,
        })


def role_index(request):
    return render(request, 'roles/index.html')


def validateDateTime(input):
    if(len(input) != 10):
        return False
    a, b, c = input.split("-")
    try:
        if(int(a)>1990 & 1<int(b)<12 & 1<int(c)<31):
            return True
        else:
            return False
    except:
        return False


def getUser(request):
    user = User.objects.get(pk = request.POST['user_id'])
    # byebug()
    return JsonResponse(serializers.serialize('json', [user,]), safe=False)

def get_choice_field_role():
    # byebug()
    return JsonResponse(Role._meta.get_field('Permission').choices, safe=False)