from ..DAL.SchoolsDAL import SchoolsDAL as sc
from ..Models.School import School
from ..Entities.Schools import Schools

class SchoolsBL():

	def allSchools():
		act = sc.allSchools()
		Schls = list()
		for i in act:
			schl = School()
			schl.logo = i.logo
			schl.name = i.name
			schl.number = i.number
			schl.location = i.location
			schl.address = i.address
			schl.phone_number = i.phone_number
			schl.email = i.email
			schl.number_of_students = i.number_of_students
			schl.rp_name = i.rp_name
			schl.rp_signature = i.rp_signature
			schl.rp_signature_file = i.rp_signature_file
			schl.rp_signature_date = i.rp_signature_date
			schl.principal_name = i.principal_name
			schl.principal_signature = i.principal_signature
			schl.principal_signature_file = i.principal_signature_file
			schl.principal_signature_date = i.principal_signature_date
			Schls.append(schl)
		return Schls

	def addSchool(ico):
		schls = Schools()
		schls.logo = ico.logo
		schls.name = ico.name
		schls.number = ico.number
		schls.location = ico.location
		schls.address = ico.address
		schls.phone_number = ico.phone_number
		schls.email = ico.email
		schls.number_of_students = ico.number_of_students
		schls.rp_name = ico.rp_name
		schls.rp_signature = ico.rp_signature
		schls.rp_signature_file = ico.rp_signature_file
		schls.rp_signature_date = ico.rp_signature_date
		schls.principal_name = ico.principal_name
		schls.principal_signature = ico.principal_signature
		schls.principal_signature_file = ico.principal_signature_file
		schls.principal_signature_date = ico.principal_signature_date
		rcto = sc.addSchool(schls)
		if rcto is None:
			return None
		schl = School()
		schl = ico
		schl.Id = rcto.id
		return schl