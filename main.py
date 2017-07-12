from datetime import datetime

import zipfile
import os

class Main():
	_now  = None
	_path_zip = None

	def __init__(self,path_zip='teste.txt'):
		self._path_zip = path_zip
		self._now      = datetime.now()

	def create_zip(self,path_zip):
		zf = zipfile.ZipFile("shape_file.zip",'w')
		zf.write(path_zip,compress_type=zipfile.ZIP_DEFLATED)
		zf.close()

	def delete_zip(self,path_dir="."):
	    files = os.listdir(path_dir)
	    
	    for f in files:
	    	if f != 'main.py':
	    		os.remove(f) 
 
	def main(self):
		hrs = self._now.hour
		path = self._path_zip

		if hrs == 00 or hrs == 0:
			# self.delete_zip()
			self.create_zip(path)




if __name__ == '__main__':
   m = Main()
   m.main()