from django.urls import path
from . import views
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from .views import register_view, login_view, logout_view
from .views import login_view
from .views import enroll
from .views import submit_partnership
from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('payment', views.payment_view, name='payment'),
    path('callback/', views.payment_callback, name='payment_callback'),
    path('stk-status/', views.stk_status_view, name='stk_status'),
    
    path('paypal_donate/', views.paypal_donate, name='paypal_donate'),
    path('mpesa-donate/', views.paypall_donate, name='mpesa_donate'),
    path('donate/', views.donate, name='donate'),
    
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),               
    path('services/', views.services, name='services'),      
    path('courses/', views.courses, name='courses'),         
    path('partners/', views.partners, name='partners'),       
    path('careers/', views.careers, name='careers'),         
    path('contact/', views.contact, name='contact'),          
    path(
        'login/', 
        auth_views.LoginView.as_view(
            template_name='login.html', 
            redirect_authenticated_user=False, 
            next_page='/home/'
        ), 
        name='login'
    ),    
    path('register/', views.register_view, name='register'),
    path("logout/", logout_view, name="logout"),
    path('submit_partnership/', views.submit_partnership, name ='submit_partnership'),
    path('team/',views.team, name='team'),
    path('mission/',views.mission, name='mission'),
    path('consulting/',views.consulting, name='consulting'),
    path('attarch/',views.attarch, name='attarch'),
    path('intern/',views.intern, name='intern'),
    path('training-and-workshops/', views.training_and_workshops, name='training_and_workshops'),
    path('register-workshop/', views.register_workshop, name='register_workshop'),
    path('workshop/<int:workshop_id>/', views.workshop_detail, name='workshop_detail'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path("enroll/", enroll, name="enroll"),
    path('submit-partnership/', submit_partnership, name='submit_partnership'),
    path("donate/success/", views.donate_success, name="donate_success"),
    path("donate/cancel/", views.donate_cancel, name="donate_cancel"),

]
