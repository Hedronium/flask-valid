import os
import sys
from flask import request
import re

class Validator:
	def __init__():
		self.requireError = False
		self.maxError 	  = False
		self.minError 	  = False
		self.emailError   = False
		self.integerError = False
		self.stringError  = False


	def validate(dictonary):
		if type(dictonary) not dict:
			raise ValueError('please pass dictionary')

		for dictionary in dictionary:
			print(dictionary)

	#check for required
	def require(self,value,errorMessage = ''):

		if errorMessage:
			self.requireError = errorMessage


		if value == "":
			return self.requireError
		else:
			return ''

	#set maximum value
	def max(self,value,max,errorMessage = ''):
		if 	type(max) not int:
			raise ValueError("max value is not an integer")

		val = int(value)
		self.maxError = errorMessage

		if (val > max ):
			return self.maxError
		else:
			return True

	#set minimum value
	def min(self,value,min,errorMessage = ''):
		
		if type(value) not int:
			raise ValueError('value is not an integer')

		val = int(value)

		if errorMessage:
			self.minError = errorMessage

		if val < min:
			return self.minError
		else:
			return True


	#check for input that email or not
	def email(self,value,errorMessage = ''):
		value = re.group("\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")

		if errorMessage:
			self.emailError = errorMessage

		if value == "":
			return self.emailError
		else:
			return True

	#check for integer value
	def integer(self,value,errorMessage =''):
		if errorMessage:
			self.integerError = errorMessage

		if type(value) not int:
			return self.integerError
		else:
			return True

	#check for string value
	def string(self,value,errorMessage = ''):
		if errorMessage:
			self.stringError = errorMessage

		if type(value) not str:
			return self.stringError
		else:
			return True

	def between(self,minvalue,maxvalue,errorMessage=''):
		if errorMessag:
			self.errorMessag = errorMessag

		if (type(minvalue) not int) or (type(maxvalue) not int):
			raise ValueError('Min value or max value must be integer')

