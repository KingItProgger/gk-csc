from django.urls import path
from .views import *
urlpatterns=[
    path('',FlatsList.as_view(),name='flats_list'),
    path('recall',RecallView.as_view()),
    path('1-room',Flats_1_List.as_view(),name='1_room_flats'),
    path('2-room',Flats_2_List.as_view(),name='2_room_flats'),
    path('3-room',Flats_3_List.as_view(),name='3_room_flats'),



    path('news/',NewsList.as_view(),name='news'),

    path('news/<int:pk>',NewsDetail.as_view()),
    path('about',about,name='about'),
    path('contacts',contacts,name='contacts'),
    path('sales',sales,name='sales'),
    path('building_plan',building_plan,name='building_plan'),
    path('credit_0',credit_0,name='credit_0'),
    path('price_list',price_list,name='price_list'),

    path('responses',ReviewCreate.as_view(),name='reviews'),
    path('faq',faq,name='faq'),
    path('credit_issues',credit_issues,name='credit_issues'),
    path('pay_ways',pay_ways,name='pay_ways'),
    path('reverse_call',reverse_call,name='reverse_call'),
    path('law_inform',law_inform,name='law_inform'),
    path('docs',docs,name='docs'),

]