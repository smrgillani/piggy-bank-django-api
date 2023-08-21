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
from ..BL.RewardTasksBL import RewardTasksBL as rtbl
from ..Models import *
import datetime
import random
import json
import jwt

class RewardTaskApiController(APIView):
	@api_view(['POST'])
	@permission_classes((AllowAny,))
	def addRewardTask(request):
		childid = request.data.get('childid')
		title = request.data.get('title')
		amount = request.data.get('amount')
		if (childid is None) or (title is None) or (amount is None):
			raise exceptions.AuthenticationFailed('Child id, Title and Amount is required')
		rewardtask = RewardTask.RewardTask()
		rewardtask.childid = childid
		rewardtask.rewardtasktitle = title
		rewardtask.rewardtaskamount = amount

		rewardtasktask = rtbl.addRewardTask(rewardtask)

		if(rewardtasktask is None):
			raise exceptions.AuthenticationFailed('Reward Task Not Added')

		return HttpResponse(Common.Common().ConverttoJson(rewardtasktask), content_type="application/json")

	@api_view(['GET'])
	@permission_classes((AllowAny,))
	def allRewardTask(request):
		child_id = request.GET.get('childid')
		if (child_id is None):
			raise exceptions.AuthenticationFailed('childid is parameter is required')
		rewardtasks = rtbl.allRewardTasks(child_id)

		if(rewardtasks is None):
			raise exceptions.AuthenticationFailed('Reward Tasks Not Found')

		return HttpResponse(Common.Common().ConverttoJson(rewardtasks), content_type="application/json")

	@api_view(['GET'])
	def selectChild(request):
		child_id = request.GET.get('childid')
		if (child_id is None):
			raise exceptions.AuthenticationFailed('childid parameter is required')
		child = cbl.selectAChild(child_id)

		if(child is None):
			raise exceptions.AuthenticationFailed('Child Not Found')

		return HttpResponse(Common.Common().ConverttoJson(child), content_type="application/json")