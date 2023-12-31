from django.contrib.auth import authenticate, login

from ..DAL.UsersDAL import UsersDAL as ud
from ..Models.User import User
from ..Entities.Users import Users

class UsersBL():

	def allUsers():
		au = ud.allUsers()
		Users = list()
		for i in au:
			usr = User()
			usr.contact_id = i.contact_id
			usr.username = i.username
			usr.emailAddr = i.emailAddr
			Users.append(usr)
		return Users

	def addUser(ico):
		ruo = ud.addUser(ico)
		Usr = User();
		Usr.username = ruo.username
		return Usr

	def latestUser():
		ruo = ud.getLatestUser()
		Usr = User();
		Cntct = Contact();
		Cntct.Id = ruo.contact_id
		Usr.contact = cbl.selectContact(Cntct)
		Usr.Id = ruo.unq_id
		Usr.username = ruo.username
		Usr.emailAddr = ruo.emailAddr
		return Usr

	def selectUserbyUsername(ico):
		ruo = ud.selectUserbyUsername(ico)
		if(ruo is None):
			return None
		Usr = User();
		Usr.username = ruo.username
		return Usr

	def selectUserbyId(ico):
		ruo = ud.selectUserbyId(ico)
		if(ruo is None):
			return None
		Usr = User();
		Usr.Id = ruo.id
		Usr.firstname = ruo.first_name
		Usr.lastname = ruo.last_name
		Usr.username = ruo.username
		return Usr

	def selectUserbyUsernameFrgtPswdCode(ico):
		ruo = ud.selectUserbyUsernameFPC(ico)
		if(ruo is None):
			return None
		Usr = User();
		Usr.username = ruo.username
		return Usr

	def updateForgetPasswordCode(ico):
		ruo = ud.updateFPCode(ico)
		if(ruo is None):
			return None
		Usr = User();
		Usr.username = ruo.username
		return Usr

	def updateUserPassword(ico):
		ruo = ud.updatePassword(ico)
		if(ruo is None):
			return None
		Usr = User();
		Usr.username = ruo.username
		return Usr

	def changeUserPassword(ico):
		ruo = ud.changePassword(ico)
		if(ruo is None):
			return None
		Usr = User();
		Usr.username = ruo.username
		return Usr