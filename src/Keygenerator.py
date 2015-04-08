import string
import random

class Keygenerator():

	def gen_key(size=20, chars=string.ascii_uppercase + string.digits):
		return ''.join(random.SystemRandom(chars) for __ in range(size))