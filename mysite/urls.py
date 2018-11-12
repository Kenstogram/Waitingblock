#urls

from django.contrib import admin
from django.urls import path, include
#from django.conf.urls import include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
]
# Use include() to add paths from the catalog application

urlpatterns += [
    path('waitingblock/', include('waitingblock.urls')),
    path('waitingblock/', include('django.contrib.auth.urls')),
    path('tables/', include('django.contrib.auth.urls')),
]
#Add URL maps to redirect the base URL to our application

urlpatterns += [
    path('', RedirectView.as_view(url='/waitingblock/')),
]
