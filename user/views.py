from user.models import User, Role, Group, UserRole, UserGroup
from django.shortcuts import render, get_object_or_404
from pdb import set_trace as byebug
from django.http import JsonResponse
from django.core import serializers
import json


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


def getUser(request):
    user = User.objects.get(pk = request.POST['user_id'])
    # byebug()
    return JsonResponse(serializers.serialize('json', [user,]), safe=False)

def search(request):
    users = User.objects.filter(FullName__startswith= request.POST['firstname']).values("FullName","pk")
    # return JsonResponse(serializers.serialize('json', list(users)), safe=False)
    return JsonResponse({'result':list(users)})
#role part


def role_index(request):
    roles = Role.objects.order_by('Permission')
    return render(request, 'roles/index.html', {'roles': roles, 'title': 'All Role'})


def create_role(request):
    if len(request.POST['firstname']) < 5:
        return JsonResponse({
            'failure':'Name of Role error'
        })
    try:
        if 0 < int(request.POST['permission']) < 7:
            pass
        else:
            return JsonResponse({
                'failure': 'You must select permission'
            })
    except:
        return JsonResponse({
            'failure': 'You must select permission'
        })
    if request.POST['description'] == '':
        return JsonResponse({
            'failure': 'Description can not be blank'
        })

    new_role = Role(
        Name=request.POST['firstname'],
        Permission=request.POST['permission'],
        Description=request.POST['description']
    )
    new_role.save()
    if new_role:
        return JsonResponse({
            'success': 'Create successfully a new Role'
        })
    else:
        return JsonResponse({
            'failure': 'Create un-successfully a new Role'
        })


def edit_role(request):
    pass


def detail_role(request, role_id):
    role = get_object_or_404(Role, pk = role_id)
    # byebug()
    context = {
        'role':role,
        'title':'Role details',
        'users':role.userrole_set.all()
    }
    return render(request, "roles/detail.html", context)


def get_choice_field_role(request):
    return JsonResponse(Role._meta.get_field('Permission').choices, safe=False)


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


def add_user_to_role(request):
    try:
        role = Role.objects.get(id=request.POST['role_id'])
        member = User.objects.get(id=request.POST['user_id'])
        if role.userrole_set.filter(user=member).count()>0:
            return JsonResponse({
                'failure': 'The member %s already exists' % member.FullName
            })
        role.userrole_set.create(user=member)
        return JsonResponse({
            'success': 'The member %s added successfully' % member.FullName
        })
    except:
        return JsonResponse(
            {
                'failure': 'The role or user does not exist'
            }
        )
