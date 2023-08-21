from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import exceptions
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponse, JsonResponse
from rest_framework.permissions import IsAuthenticated
from django.core.files.base import ContentFile
from ..Customs.jwtCustomOperations import generate_access_token, generate_refresh_token, verify_refresh_token
from django.core.mail import send_mail
from ..Customs.authentication import SafeJWTAuthentication
from ..BL.TransactionsBL import TransactionsBL as tsbl
from ..Models import *
import datetime
import random
import json
import jwt

class TransactionApiController(APIView):
	@api_view(['POST'])
	def addTransaction(request):
		userid = request.user.id
		childid = request.data.get('childid')
		title = request.data.get('title')
		amount = request.data.get('amount')
		if (userid is None) or (childid is None) or (title is None) or (amount is None):
			raise exceptions.AuthenticationFailed('User id, Child Id, Transaction Title and Amount is required')
		trnsctn = Transaction.Transaction()
		trnsctn.userid = userid
		trnsctn.childid = childid
		trnsctn.tstitle = title
		trnsctn.tsamount = amount

		trnsctn = tsbl.addTransaction(trnsctn)

		if(trnsctn is None):
			raise exceptions.AuthenticationFailed('Transaction Not Added')

		return HttpResponse(Common.Common().ConverttoJson(trnsctn), content_type="application/json")

	@api_view(['GET'])
	def allTransactions(request):
		userid = request.user.id
		if (userid is None):
			raise exceptions.AuthenticationFailed('userid is required')
		transactions = tsbl.allTransactions(userid)

		if(transactions is None):
			raise exceptions.AuthenticationFailed('Transactions Not Found')

		return HttpResponse(Common.Common().ConverttoJson(transactions), content_type="application/json")

	@api_view(['POST'])
	def selectChildTotalSumofTrans(request):
		userid = request.user.id
		childid = request.data.get('childid')
		if (userid is None) or (childid is None):
			raise exceptions.AuthenticationFailed('User Id and Child Id parameter is required')
		trnsctn = tsbl.selectChildTransactionsSum(userid, childid)

		if(trnsctn is None):
			raise exceptions.AuthenticationFailed('Transactions of Child Not Found')

		return HttpResponse(Common.Common().ConverttoJson(trnsctn), content_type="application/json")