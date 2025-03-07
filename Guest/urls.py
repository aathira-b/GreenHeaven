from django.urls import path
from Guest import views
app_name="Guest"

urlpatterns = [
    path('Login/', views.login, name='Login'),
    path('Register/', views.register, name='Register'),
    path('designer/', views.designer, name='designer'),
    path('ajaxplace/', views.ajaxplace, name='ajaxplace'),
    path('shopreg/', views.shopreg, name='shopreg'),
    

    ]

