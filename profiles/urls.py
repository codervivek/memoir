from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
from django.conf.urls import include

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^department/(?P<pk>\d+)$', views.DepartmentDetailView.as_view(), name='department-detail'),
    url(r'^professor/about/(?P<pk>\d+)$', views.ProfessorDetailView.as_view(), name='professor-detail'),
    url(r'^professor/category/(?P<pk>\d+)$', views.CategoryDetailView.as_view(), name='category-detail'),
    url(r'^professor/create/$', views.ProfessorCreate.as_view(), name='professor_create'),
    url(r'^professor/update/(?P<pk>\d+)/$', login_required(views.ProfessorUpdate.as_view()), name='professor_update'),
    url(r'^professor/delete/(?P<pk>\d+)/$', login_required(views.ProfessorDelete.as_view()), name='professor_delete'),
    url(r'^category/create/$', views.CategoryCreate.as_view(), name='category_create'),
    url(r'^category/update/(?P<pk>\d+)/$', login_required(views.CategoryUpdate.as_view()), name='category_update'),
    url(r'^category/delete/(?P<pk>\d+)/$', login_required(views.CategoryDelete.as_view()), name='category_delete'),
    url(r'^categorylist/create/(?P<pk>\d+)/$', views.categorylist_create, name='categorylist_create'),
    url(r'^categorylist/update/(?P<pk>\d+)/$', login_required(views.CategoryListUpdate.as_view()), name='categorylist_update'),
    url(r'^categorylist/delete/(?P<pk>\d+)/$', login_required(views.CategoryListDelete.as_view()), name='categorylist_delete'),
]