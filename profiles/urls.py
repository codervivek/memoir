from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
from django.conf.urls import include

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^department/(?P<pk>\d+)$', views.DepartmentDetailView.as_view(), name='department-detail'),
    url(r'^professor/about/(?P<pk>\d+)$', views.ProfessorDetailView.as_view(), name='professor-detail'),
    url(r'^professor/category/(?P<pk>\d+)$', views.CategoryDetailView.as_view(), name='category-detail'),
]