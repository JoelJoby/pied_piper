from django.urls import path
from .views import CustomLoginView, SignupView, HomeView, CustomLogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('', HomeView.as_view(), name='home'),
]
