from django import forms
from django.forms.utils import ErrorList

class FormMixin(object):

	def form_valid(self,form):
		if self.request.user.is_authenticated:
			form.instance.user = self.request.user
			return super(FormMixin,self).form_valid(form)
		else:
			form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue."])
			return self.form_invalid(form)

class OwnerMixin(object):

	def form_valid(self,form):

		if form.instance.user == self.request.user:
			return super(OwnerMixin,self).form_valid(form)
		else:
			form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["This User is not allowed to change this data."])
			return self.form_invalid(form)