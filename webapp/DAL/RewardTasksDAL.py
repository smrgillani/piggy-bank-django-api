from ..Entities.RewardTasks import RewardTasks as rt
from .Commons import Commons as c
import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

class RewardTasksDAL:

	def allRewardTasks(ico):
		return rt.objects.all().filter(child_id=ico)

	def selectSingleRewardTask(ico):
		so = None
		try:
			so = rt.objects.get(id=ico)
		except ObjectDoesNotExist:
		 	so = None
		return so

	def addRewardTask(ico):
		return rt.objects.create(child_id=ico.childid, reward_task_title=ico.rewardtasktitle, reward_task_amount=ico.rewardtaskamount)
