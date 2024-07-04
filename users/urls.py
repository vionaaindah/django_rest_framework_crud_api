from django.urls import path
from .views import *

urlpatterns = [
    path('user/fetch', FetchUsers.as_view(), name='fetch_users'),
    path('user/<int:user_id>', GetUser.as_view(), name='get_user'),
    path('user', CRUDUsers.as_view(), name='get_all_users')
]
