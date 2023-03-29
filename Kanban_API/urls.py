from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Kanban.views import register_view, UserViewSet, login_View, TaskViewset, CategoryViewSet, ContactViewSet, SubTaskViewSet
from rest_framework.authtoken import views


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tasks', TaskViewset)
router.register(r'categorys', CategoryViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'subtasks', SubTaskViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('register/', register_view),
    path('login/', login_View.as_view()),
    path('contacts/<str:name>/', ContactViewSet.as_view({
        'get': 'retrieve',
        'PUT': 'update',
        'delete': 'destroy'
    }), name='contact-detail')
]
