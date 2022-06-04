from django.urls import path
from . import views


urlpatterns =[
    path('',views.index_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view,name='signup'),
    path('home/', views.home_view, name='home'),
    path('logout/' , views.logOutUser, name='logout'),
    path('head/', views.head_view, name='head'),
    path('subhead/', views.subhead_view, name='subhead'),
    path('volunteer/', views.volunteer_view, name='vol'),
    path('payments/<str:pk_d>', views.donor_payment_form_view, name='donor_payment_form'),
    path('admin/', views.admin_view, name='super'),
    path('delete_donor/<str:pk>', views.delete_donor, name='delete_donor'),
    path('create_donor/', views.create_donor_view, name='create_donor'),

]