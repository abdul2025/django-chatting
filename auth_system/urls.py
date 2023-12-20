from django.urls import path, include
from .views import MyTokenObtainPairView, LogOutView


urlpatterns = [
    path('login', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout', LogOutView.as_view(), name='logoutView'),
]
