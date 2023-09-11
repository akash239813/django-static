


from django.urls import path
from . import views


urlpatterns = [

    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('admission',views.admission,name='admission'),
    path('learning',views.learning,name='learning'),
    path('newsevents',views.newsevents,name='newsevents'),
    path('parents',views.parents,name='parents'),
   
]