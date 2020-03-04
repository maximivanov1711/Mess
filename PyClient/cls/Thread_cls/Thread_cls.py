import threading
import time


class Printer(threading.Thread):
	def __init__(self, name):
		threading.Thread.__init__(self)
		self.name = name
		self.stop = False
	
	def run(self):
		while True:
			if not self.stop:
				print('message')
				time.sleep(10)
			else:
				break