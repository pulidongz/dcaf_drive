from django.conf import settings
from django.utils.crypto import get_random_string
from landsat.google_download import GoogleDownload
import os

# INSERT CUSTOM PYTHON SCRIPTS HERE

def DownloadLandsat():
	g = GoogleDownload(start='2019-11-01', end='2019-11-01', satellite=8, path='116', row='50', output_path=settings.DATA_DIR+'/landsat')
	g.download()

def Ping():
  print("Hello from a function")

def CreateFile():
	filename = get_random_string(length=10)
	os.mkdir('landsat/'+filename)
	file_dat = open(settings.DATA_DIR+'/landsat/'+filename+'/'+filename+'.dat', "w+")
	for i in range(10):
		file_dat.write("This is line %d\r\n" % (i+1))
	file_dat.close()
	
	file_tiff = open(settings.DATA_DIR+'/landsat/'+filename+'/'+filename+'.tif', "w+")
	for i in range(10):
		file_tiff.write("This is line %d\r\n" % (i+1))
	file_tiff.close()
	
	file_dbf = open(settings.DATA_DIR+'/landsat/'+filename+'/'+filename+'.dbf', "w+")
	for i in range(10):
		file_dbf.write("This is line %d\r\n" % (i+1))
	file_dbf.close()

	file_prj = open(settings.DATA_DIR+'/landsat/'+filename+'/'+filename+'.prj', "w+")
	for i in range(10):
		file_prj.write("This is line %d\r\n" % (i+1))
	file_prj.close()

	file_sbn = open(settings.DATA_DIR+'/landsat/'+filename+'/'+filename+'.sbn', "w+")
	for i in range(10):
		file_sbn.write("This is line %d\r\n" % (i+1))
	file_sbn.close()

	file_sbx = open(settings.DATA_DIR+'/landsat/'+filename+'/'+filename+'.sbx', "w+")
	for i in range(10):
		file_sbx.write("This is line %d\r\n" % (i+1))
	file_sbx.close()

	file_shp = open(settings.DATA_DIR+'/landsat/'+filename+'/'+filename+'.shp', "w+")
	for i in range(10):
		file_shp.write("This is line %d\r\n" % (i+1))
	file_shp.close()

	file_shx = open(settings.DATA_DIR+'/landsat/'+filename+'/'+filename+'.shx', "w+")
	for i in range(10):
		file_shx.write("This is line %d\r\n" % (i+1))
	file_shx.close()

	file_csv = open(settings.DATA_DIR+'/landsat/'+filename+'/'+filename+'.csv', "w+")
	for i in range(10):
		file_csv.write("This is line %d\r\n" % (i+1))
	file_csv.close()

	file_png = open(settings.DATA_DIR+'/landsat/'+filename+'/'+filename+'.png', "w+")
	for i in range(10):
		file_png.write("This is line %d\r\n" % (i+1))
	file_png.close()


