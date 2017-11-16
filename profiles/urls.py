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
    url(r'^category/create/$', login_required(views.CategoryCreate.as_view()), name='category_create'),
    url(r'^category/update/(?P<pk>\d+)/$', login_required(views.CategoryUpdate.as_view()), name='category_update'),
    url(r'^category/delete/(?P<pk>\d+)/$', login_required(views.CategoryDelete.as_view()), name='category_delete'),
    url(r'^categorylist/create/(?P<pk>\d+)/$', login_required(views.categorylist_create), name='categorylist_create'),
    url(r'^categorylist/update/(?P<pk>\d+)/$', login_required(views.CategoryListUpdate.as_view()), name='categorylist_update'),
    url(r'^categorylist/delete/(?P<pk>\d+)/$', login_required(views.CategoryListDelete.as_view()), name='categorylist_delete'),
    url(r'^education/create/$', login_required(views.EducationCreate.as_view()), name='education_create'),
    url(r'^education/update/(?P<pk>\d+)/$', login_required(views.EducationUpdate.as_view()), name='education_update'),
    url(r'^education/delete/(?P<pk>\d+)/$', login_required(views.EducationDelete.as_view()), name='education_delete'),
    url(r'^work/create/$', login_required(views.WorkCreate.as_view()), name='work_create'),
    url(r'^work/update/(?P<pk>\d+)/$', login_required(views.WorkUpdate.as_view()), name='work_update'),
    url(r'^work/delete/(?P<pk>\d+)/$', login_required(views.WorkDelete.as_view()), name='work_delete'),
    url(r'^search/$', views.SearchListView.as_view(), name='search_list_view'),
    url(r'^approve/(?P<pk>\d+)/(?P<ck>\d+)/$', views.approve, name='approve'),
    url(r'^post_approve/(?P<pk>\d+)/$', views.post_approve, name='post_approve'),
    url(r'^post_delete/(?P<pk>\d+)/$', views.post_delete, name='post_delete'),
]