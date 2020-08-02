from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('category', views.category, name="category"),
    path('single-product', views.single_product, name="single-product"),
    path('checkout', views.checkout, name="checkout"),
    path('cart', views.cart, name="cart"),
    path('confirmation', views.confirmation, name="confirmation"),
    path('blog', views.blog, name="blog"),
    path('single-blog', views.single_blog, name="single_blog"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    
]
