from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http.response import StreamingHttpResponse

def home(request):
    return render(request, 'index.html')
    
def category(request):
    return render(request, 'category.html')

def single_product(request):
    return render(request, 'single-product.html')

def checkout(request):
    return render(request, 'checkout.html')

def cart(request):
    return render(request, 'cart.html')

def confirmation(request):
    return render(request, 'confirmation.html')

def blog(request):
    return render(request, 'blog.html')

def single_blog(request):
    return render(request, 'single-blog.html')

def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['Password']

        user = auth.authenticate(username=name, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

