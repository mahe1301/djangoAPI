from rest_framework.response import Response
from rest_framework import  status
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import AllowAny
from ..models import CustomAccount


@api_view(['POST'])
@permission_classes([AllowAny, ])
def create_user(request):
    try:
        resp={
                "data": {
                    "error": {
                    "customer_xid": [
                        "Missing data for required field."
                    ]
                    }
                },
                "status": "fail"
            }
        if 'customer_xid' in request.data.keys() and len(request.data['customer_xid']) > 0:
            user_obj=CustomAccount.objects.filter(username=request.data['customer_xid'])
            if len(user_obj) == 0:
                user_obj=CustomAccount.objects.create_user(username=request.data['customer_xid'],password=request.data['customer_xid'])
            else:
                user_obj=user_obj[0]
            resp["data"] = user_obj.tokens()
            resp["status"] = "success"
            resp_status=status.HTTP_201_CREATED
        else:
            raise Exception
    except Exception as e:
        resp_status=status.HTTP_400_BAD_REQUEST
    finally:
        return Response(resp, status=resp_status)