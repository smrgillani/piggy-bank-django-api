from ..Entities.Transactions import Transactions as ts
from .Commons import Commons as c
import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.db.models import Sum

class TransactionsDAL:

	def allTransactions(ico):
		return ts.objects.all().filter(user_id=ico)

	def getLatestTransaction():
		uo = None
		try:
			uo = ts.objects.latest('u_id')
		except ObjectDoesNotExist:
		 	uo = None
		return uo

	def selectTransactionsSum(userId, childId):
		cco = None
		try:
			cco = ts.objects.filter(user_id=userId, child_id=childId).aggregate(Sum('ts_amount'))
		except ObjectDoesNotExist:
		 	cco = None
		return cco

	def addTransaction(ico):
		return ts.objects.create(user_id=ico.userid, child_id=ico.childid, ts_title=ico.tstitle, ts_amount=ico.tsamount)
