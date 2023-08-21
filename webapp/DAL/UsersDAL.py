from ..Entities.Users import Users as u
from .Commons import Commons as c
import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.contrib.auth.hashers import make_password

class UsersDAL:
	def allUsers():
		return u.objects.all()
	def getLatestUser():
		uo = None
		try:
			uo = u.objects.latest('u_id')
		except ObjectDoesNotExist:
		 	uo = None
		return uo
	def addUser(ico):
		return u.objects.create(first_name=ico.firstname, last_name=ico.lastname, username=ico.username, password = make_password(ico.password), profile_pic='1', is_active=1, is_superuser=0, is_staff=0)
	def updateFPCode(ico):
		qrr = u.objects.filter(username=ico.username).update(fp_code=ico.fp_code)
		return (None, u.objects.get(username=ico.username)) [qrr != 0]
	def updateToken(ico):
		qrr = u.objects.filter(unq_id=ico.Id).update(auth_token=ico.auth_token, token_expiry=ico.token_expiry)
		return (None, u.objects.get(unq_id=ico.Id)) [qrr != 0]
	def updatePassword(ico):
		qrr = u.objects.filter(username=ico.username, fp_code=ico.fp_code).update(password = make_password(ico.password), fp_code='')
		return (None, u.objects.get(username=ico.username)) [qrr != 0]
	def changePassword(ico):
		qrr = u.objects.filter(username=ico.username).update(password = make_password(ico.password))
		return (None, u.objects.get(username=ico.username)) [qrr != 0]
	def selectUserbyUsername(ico):
		try:
			return u.objects.filter(username=ico.username)[0]
		except IndexError:
			return None
	def selectUserbyUsernameFPC(ico):
		try:
			return u.objects.filter(username=ico.username, fp_code=ico.fp_code)[0]
		except IndexError:
			return None

	def selectUserbyId(ico):
		cco = None
		try:
			cco = u.objects.get(id=ico)
		except ObjectDoesNotExist:
		 	cco = None
		return cco