import string
import random

class Keygenerator():

	def generate(self, size=20, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
		return ''.join(random.choice(chars) for _ in range(size))