from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('profile/', user_profile, name='profile'),
    path('profile/edit/', user_edit_profile, name='edit_profile'),
    path('profile/change_password/', user_change_password, name='change_password'),
]