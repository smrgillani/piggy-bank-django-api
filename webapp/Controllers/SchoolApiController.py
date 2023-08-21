from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import FormParser,MultiPartParser
from django.http import HttpResponse, JsonResponse
from rest_framework.permissions import IsAuthenticated
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.core.files.storage import FileSystemStorage

import base64
from django.core.files.base import ContentFile

from ..BL.SchoolsBL import SchoolsBL as scbl
from ..Models import *
import datetime
import json
class SchoolApiController(APIView):
	# parser_class = (MultiPartParser,)
	# @permission_classes([IsAuthenticated])
	# permission_classes = (IsAuthenticated)
	# authentication_classes = (JSONWebTokenAuthentication,)

	@api_view(['GET'])
	def allSchools(request, format=None):
		data = scbl.allSchools()

		return HttpResponse(Common.Common().ConverttoJson(data), content_type="application/json")

	@api_view(['POST'])
	def addSchool(request, format=None):
		ud = json.loads(request.body)
		schl = School.School()
		# print(ud["s_logo"])

		image_data = ud["s_logo"]
		formatExt, imgstr = image_data.split(';base64,')
		ext = formatExt.split('/')[-1]
		data = ContentFile(base64.b64decode(imgstr))
		
		folder='media/images/'
		fs = FileSystemStorage(location=folder)
		fullFileName = datetime.datetime.now().strftime("%Y-%d-%m-%H-%M-%S-%f") + "." + ext
		filename = fs.save(fullFileName, data)

		schl.logo = fullFileName

		image_data = ud["s_mngmnt_prsn_sgntr"]
		formatExt, imgstr = image_data.split(';base64,')
		ext = formatExt.split('/')[-1]
		data = ContentFile(base64.b64decode(imgstr))
		
		folder='media/images/'
		fs = FileSystemStorage(location=folder)
		fullFileName = datetime.datetime.now().strftime("%Y-%d-%m-%H-%M-%S-%f") + "." + ext
		filename = fs.save(fullFileName, data)

		schl.rp_signature = fullFileName

		image_data = ud["s_prncpl_sgntr"]
		formatExt, imgstr = image_data.split(';base64,')
		ext = formatExt.split('/')[-1]
		data = ContentFile(base64.b64decode(imgstr))
		
		folder='media/images/'
		fs = FileSystemStorage(location=folder)
		fullFileName = datetime.datetime.now().strftime("%Y-%d-%m-%H-%M-%S-%f") + "." + ext
		filename = fs.save(fullFileName, data)

		schl.principal_signature = fullFileName
		
		schl.name = ud["s_name"]
		schl.number = ud["s_number"]
		schl.location = ud["s_location"]
		schl.address = ud["s_address"]
		schl.phone_number = ud["s_phone_number"]
		schl.email = ud["s_email"]
		schl.number_of_students = ud["s_num_of_stdnt"]
		schl.rp_name = ud["s_mngmnt_prsn_name"]
		schl.rp_signature_date = ud["s_mngmnt_prsn_sgntr_date"]
		schl.principal_name = ud["s_prncpl_name"]
		schl.principal_signature_date = ud["s_prncpl_sgntr_date"]
		data = scbl.addSchool(schl)
		#data = scbl.allSchools()
		
		return HttpResponse(Common.Common().ConverttoJson(data), content_type="application/json")