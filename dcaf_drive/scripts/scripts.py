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
	filename = get_random_string(length=10)
	os.mkdir('landsat/'+filename)
	file_dat = open(settings.DATA_DIR+'/landsat/'+filename+'/'+filename+'.dat', "w+")
	# for i in range(10):
	# 	file_1.write("This is line %d\r\n" % (i+1))
	file_dat.close()
	
	file_tiff = open(settings.DATA_DIR+'/landsat/'+filename+'/'+filename+'.tif', "w+")
	file_tiff.close()
	
	file_dbf = open(settings.DATA_DIR+'/landsat/'+filename+'/'+filename+'.dbf', "w+")
	file_dbf.close()

	file_prj = open(settings.DATA_DIR+'/landsat/'+filename+'/'+filename+'.prj', "w+")
	file_prj.close()

	file_sbn = open(settings.DATA_DIR+'/landsat/'+filename+'/'+filename+'.sbn', "w+")
	file_sbn.close()

	file_sbx = open(settings.DATA_DIR+'/landsat/'+filename+'/'+filename+'.sbx', "w+")
	file_sbx.close()

	file_shp = open(settings.DATA_DIR+'/landsat/'+filename+'/'+filename+'.shp', "w+")
	file_shp.close()

	file_shx = open(settings.DATA_DIR+'/landsat/'+filename+'/'+filename+'.shx', "w+")
	file_shx.close()

	file_csv = open(settings.DATA_DIR+'/landsat/'+filename+'/'+filename+'.csv', "w+")
	file_csv.close()

	file_png = open(settings.DATA_DIR+'/landsat/'+filename+'/'+filename+'.png', "w+")
	file_png.close()