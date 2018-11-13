from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls import url
from django.urls import include, path
from waitingblock.views import WaitingblockView, CustomerUpdateView, TablesView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', WaitingblockView.as_view(), name='home'),
    path('waitingblock/', include('django.contrib.auth.urls')),
    path('success/', WaitingblockView.redirect_view),
    path('update/', CustomerUpdateView.as_view(), name='status_update'),
    path('tables/', TablesView.as_view(), name='tables'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.SignUp.as_view(), name='signup'),
    path('accounts/password_reset', views.PasswordReset.as_view(), name='password_reset'),
]
