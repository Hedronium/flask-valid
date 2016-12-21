import os
import sys
from flask import request,session
import re
import hashlib
import random

class Validator:
	def __init__(self,dictionary):
		self.requireError = False
		self.maxError 	  = False
		self.minError 	  = False
		self.emailError   = False
		self.integerError = False
		self.stringError  = False
		self.validate(dictionary)


	def validate(self,dictionary):
		if type(dictionary) is dict:
			for diction in dictionary:
				print(diction)
		else:	
			raise ValueError('Please pass a dicitonary')


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
		try:
			val = int(value)
			self.maxError = errorMessage

			if (val > max ):
				return self.maxError
			else:
				return ''

		except ValueError:
			print("it's not an integer")

	#set minimum value
	def min(self,value,min,errorMessage = ''):
		try:
			val = int(value)

			if errorMessage:
				self.minError = errorMessage

			if val < min:
				return self.minError
			else:
				return ''

		except ValueError:
			print("It's not an integer")

	#check for input that email or not
	def email(self,value,errorMessage = ''):
		value = re.group("\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")

		if errorMessage:
			self.emailError = errorMessage

		if value == "":
			return self.emailError
		else:
			return ''

	#check for integer value
	def integer(self,value,errorMessage =''):
		if errorMessage:
			self.integerError = errorMessage

		if type(value) is not int:
			return self.integerError
		else:
			return ''

	#check for string value
	def string(self,value,errorMessage = ''):
		if errorMessage:
			self.stringError = errorMessage

		if type(value) is not str:
			return self.stringError
		else:
			return ''

	#generate csrf token
	def csrftoken(self): 
		self.csrfdestroy()
		hashed_data = str(random.randrange(99999))
		hashed_data = hashlib.sha224(bytes(hashed_data, encoding='utf-8')).hexdigest()
		session['sdfshdfahlfgfdlhdfkjghakgjhdfkgjdfhgdfgnjgnf'] = hashed_data
		return hashed_data

	#get csrf value
	def getcsrf(self):
		data = session.get('sdfshdfahlfgfdlhdfkjghakgjhdfkgjdfhgdfgnjgnf')
		self.csrfdestroy()
		return data

	def csrffiled(self):
		return "<input type=\"hidden\" value=\""+ self.csrftoken() +"\""

	def csrfdestroy(self):
		return session['sdfshdfahlfgfdlhdfkjghakgjhdfkgjdfhgdfgnjgnf'] = ''

