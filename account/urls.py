from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView
)
from account.views import (
    RegisterAPIView,
)


urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register')
]