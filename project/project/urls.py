"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include 
from tickets import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register( 'guests',views.viewsets_guest)
router.register('Movie' , views.viewsets_Movie)
router.register('Reservation' , views.viewsets_Reserv)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('no_rest/', views.no_rest_module),
    path('from_mod/' , views.from_module),
    path('FBV_List/' , views.FBV_List),
    path('FBV_pk/<int:pk>' , views.FBV_pk),
    path('CBV_List/' , views.CBV_List.as_view()),
    path('CBV_pk/<int:pk>' , views.CBV_pk.as_view()) , 
    path('rest/mixins_LC/' , views.mixins_List.as_view()) , 
    path('rest/mixins_pk/<int:pk>' , views.mixins_pk.as_view()),
    path('rest/generics_LC/', views.gen_list.as_view() ), 
    path('rest/generics_pk/<int:pk>', views.gen_pk.as_view() ),
    #viewsets path 
    path('rest/viewsets/' , include(router.urls)),

    #8find movie 
    path('fbv/movie/' , views.find_movie),

]
