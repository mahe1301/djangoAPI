import hashlib
from rest_framework.response import Response
from rest_framework import  status
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import  IsAuthenticated
from ..models import Wallet
from datetime import datetime


@api_view(['GET', 'POST', 'PATCH'])
@permission_classes([IsAuthenticated , ])
def wallet_info(request):
    hash_object = hashlib.sha256(str(request.user.id).encode('utf-8'))
    uid = list(hash_object.hexdigest()[0:32])
    uid.insert(8,"-")
    uid.insert(13,"-")
    uid.insert(18,"-")
    uid.insert(23,"-")
    uid = "".join(uid) 
    
    resp={
            "status": "fail",
            "data": {
                "error": "Already enabled"
            }
         }
    resp_status=None
    
    if request.method == 'GET': # View my wallet balance
        try:
            wallet_obj= Wallet.objects.get(owned_by_id=request.user.id)
            if wallet_obj.status == "disabled":
                raise Exception
            data= {
                        "wallet": {
                        "id": uid,
                        "owned_by": str(request.user),
                        "status": wallet_obj.status,
                        "enabled_at": wallet_obj.enabled_at,
                        "balance": wallet_obj.current_balance
                        }
                 }
            resp["status"]="success"
            resp["data"]=data
            resp_status=status.HTTP_200_OK
        except Exception as e:
            resp["status"]="fail"
            resp["data"]={ "error": "Disabled"}
            resp_status=status.HTTP_404_NOT_FOUND
    elif request.method == 'POST':  #Enable my wallet
        try:
            wallet_obj= Wallet.objects.filter(owned_by_id=request.user.id)
            if len(wallet_obj) == 0:
                wallet_obj=Wallet()
                wallet_obj.owned_by_id=request.user.id
                wallet_obj.current_balance=0
            else:
                wallet_obj=wallet_obj[0]
            wallet_obj.status="enabled"
            wallet_obj.enabled_at=datetime.now()
            wallet_obj.save()
            data= {
                        "wallet": {
                        "id": uid,
                        "owned_by": str(request.user),
                        "status": "enabled",
                        "enabled_at": wallet_obj.enabled_at,
                        "balance": wallet_obj.current_balance
                        }
                 }
            resp["status"]="success"
            resp["data"]=data
            resp_status=status.HTTP_201_CREATED
        except Exception as e:
            resp["status"]="fail"
            resp["data"]={ "error": "Already enabled"}
            resp_status=status.HTTP_400_BAD_REQUEST
       
    elif request.method == 'PATCH':
        try:
            if 'is_disabled' in request.data.keys() and request.data['is_disabled'] =="true":
                wallet_obj= Wallet.objects.get(owned_by_id=request.user.id)
                wallet_obj.status="disabled"
                wallet_obj.disabled_at=datetime.now()
                wallet_obj.save()
                data= {
                            "wallet": {
                            "id": uid,
                            "owned_by": str(request.user),
                            "status": wallet_obj.status,
                            "disabled_at": wallet_obj.disabled_at,
                            "balance": wallet_obj.current_balance
                            }
                    }
                resp["status"]="success"
                resp["data"]=data
                resp_status=status.HTTP_200_OK
            else:
                raise Exception
        except Exception as e:
            resp["status"]="fail"
            resp["data"]={ "error": "Enabled"}
            resp_status=status.HTTP_400_BAD_REQUEST
    return Response(resp, status=resp_status)
 
