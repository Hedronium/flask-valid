import os
import sys
from flask import request

class Validator:
	def __init__():
		pass

	def require(value):
		if value == "":
			return False
		else:
			return True

	def max(value,max):
		try:
			val = int(value)
			if (val > max ):
				return False

		except ValueError:
			print('it\'s not an integer')

	def min(value,min):
		try:
			val = int(value)
			if val < min:
				return False

		except ValueError: