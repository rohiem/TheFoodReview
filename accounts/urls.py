from django.conf import settings
from django.urls import path, include
from .views import signup
from django.contrib.auth.views import LoginView,LogoutView

app_name = 'accounts'
urlpatterns = [
    path('signup', signup, name="signup"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(template_name="registration/logout.html"), name="logout"),

]