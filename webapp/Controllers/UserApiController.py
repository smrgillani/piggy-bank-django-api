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
from ..BL.UsersBL import UsersBL as ubl
from ..Models import *
import datetime
import random
import json
import jwt

class UserApiController(APIView):
	@api_view(['POST'])
	@permission_classes((AllowAny,))
	def userLogin(request):
		username = request.data.get('username')
		password = request.data.get('password')
		if (username is None) or (password is None):
			raise exceptions.AuthenticationFailed('username and password required')
		user = authenticate(request, username=username, password=password)

		if(user is None):
			raise exceptions.AuthenticationFailed('user not found')

		if (not user.check_password(password)):
			raise exceptions.AuthenticationFailed('wrong password')

		response= {
			'access_token': generate_access_token(user),
			'refresh_token': generate_refresh_token(user),
			'user_id': user.id,
		}

		return HttpResponse(Common.Common().ConverttoJson(response), content_type="application/json")

	@api_view(['POST'])
	@permission_classes((AllowAny,))
	def userSignup(request):
		firstname = request.data.get('firstname')
		lastname = request.data.get('lastname')
		username = request.data.get('username')
		password = request.data.get('password')
		if (firstname is None) or (lastname is None) or (username is None) or (password is None):
			raise exceptions.AuthenticationFailed('First Name, Last Name, Username and Password is required')
		udo = User.User()
		udo.username = username

		if(ubl.selectUserbyUsername(udo) is None):
			udo.firstname = firstname
			udo.lastname = lastname
			udo.password = password
			udo = ubl.addUser(udo)
		else:
			raise exceptions.AuthenticationFailed('User Already Exists with the same Username Or Email !')

		user = authenticate(request, username=username, password=password)

		if(user is None):
			raise exceptions.AuthenticationFailed('user not found')

		if (not user.check_password(password)):
			raise exceptions.AuthenticationFailed('wrong password')

		send_mail( 'Subject here', 'Here is the message.', 'piggybank@effinit.com', [username], fail_silently=False, )
		response= {
			'access_token': generate_access_token(user),
			'refresh_token': generate_refresh_token(user),
			'user_id': user.id,
		}

		return HttpResponse(Common.Common().ConverttoJson(response), content_type="application/json")

	@api_view(['POST'])
	@permission_classes((AllowAny,))
	def genUserFPCode(request):
		username = request.data.get('username')
		if (username is None):
			raise exceptions.AuthenticationFailed('Username is required')
		udo = User.User()
		udo.username = username

		udo = ubl.selectUserbyUsername(udo)


		if(udo is not None):
			user_fp_code = random.randint(0,9999999)
			udo.fp_code = user_fp_code
			udo = ubl.updateForgetPasswordCode(udo)
			send_mail( 'Reset Password Piggy Bank', 'Your password reset code is ' + str(user_fp_code), 'piggybank@effinit.com', [username], fail_silently=False, )
		else:
			raise exceptions.AuthenticationFailed('user not found')
		
		response= {
			'user_email': udo,
		}

		return HttpResponse(Common.Common().ConverttoJson(udo), content_type="application/json")

	@api_view(['POST'])
	@permission_classes((AllowAny,))
	def verifyUserFPCode(request):
		username = request.data.get('username')
		fpcode = request.data.get('code')
		if (username is None) or (fpcode is None):
			raise exceptions.AuthenticationFailed('Username and code is required')
		udo = User.User()
		udo.username = username
		udo.fp_code = fpcode

		udo = ubl.selectUserbyUsernameFrgtPswdCode(udo)

		if(udo is None):
			udo = False
		else:
			udo = True
		
		response= {
			'code_verification_status': udo,
		}

		return HttpResponse(Common.Common().ConverttoJson(response), content_type="application/json")

	@api_view(['POST'])
	@permission_classes((AllowAny,))
	def updateUserForgetPassword(request):
		username = request.data.get('username')
		password = request.data.get('password')
		fpcode = request.data.get('code')
		if (username is None) or (password is None) or (fpcode is None):
			raise exceptions.AuthenticationFailed('Username, Password and code is required')
		udo = User.User()
		udo.username = username
		udo.password = password
		udo.fp_code = fpcode

		udo = ubl.updateUserPassword(udo)

		if(udo is None):
			udo = False
		else:
			udo = True
		
		response= {
			'password_update_status': udo,
		}

		return HttpResponse(Common.Common().ConverttoJson(response), content_type="application/json")

	@api_view(['POST'])
	def changeUserPassword(request):
		username = request.data.get('username')
		oldpassword = request.data.get('oldpassword')
		newpassword = request.data.get('newpassword')
		if (username is None) or (oldpassword is None) or (newpassword is None):
			raise exceptions.AuthenticationFailed('Username, Old Password and New Password is required')
		
		user = authenticate(request, username=username, password=oldpassword)

		if(user is None):
			raise exceptions.AuthenticationFailed('User not found')

		udo = User.User()
		udo.username = username
		udo.password = newpassword

		udo = ubl.changeUserPassword(udo)

		if(udo is None):
			udo = False
		else:
			udo = True
		
		response= {
			'password_change_status': udo,
		}

		return HttpResponse(Common.Common().ConverttoJson(response), content_type="application/json")

	@api_view(['GET'])
	def selectUser(request):
		udo = ubl.selectUserbyId(request.user.id)

		return HttpResponse(Common.Common().ConverttoJson(udo), content_type="application/json")