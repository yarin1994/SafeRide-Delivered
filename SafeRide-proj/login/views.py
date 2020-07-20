from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User     

from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .forms import ScooterForm, createUserForm
from .models import Scooter
import json
from django.conf import settings
 
import os

def registerform(request):
    if request.method == 'GET':
        return render(request, 'login/registerform.html', {'form':createUserForm()})
    else:
            if request.POST['password1'] == request.POST['password2']:
                try:
                    staff  = request.POST.get('is_staff', False)
                    if staff == 'on':
                        staff = True
                    else:
                        staff = False
                    user = User.objects.create_user(request.POST['username'],password=request.POST['password1'], email = request.POST['email'], is_staff = staff  )
                    user.save()
                    login(request, user)
                    return redirect('index')
                except IntegrityError:
                    return render(request, 'login/registerform.html', {'form':createUserForm(),'errMsg':'User name already exists, Choose another one'})

            else:
                return render(request, 'login/registerform.html', {'form':createUserForm(),'errMsg':'Password did not match'})

def index(request):
    json_path = os.path.join(settings.STATIC_ROOT, 'login','js','logos.json')
    with open(json_path) as f:
                json_logos = json.load(f)
    scooters = Scooter.objects.all()
    images_path = os.path.join(settings.STATIC_URL,'login')
    context = {
        'allscooters':scooters, 
        'logos': json_logos,
        'image_folder_path': images_path
    }
    return render(request, 'login/index.html', context)





    # scooters = Scooter.objects.all()
    # return render(request, 'login/index.html', {'allscooters':scooters})
    # return render(request, 'login/index.html')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('LandingPage')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'login/loginpage.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username= request.POST['username'], password= request.POST['password'] )
    if user is None:
        return render(request, 'login/loginpage.html', {'form':AuthenticationForm(), 'errMsg':'User does not exist'})
    else:
        login(request, user)
        return redirect('index')


def homepage(request):
    return render(request, 'login/LandingPage.html')

    
def createNewScooter(request):
    if request.method == 'GET':
        return render(request,'login/form.html', {'form':ScooterForm()})
    else:
        try:
            form = ScooterForm(request.POST)
            newscooter = form.save(commit=False)
            newscooter.user_id = request.user
            newscooter.save()
            return redirect('index')
        except ValueError:
            return render(request, 'login/form.html', {'form':ScooterForm(), 'errMsg':'Data mismatch'})

def my_scooters(request):
    json_path = os.path.join(settings.STATIC_ROOT, 'login','js','logos.json')
    with open(json_path) as f:
                json_logos = json.load(f)
    scooters = Scooter.objects.filter(user_id= request.user)
    images_path = os.path.join(settings.STATIC_URL,'login')
    context = {
        'allscooters':scooters, 
        'logos': json_logos,
        'image_folder_path': images_path
    }
    return render(request, 'login/vendor_list.html', context)



# def updatescooter(request, scooter_pk):
#     scooters = get_object_or_404(Scooter, pk= scooter_pk, user_id = request.user)

#     if request.method == 'POST':
#         form - ScooterForm(instance=scooters)
#         return render(request, 'login/updatescooter.html', {'scooters':scooters, 'form':form})
#     else:
#         try:
#             form = ScooterForm(request.POST, instance=scooters)
#             form.save()
#             return redirect('vendor_list.html')
#         except ValueError:
#             return render(request, 'login/updatescooter.html', {'form':ScooterForm(), 'errMsg':'Data mismatch'})

def updateScooter(request, pk):
    scooter = Scooter.objects.get(id = pk)
    form = ScooterForm(instance=scooter)   
    if request.method == 'POST':
        form = ScooterForm(request.POST, instance=scooter)
        if form.is_valid():
            form.save()
            return redirect('myScooters')

    context = {'form':form}
    return render(request, 'login/updateScooter.html', context)
    
  

def deleteScooter(request, pk):
    scooter = Scooter.objects.get(id = pk)

    scooter.delete()
    return redirect('myScooters')
   

    
# def logos(request):
#     scooter_logos = [
#         {'brand':'bird','url':'../images/bird.png'},
#         {'brand':'lime','url':'../images/lime.png'},
#         {'brand':'wind','url':'../images/wind.png'}
#     ]

#     return JsonResponse({'scooter_logos':scooter_logos})
