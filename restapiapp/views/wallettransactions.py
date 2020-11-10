import hashlib
from rest_framework.response import Response
from rest_framework import  status
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import  IsAuthenticated,AllowAny
from django.db import transaction
from ..models import Wallet,WalletTransactions
from datetime import datetime


@api_view(['POST'])
@permission_classes([AllowAny , ])
def wallet_deposit(request):
    try:
        if 'amount' in request.data.keys() and 'reference_id' in request.data.keys() and int(request.data['amount']) > 0:
            with transaction.atomic():
                wallet_obj= Wallet.objects.get(owned_by_id=request.user.id)
                if wallet_obj.status == "disabled":
                    raise Exception("disabled wallet")
                wallet_trans_obj=WalletTransactions()
                wallet_trans_obj.transaction_by_id=request.user.id
                wallet_trans_obj.wallet_info_id = wallet_obj.id
                wallet_trans_obj.current_balance = wallet_obj.current_balance
                wallet_trans_obj.transaction_type = "deposit"
                wallet_trans_obj.transaction_amount = int(request.data['amount'])
                wallet_trans_obj.transaction_status = "success"
                wallet_trans_obj.reference_id = str(request.data['reference_id']) 
                wallet_trans_obj.save()
                trans_id = wallet_trans_obj.id
                wallet_trans_obj= WalletTransactions.objects.get(id=trans_id)
                trans_id = "bgdeposit"+ str(trans_id)
                wallet_obj.current_balance = wallet_obj.current_balance + wallet_trans_obj.transaction_amount
                wallet_obj.save()
                hash_object = hashlib.sha256(trans_id.encode('utf-8'))
                trans_id = list(hash_object.hexdigest()[0:32])
                trans_id.insert(8,"-")
                trans_id.insert(13,"-")
                trans_id.insert(18,"-")
                trans_id.insert(23,"-")
                trans_id = "".join(trans_id) 
                resp={
                        "status": "success",
                        "data": {
                                    "deposit": {
                                    "id": trans_id,
                                    "deposited_by": str(request.user),
                                    "status": wallet_trans_obj.transaction_status,
                                    "deposited_at": wallet_trans_obj.created,
                                    "amount": wallet_trans_obj.transaction_amount,
                                    "reference_id": wallet_trans_obj.reference_id
                                    }
                            }
                        }
                resp_status=status.HTTP_201_CREATED             
        else:
            raise Exception
    except Exception as e:
        print(e)
        resp={
            "status": "fail",
            "data": {
                "error": "Deposit Failed"
            }
         }
        resp_status=status.HTTP_400_BAD_REQUEST
    finally:
        return Response(resp ,status=resp_status)


@api_view(['POST'])
@permission_classes([AllowAny , ])
def wallet_withdrawal(request):
    try:
        if 'amount' in request.data.keys() and 'reference_id' in request.data.keys() and int(request.data['amount']) > 0:
            with transaction.atomic():
                wallet_obj= Wallet.objects.get(owned_by_id=request.user.id)
                if wallet_obj.status == "disabled" or int(request.data['amount']) > wallet_obj.current_balance:
                    raise Exception
                wallet_trans_obj=WalletTransactions()
                wallet_trans_obj.transaction_by_id=request.user.id
                wallet_trans_obj.wallet_info_id = wallet_obj.id
                wallet_trans_obj.current_balance = wallet_obj.current_balance
                wallet_trans_obj.transaction_type = "withdrawal"
                wallet_trans_obj.transaction_amount = int(request.data['amount'])
                wallet_trans_obj.transaction_status = "success"
                wallet_trans_obj.reference_id = str(request.data['reference_id']) 
                wallet_trans_obj.save()
                trans_id = wallet_trans_obj.id
                wallet_trans_obj= WalletTransactions.objects.get(id=trans_id)
                trans_id = "bgwithdrawal"+ str(trans_id)
                wallet_obj.current_balance = wallet_obj.current_balance - wallet_trans_obj.transaction_amount
                wallet_obj.save()
                hash_object = hashlib.sha256(trans_id.encode('utf-8'))
                trans_id = list(hash_object.hexdigest()[0:32])
                trans_id.insert(8,"-")
                trans_id.insert(13,"-")
                trans_id.insert(18,"-")
                trans_id.insert(23,"-")
                trans_id = "".join(trans_id) 
                resp={
                        "status": "success",
                        "data": {
                            "withdrawal": {
                            "id": trans_id,
                            "withdrawn_by": str(request.user),
                            "status":  wallet_trans_obj.transaction_status,
                            "withdrawn_at": wallet_trans_obj.created,
                            "amount": wallet_trans_obj.transaction_amount,
                            "reference_id": wallet_trans_obj.reference_id
                            }
                        }
                    }
                resp_status=status.HTTP_201_CREATED             
        else:
            raise Exception
    except Exception as e:
        print(e)
        resp={
            "status": "fail",
            "data": {
                "error": "Withdrawal Failed"
            }
         }
        resp_status=status.HTTP_400_BAD_REQUEST
    finally:
        return Response(resp ,status=resp_status)