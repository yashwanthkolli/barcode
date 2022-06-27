from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('get/<str:id>',views.get_info),
    path('__debug__/', include('debug_toolbar.urls'))
]