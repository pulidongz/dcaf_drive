from django.conf import settings
from django.utils.crypto import get_random_string
from landsat.google_download import GoogleDownload
import os

# INSERT CUSTOM PYTHON SCRIPTS HERE

# class DownloadLandsat():
# 	g = GoogleDownload(start='2019-11-01', end='2019-11-01', satellite=8, path='116', row='50', output_path=settings.DATA_DIR+'/landsat')
# 	g.download()

def Ping():
  print("Hello from a function")

def CreateFile():
	filename_1 = get_random_string(length=10) + '.TIFF'
	file_1 = open(settings.DATA_DIR+'/landsat/'+filename_1, "w+")
	for i in range(10):
		file_1.write("This is line %d\r\n" % (i+1))
	file_1.close()
	filename_2 = get_random_string(length=10) + '.txt'
	file_2 = open(settings.DATA_DIR+'/landsat/'+filename_2, "w+")
	for i in range(10):
		file_2.write("This is line %d\r\n" % (i+1))
	file_2.close()
	filename_3 = get_random_string(length=10) + '.shp'
	file_3 = open(settings.DATA_DIR+'/landsat/'+filename_3, "w+")
	for i in range(10):
		file_3.write("This is line %d\r\n" % (i+1))
	file_3.close()