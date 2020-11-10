from rest_framework.response import Response
from rest_framework import  status
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import AllowAny #, IsAuthenticated
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
        if 'customer_xid' in request.data.keys():
            user_obj=CustomAccount.objects.get(username=request.data['customer_xid'])
            resp["data"] = user_obj.tokens()
            resp["status"] = "success"
    except Exception as e:
        pass
    finally:
        return Response(resp, status=status.HTTP_200_OK)