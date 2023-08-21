from ..DAL.TransactionsDAL import TransactionsDAL as tsd
from ..Models.Transaction import Transaction
from ..Entities.Transactions import Transactions

class TransactionsBL():

	def allTransactions(ico):
		ats = tsd.allTransactions(ico)
		Trnsctns = list()
		for i in ats:
			Trnsctn = Transaction()
			Trnsctn.Id = i.id
			Trnsctn.userid = i.user_id
			Trnsctn.childid = i.child_id
			Trnsctn.tstitle = i.ts_title
			Trnsctn.tsamount = i.ts_amount
			Trnsctns.append(Trnsctn)
		return Trnsctns

	def addTransaction(ico):
		rto = tsd.addTransaction(ico)
		Trnsctn = Transaction()
		Trnsctn.Id = rto.id
		Trnsctn.userid = rto.user_id
		Trnsctn.childid = rto.child_id
		Trnsctn.tstitle = rto.ts_title
		Trnsctn.tsamount = rto.ts_amount
		return Trnsctn

	def selectChildTransactionsSum(userId, childId):
		rto = tsd.selectTransactionsSum(userId, childId)
		if(rto is None):
			return None
		return rto