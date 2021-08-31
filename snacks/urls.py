from django.urls import path
# from django.urls.resolvers import URLPattern
from .views import Snackslistview,Snacksdetailview

urlpatterns=[
    path('',Snackslistview.as_view(),name='snacks_list'),
    path('<int:pk>/',Snacksdetailview.as_view(),name='snacks_detail')

]