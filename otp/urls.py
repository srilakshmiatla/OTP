"""
URL configuration for otp project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py

from django.contrib import admin
from django.urls import path
from app import views  # ✅ Correct import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('verify/', views.verify_otp, name='verify_otp'),
    path('resend/', views.resend_otp, name='resend_otp'),
    path('home/', views.login_view, name='home'),  # or your actual home view
]
