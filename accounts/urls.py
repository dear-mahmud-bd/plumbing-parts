from django.urls import path
from .views import *


urlpatterns = [
    path('register/', register, name='register_page'),
    path('login/', login, name='login_page'),
    # path('dashboard/', dashboard, name='dashboard_page'),
    path('logout/', logout, name='logout'),
    path('', dashboard, name='dashboard_page'),

    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('forgotPassword/', forgotPassword, name='forgotPassword_page'),
    path('reset_password_validate/<uidb64>/<token>/', reset_password_validate, name='reset_password_validate'),
    path('resetPassword/', resetPassword, name='resetPassword_page'),

    path('my_orders/', my_orders, name='my_orders'),
    path('order_detail/<int:order_id>/', order_detail, name='order_detail'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('change_password/', change_password, name='change_password'),
]
