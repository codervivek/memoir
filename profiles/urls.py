from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
from django.conf.urls import include

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^department/(?P<pk>\d+)$', views.DepartmentDetailView.as_view(), name='department-detail'),
    url(r'^professor/(?P<pk>\d+)$', views.ProfessorDetailView.as_view(), name='professor-detail'),
]