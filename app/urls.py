from django.urls import path
from .views import home,main, signup, user_login

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('main/',main,name='main'),
    path('home/',home,name='home')
]


