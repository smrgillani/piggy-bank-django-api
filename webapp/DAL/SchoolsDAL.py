from ..Entities.Schools import Schools as schl
from .Commons import Commons as c
import datetime
from django.core.exceptions import ObjectDoesNotExist

class SchoolsDAL:
	def allSchools():
		return schl.objects.filter().all()
	def addSchool(ico):
		# return schl.objects.create(logo=ico.logo, name=ico.name, number=ico.number, location=ico.location, address=ico.address, phone_number=ico.phone_number, email=ico.email, number_of_students=ico.number_of_students, rp_name=ico.rp_name, rp_signature=ico.rp_signature, rp_signature_file=ico.rp_signature_file, principal_name=ico.principal_name, principal_signature=ico.principal_signature, principal_signature_file=ico.principal_signature_file)
		return schl.objects.create(logo=ico.logo, name=ico.name, number=ico.number, location=ico.location, address=ico.address, phone_number=ico.phone_number, email=ico.email, number_of_students=ico.number_of_students, rp_name=ico.rp_name, rp_signature=ico.rp_signature, rp_signature_file=ico.rp_signature_file, rp_signature_date=ico.rp_signature_date, principal_name=ico.principal_name, principal_signature=ico.principal_signature, principal_signature_file=ico.principal_signature_file, principal_signature_date=ico.principal_signature_date)