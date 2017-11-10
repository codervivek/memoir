"""memoir URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from profiles.views import signup,LoginView,HomeView,LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^', include('profiles.urls')),
    url(r'^admin/', admin.site.urls,name='admin'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^signup/$', signup, name='signup'),
    url(r'login/$', LoginView.as_view(), name='login'),
    # url(r'home/$', HomeView.as_view(), name='home'),
    url(r'logout/$',LogoutView.as_view(), name='logout')
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)