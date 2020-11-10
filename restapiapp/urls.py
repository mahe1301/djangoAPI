from django.urls import path
from django.conf.urls import include
from . import views
# from django.contrib import admin



urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('test/', views.testwallet),
    
    path('init/', views.create_user),
    path('wallet', views.wallet_info),
    path('wallet/deposits', views.wallet_deposit),
    path('wallet/withdrawals', views.wallet_withdrawal)
]