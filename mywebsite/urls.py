from django.contrib import admin
from django.urls import path, include
from mywebsite import views

urlpatterns = [
path('admin/', admin.site.urls),
path('', views.home,name='home_page'),
path('myapp/', include('myapp.urls')),
path('accounts/', include('myapp.urls'))

]
