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
from ..BL.ChildrenBL import ChildrenBL as cbl
from ..Models import *
import datetime
import random
import json
import jwt

class ChildApiController(APIView):
	@api_view(['POST'])
	def addChild(request):
		userid = request.data.get('userid')
		firstname = request.data.get('firstname')
		lastname = request.data.get('lastname')
		dateofbirth = request.data.get('dateofbirth')
		profilepic = request.data.get('profilepic')
		if (userid is None) or (firstname is None) or (lastname is None) or (dateofbirth is None) or (profilepic is None):
			raise exceptions.AuthenticationFailed('User id, First Name, Last Name, Date of Birth and Profile Picture is required')
		child = Child.Child()
		child.userid = userid
		child.firstname = firstname
		child.lastname = lastname
		child.dateofbirth = dateofbirth
		child.profilepic = profilepic

		child = cbl.addChild(child)

		if(child is None):
			raise exceptions.AuthenticationFailed('Child Not Added')

		return HttpResponse(Common.Common().ConverttoJson(child), content_type="application/json")

	@api_view(['GET'])
	def allChildren(request):
		userid = request.user.id
		if (userid is None):
			raise exceptions.AuthenticationFailed('userid is required')
		children = cbl.allChildren(userid)

		if(children is None):
			raise exceptions.AuthenticationFailed('Children Not Found')

		return HttpResponse(Common.Common().ConverttoJson(children), content_type="application/json")

	@api_view(['GET'])
	def selectChild(request):
		child_id = request.GET.get('childid')
		if (child_id is None):
			raise exceptions.AuthenticationFailed('childid parameter is required')
		child = cbl.selectAChild(child_id)

		if(child is None):
			raise exceptions.AuthenticationFailed('Child Not Found')

		return HttpResponse(Common.Common().ConverttoJson(child), content_type="application/json")