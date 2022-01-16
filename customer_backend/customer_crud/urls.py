from django.urls import path
# from .views import UserList, UserDetail
from .views import CustomerCreate, \
                   CustomerDetail, CustomerUpdate, \
                   CustomerList, CustomerDelete

app_name = "customer_crud"

urlpatterns = [
    # path('users/', UserList.as_view(), name="user_list"),
    # path('users/<int:pk>/', UserDetail.as_view(), name="user_detail"),
    path('customer/create',
         CustomerCreate.as_view(), name="customer_create"),
    path('customer/detail/<int:pk>',
         CustomerDetail.as_view(), name="customer_detail"),
    path('customer/list',
         CustomerList.as_view(), name="customer_list"),
    path('customer/update/<int:pk>',
         CustomerUpdate.as_view(), name="customer_update"),
    path('customer/delete/<int:pk>',
         CustomerDelete.as_view(), name="customer_delete"),
]
