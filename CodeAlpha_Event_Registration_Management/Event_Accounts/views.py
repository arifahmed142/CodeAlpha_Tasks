from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth import authenticate,logout, login as auth_login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q


# Create your views here.
def register(request):
    if request.method == 'POST':
        name = request.POST.get("name","").strip()
        email = request.POST.get("email", "").strip().lower()
        phone = request.POST.get("phone", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")
        profile_photo = request.FILES.get("profile_photo")
        if not name or not email or not phone or not password:
            return render(request,'register.html', {'error': 'Please fill all the field!'})
        if password != confirm_password:
            return render(request, 'register.html', {'error': 'Password did not match!'})
        if CustomUser.objects.filter(email=email).exists():
            return render(request,'register.html', {'error':'Email Exists. Use another!'})
        if CustomUser.objects.filter(phone = phone).exists():
            return render(request,'register.html', {'error':'Phone Number Exists. Use another!'})
        
        CustomUser.objects.create_user(
            name = name,
            email=email,
            phone=phone,
            password=password,
            profile_photo = profile_photo
        )
        return redirect("member_login")

    return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get("email","").strip().lower()
        password = request.POST.get("password","")

        user = authenticate(
            request,
            email = email,
            password = password
        )

        if user is not None:
            auth_login(request, user)
            return redirect('Home')
        return render(request, "login.html",{"error":"User Not Found!"})


    return render(request, 'login.html')

@login_required
def edit_profile(request):
    return render(request, "edit_profile.html")

@login_required
def editing_profile(request):
    member = request.user
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        nemail = request.POST.get('email', '').strip().lower()
        phone = request.POST.get('phone','').strip()
        password = request.POST.get('password','')
        confirm_password = request.POST.get('confirm_password','')
        profile_photo = request.FILES.get("profile_photo")

        if password and confirm_password:
            if password != confirm_password:
                return render(request, 'edit_member.html', {'error': 'Password did not match!'})
        elif password or confirm_password:
            return render(request, 'edit_member.html', {'error':'Either Enter both password or None!'})
        if nemail and CustomUser.objects.exclude(email=member.email).filter(email=nemail).exists():
            return render(request, 'edit_member.html', {'member': member,'error': 'Email already exists!'})
        if phone and CustomUser.objects.exclude(email=member.email).filter(phone=phone).exists():
            return render(request, 'edit_member.html', {'member': member,'error': 'Phone Number Exists. Use another!'})
        if name:
            member.name = name
        if nemail:
            member.email = nemail
        if phone:
            member.phone = phone
        if password:
            member.set_password(password)
        if profile_photo:
            member.profile_photo = profile_photo
        member.save()
        return redirect('member_profile')

    return render(request, 'member_profile.html', {'member': member})

@user_passes_test(lambda user: user.is_authenticated and user.is_superuser)
def memberlist(request):
    user = CustomUser.objects.filter(is_superuser=False)
    if user.exists:
        return render(request, 'member_list.html', {"user":user})
    else:
        return render(request, 'member_list.html', {"error":"No User Found!"})

@user_passes_test(lambda user: user.is_authenticated and user.is_superuser)
def searchmember(request):
    if request.method == 'POST':
        search = request.POST.get('search', '')
        if search:
            user = CustomUser.objects.filter(
                Q(name__icontains = search) |
                Q(email__icontains = search) |
                Q(phone__icontains = search)
            )
            user = user.filter(is_superuser=False)
            return render(request, 'member_list.html', {'user':user})
        else:
            return render(request, 'member_list.html', {'error':'No User Found!'})

@login_required
def profile(request):
    return render(request, "profile.html")

@login_required
def auth_logout(request):
    logout(request)
    return redirect('Home')

@login_required
def delete(request):
    member = request.user
    logout(request)
    member.delete()
    return redirect('member_login')