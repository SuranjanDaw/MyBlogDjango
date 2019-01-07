from django.urls import path
from . import views

urlpatterns = [
    path('post1',views.post_list,name='post_list'),
    path('post2/<int:pk>/',views.post_details,name='post_details')
]