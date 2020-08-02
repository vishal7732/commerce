from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['pass']
        password1 = request.POST['re_pass']

        if password == password1:
            if User.objects.filter(username=name).exists():
                messages.info(request, 'Username already exist')
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('registration')

            else:
                user = User.objects.create_user(username=name, email=email, password=password)
                user.save()
                print("Done")
                messages.info(request, 'Registration Successful')
                return redirect('/')

        else:
            messages.info(request, 'Passeword not matching')
            return redirect('registration')

    # return redirect('/')
    else:
        return render(request, 'registration.html')


