from ..DAL.ChildrenDAL import ChildrenDAL as cd
from ..DAL.RewardTasksDAL import RewardTasksDAL as rtd
from ..DAL.TransactionsDAL import TransactionsDAL as tsd
from ..Models.Child import Child
from ..Models.RewardTask import RewardTask
from ..Entities.Children import Children
from ..Entities.RewardTasks import RewardTasks

class ChildrenBL():

	def allChildren(ico):
		acd = cd.allChildren(ico)
		Childrn = list()
		for i in acd:
			Chld = Child()
			Chld.Id = i.id
			Chld.firstname = i.first_name
			Chld.lastname = i.last_name
			Chld.dateofbirth = i.date_of_birth
			# Chld.profilepic = i.profile_pic
			Chld.sumoftransactions = tsd.selectTransactionsSum(ico, i.id)["ts_amount__sum"]
			Childrn.append(Chld)
		return Childrn

	def addChild(ico):
		rco = cd.addChild(ico)
		Chld = Child();
		Chld.Id = rco.id
		Chld.userid = rco.user_id
		Chld.firstname = rco.first_name
		Chld.lastname = rco.last_name
		Chld.dateofbirth = rco.date_of_birth
		Chld.profilepic = rco.profile_pic
		return Chld

	def selectAChild(ico):
		rco = cd.selectSingleChild(ico)
		if(rco is None):
			return None
		Chld = Child();
		Chld.Id = rco.id
		Chld.userid = rco.user_id
		Chld.firstname = rco.first_name
		Chld.lastname = rco.last_name
		Chld.dateofbirth = rco.date_of_birth
		Chld.profilepic = rco.profile_pic
		artd = rtd.allRewardTasks(rco.id)
		RewrdTasks = list()
		for i in artd:
			RewardTsk = RewardTask()
			RewardTsk.Id = i.id
			RewardTsk.rewardtasktitle = i.reward_task_title
			RewardTsk.rewardtaskamount = i.reward_task_amount
			RewrdTasks.append(RewardTsk)
		Chld.chorewitrewards = RewrdTasks
		return Chld