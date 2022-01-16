from django.core.exceptions import ObjectDoesNotExist
# from django.contrib.auth.models import User

from rest_framework import status
# from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_auth.registration.views import RegisterView

from .models import Customer
from .serializers import CustomerSerializer

# Create your views here.


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class CustomRegisterView(RegisterView):

    def get_response_data(self, user):
        return {'message': 'user registration success'}


class CustomerCreate(APIView):
    """
    Create a new customer
    """
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        data = request.data
        data['owner'] = request.user.id
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success",
                             "message": "new customer record created"
                             }, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "failure",
                             "message": serializer.errors
                             }, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetail(APIView):
    """
    Get detail of a specific customer
    """
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        data = request.data
        if data:
            try:
                customer = Customer.objects.get(id=kwargs['pk'])
                serializer = CustomerSerializer(customer)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response({"status": "failure",
                                 "message": "entered email does not exist"
                                 }, status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response({"status": "failure",
                                 "message": "you do not have permissions to perform this action"
                                 }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"status": "failure",
                             "message": "please enter a valid data"
                             }, status=status.HTTP_400_BAD_REQUEST)


class CustomerList(APIView):
    """
    List all the customers of a user
    """
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        logged_user_id = request.user.id
        customers = Customer.objects.filter(owner=logged_user_id)
        for customer in customers:
            if logged_user_id == customer.owner.id:
                customer = Customer.objects.filter(owner=logged_user_id)
                serializer = CustomerSerializer(customer, many=True)
                return Response(serializer.data)
            else:
                return Response({"status": "failure",
                                 "message": "you do not have permissions to perform this action"
                                 }, status=status.HTTP_400_BAD_REQUEST)


class CustomerUpdate(APIView):
    """
    Update a customer record by a user
    """
    permission_classes = [IsAuthenticatedOrReadOnly]

    def put(self, request, *args, **kwargs):
        data = request.data
        customer = Customer.objects.get(id=kwargs['pk'])
        if request.user.id == customer.owner.id:
            data['owner'] = request.user.id
            serializer = CustomerSerializer(customer, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success",
                                 "message": "customer record updated"})
            return Response({"status": "failure",
                             "message": serializer.errors
                             }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"status": "failure",
                             "message": "you do not have permissions to perform this action"
                             }, status=status.HTTP_400_BAD_REQUEST)


class CustomerDelete(APIView):
    """
    Delete a customer record by a user
    """
    permission_classes = [IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        try:
            customer = Customer.objects.get(id=kwargs['pk'])
            if request.user.id == customer.owner.id:
                customer.delete()
                return Response({"status": "customer record deleted"
                                 }, status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response({"status": "record does not exist"
                             }, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"status": "failure",
                             "message": "you do not have permissions to perform this action"
                             }, status=status.HTTP_400_BAD_REQUEST)
