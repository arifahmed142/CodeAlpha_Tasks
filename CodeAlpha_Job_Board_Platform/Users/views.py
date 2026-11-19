from django.shortcuts import render, redirect
from .models import candidate,employer
from django.contrib.auth import authenticate, logout, login as logging
from django.contrib.auth.decorators import user_passes_test, login_required

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip().lower()
        password = request.POST.get('password')

        user = authenticate(
            request,
            username = username,
            password = password
        )
        if hasattr(user, 'candidate'):
            user = user.candidate
        elif hasattr(user, 'employer'):
            user = user.employer
            
        if user is not None:
            logging(request, user)
            return redirect('Home')
        return render(request, 'login.html', {'error':'User Not Found!'})
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name','').strip()
        username = request.POST.get('username','').strip().lower()
        email = request.POST.get('email','').strip().lower()
        phone = request.POST.get('phone','').strip()
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        actor = request.POST.get('actor')

        if not actor:
            return render(request, 'register.html', {'error':'Choose the user type!'})

        if actor == 'candidate':
            if not password or not confirm_password:
                return render(request, 'register.html', {'error':'Password Empty!'})
            if password != confirm_password:
                return render(request, 'register.html', {'error':'Password does not match!'})
            if candidate.objects.filter(phone = phone).exists():
                return render(request, 'register.html', {'error':'Phone Number Exists!'})
            if candidate.objects.filter(email = email).exists():
                return render(request, 'register.html', {'error':'Email Exists!'})
            if candidate.objects.filter(username = username).exists():
                return render(request, 'register.html', {'error':'Username taken!'})
            if name and username and email and phone and password:
                candidate.objects.create_user(
                    name = name,
                    username = username,
                    email = email,
                    phone = phone,
                    password = password,
                    is_candidate = True
                )
                return render(request, 'login.html', {'alert':'Candidate Sucessfully Registered.'})
            else:
                return render(request, 'register.html', {'error':'Every Field Must be Filled!'})
        if actor == 'employer':
            if not password or not confirm_password:
                return render(request, 'register.html', {'error':'Password Empty!'})
            if password != confirm_password:
                return render(request, 'register.html', {'error':'Password does not match!'})
            if employer.objects.filter(phone = phone).exists():
                return render(request, 'register.html', {'error':'Phone Number Exists!'})
            if employer.objects.filter(email = email).exists():
                return render(request, 'register.html', {'error':'Email Exists!'})
            if employer.objects.filter(username = username).exists():
                return render(request, 'register.html', {'error':'Username taken!'})
            if name and username and email and phone and password:
                employer.objects.create_user(
                    name = name,
                    username = username,
                    email = email,
                    phone = phone,
                    password = password,
                    is_employer = True
                )
                return redirect('Login')
            else:
                return render(request, 'register.html', {'error':'Every Field Must be Filled!'})
    return render(request, 'register.html')

@login_required
def profile(request):
    if hasattr(request.user, 'candidate'):
        user = request.user.candidate
    elif hasattr(request.user, 'employer'):
        user = request.user.employer
    else:
        return render(request, 'login.html', {'error':'User not available'})
    if request.method == 'POST':
        name = request.POST.get('name','').strip()
        email = request.POST.get('email','').strip().lower()
        phone = request.POST.get('phone','').strip()
        blood_group = request.POST.get('blood_group')
        nationality = request.POST.get('nationality')
        profile_photo = request.FILES.get('profile_photo')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')
        if name:
            user.name = name
        if email:
            user.email = email
        if phone:
            user.phone = phone
        if blood_group:
            user.blood_group = blood_group
        if nationality:
            user.nationality = nationality
        if present_address:
            user.present_address = present_address
        if permanent_address:
            user.permanent_address = permanent_address
        if profile_photo:
            user.profile_photo = profile_photo
        if user.is_candidate == True:
            resume = request.FILES.get('resume')
            ssc_board = request.POST.get('ssc_board')
            ssc_institution = request.POST.get('ssc_institution')
            ssc_result = request.POST.get('ssc_result')
            hsc_board = request.POST.get('hsc_board')
            hsc_institution = request.POST.get('hsc_institution')
            hsc_result = request.POST.get('hsc_result')
            if resume:
                user.resume = resume
            if ssc_board:
                user.ssc_board = ssc_board
            if ssc_institution:
                user.ssc_institution = ssc_institution
            if ssc_result:
                user.ssc_result = ssc_result
            if hsc_board:
                user.hsc_board = hsc_board
            if hsc_institution:
                user.hsc_institution = hsc_institution
            if hsc_result:
                user.hsc_result = hsc_result
        if user.is_employer == True:
            working_company = request.POST.get('working_company')
            designation = request.POST.get('designation')
            working_time = request.POST.get('working_time')
            cv = request.FILES.get('cv')
            if working_company:
                user.working_company = working_company
            if designation:
                user.designation = designation
            if working_time:
                user.working_time = working_time
            if cv:
                user.cv = cv
        user.save()
        return redirect('Profile')
    return render(request, 'profile.html', {'user':user})


@login_required
def auth_logout(request):
      logout(request)
      return redirect("Login")