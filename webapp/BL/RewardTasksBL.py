from ..DAL.RewardTasksDAL import RewardTasksDAL as rtd
from ..Models.RewardTask import RewardTask
from ..Entities.RewardTasks import RewardTasks

class RewardTasksBL():

	def allRewardTasks(ico):
		artd = rtd.allRewardTasks(ico)
		RewrdTasks = list()
		for i in artd:
			RewardTsk = RewardTask()
			RewardTsk.Id = i.id
			RewardTsk.rewardtasktitle = i.reward_task_title
			RewardTsk.rewardtaskamount = i.reward_task_amount
			RewrdTasks.append(RewardTsk)
		return RewrdTasks

	def addRewardTask(ico):
		rrto = rtd.addRewardTask(ico)
		RewardTsk = RewardTask();
		RewardTsk.Id = rrto.id
		RewardTsk.rewardtasktitle = rrto.reward_task_title
		RewardTsk.rewardtaskamount = rrto.reward_task_amount
		return RewardTsk

	def selectARewardTask(ico):
		rrto = rtd.selectSingleRewardTask(ico)
		if(rrto is None):
			return None
		RewardTsk = RewardTask();
		RewardTsk.Id = rrto.id
		RewardTsk.rewardtasktitle = rrto.reward_task_title
		RewardTsk.rewardtaskamount = rrto.reward_task_amount
		return RewardTsk