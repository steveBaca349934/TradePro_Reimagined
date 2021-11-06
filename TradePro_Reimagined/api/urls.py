from django.urls import path, include
from django.contrib import admin
from .views import RoomView

urlpatterns = [
    #path('admin/',admin.site.urls),
    #path('api',include('api.urls')),
    path('room/', include('frontend.urls'))
    #path('/room/', RoomView)
    

]
