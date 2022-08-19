from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="shophome"),
    path("about/",views.about,name="aboutus"),
    path("login/",views.login,name="login"),
    path("register/",views.register,name="register"),
    path("forgetpass/",views.forgetpass,name="forgetpass"),
    path("buynow/",views.buynow,name="buynow"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/",views.checkout,name="checkout"),
    path("contact/",views.contact,name="contact"),
    path("review/<int:myid>",views.review,name="review"),
    path("tracker/",views.tracker,name="tracker")
]