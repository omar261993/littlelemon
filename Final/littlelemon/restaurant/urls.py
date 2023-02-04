from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('menu/',views.Menuitemview.as_view()),
    path('menu/<int:pk>',views.singlemenuitemview.as_view()),
]