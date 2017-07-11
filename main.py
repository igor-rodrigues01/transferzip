from datetime import datetime

import zipfile
import os

class Main():
	_now = None

	def __init__(self,path='teste.txt'):
		self.delete_zip()
		self.create_zip(path)
		self._now = datetime.now()

	def create_zip(self,path):
		zf = zipfile.ZipFile(path,'w')
		zf.write(path,compress_type=zipfile.ZIP_DEFLATED)
		zf.close()

	def delete_zip(self,path="."):
	    files = os.listdir(path)
	    for f in files:
	    	if f != 'main.py':
	    		os.remove(f)  



if __name__ == '__main__':
   m = Main()
   m.delete()