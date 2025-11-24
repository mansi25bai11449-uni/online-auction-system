from django.urls import path
from . import views

app_name = 'auction'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create-item/', views.create_item, name='create_item'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('item/<int:item_id>/bid/', views.place_bid, name='place_bid'),
]