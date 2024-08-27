from django.contrib import admin
from django.urls import path, include
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.userAddShow, name='addandshow'),
    path('', views.UserAddShow.as_view(), name='addandshow'),
    path('delete/<int:id>/', views.deleteuser, name='deletedata'),
    path('update/<int:id>/', views.UserUpdateView.as_view(), name='updatedata'),
    path('api/',include('enroll.api.urls')),
    
]