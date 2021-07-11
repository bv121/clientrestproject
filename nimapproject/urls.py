 
from django.contrib import admin
from django.urls import path,include
from apiapp import views
from rest_framework import routers
from clientapp.views import ClientList,ClientDetail,ProjectList,ProjectDetail

router = routers.DefaultRouter()
router.register(r'users',views.UserViewSet)
router.register(r'group',views.GroupViewSet)
#router.register(r'client', ClientViewSet)



urlpatterns = [
    path('admin',admin.site.urls),
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(('clientapp.urls', 'clientapp'), namespace="api")),
]