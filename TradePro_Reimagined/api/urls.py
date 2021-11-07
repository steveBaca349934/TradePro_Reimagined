from django.urls import path, include
from django.contrib import admin
from .views import RoomView, CreateRoomView

urlpatterns = [
    #path('admin/',admin.site.urls),
    #path('api',include('api.urls')),
    path('', include('frontend.urls')),
    path('create-room', CreateRoomView.as_view())
    #path('/room/', RoomView)
    

]
