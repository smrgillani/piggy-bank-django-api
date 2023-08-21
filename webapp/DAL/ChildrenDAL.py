from ..Entities.Children import Children as cd
from .Commons import Commons as c
import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

class ChildrenDAL:

	def allChildren(ico):
		return cd.objects.all().filter(user_id=ico)

	def getLatestChildren():
		uo = None
		try:
			uo = cd.objects.latest('u_id')
		except ObjectDoesNotExist:
		 	uo = None
		return uo

	def selectSingleChild(ico):
		cco = None
		try:
			cco = cd.objects.get(id=ico)
		except ObjectDoesNotExist:
		 	cco = None
		return cco

	def addChild(ico):
		return cd.objects.create(user_id=ico.userid, first_name=ico.firstname, last_name=ico.lastname, date_of_birth=ico.dateofbirth, profile_pic = ico.profilepic)
