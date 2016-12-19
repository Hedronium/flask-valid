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

		if type(value) not int:
			return self.integerError
		else:
			return ''

	#check for string value
	def string(self,value,errorMessage = ''):
		if errorMessage:
			self.stringError = errorMessage

		if type(value) not str:
			return self.stringError
		else:
			return ''