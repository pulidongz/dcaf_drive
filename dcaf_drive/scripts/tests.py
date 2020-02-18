from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.conf import settings
from filer.models import File, Folder, Image
import sys, requests, os

# SAMPLE / TEST CODES

# Text file creation for testing
def MakeTextFile():
	filename = get_random_string(length=10)
	file_zip = open(settings.DATA_DIR+'/output/'+filename+'.txt', "w+")
	for i in range(10):
		file_zip.write("This is line %d\r\n" % (i+1))
	file_zip.close()

# File creation for testing
def CreateFile():
	filename = get_random_string(length=10)
	os.mkdir('output/'+filename)
	file_zip = open(settings.DATA_DIR+'/output/'+filename+'/'+filename+'.zip', "w+")
	for i in range(10):
		file_zip.write("This is line %d\r\n" % (i+1))
	file_zip.close()

	file_dat = open(settings.DATA_DIR+'/output/'+filename+'/'+filename+'.dat', "w+")
	for i in range(10):
		file_dat.write("This is line %d\r\n" % (i+1))
	file_dat.close()
	
	file_tiff = open(settings.DATA_DIR+'/output/'+filename+'/'+filename+'.tif', "w+")
	for i in range(10):
		file_tiff.write("This is line %d\r\n" % (i+1))
	file_tiff.close()
	
	file_dbf = open(settings.DATA_DIR+'/output/'+filename+'/'+filename+'.dbf', "w+")
	for i in range(10):
		file_dbf.write("This is line %d\r\n" % (i+1))
	file_dbf.close()

	file_prj = open(settings.DATA_DIR+'/output/'+filename+'/'+filename+'.prj', "w+")
	for i in range(10):
		file_prj.write("This is line %d\r\n" % (i+1))
	file_prj.close()

	file_sbn = open(settings.DATA_DIR+'/output/'+filename+'/'+filename+'.sbn', "w+")
	for i in range(10):
		file_sbn.write("This is line %d\r\n" % (i+1))
	file_sbn.close()

	file_sbx = open(settings.DATA_DIR+'/output/'+filename+'/'+filename+'.sbx', "w+")
	for i in range(10):
		file_sbx.write("This is line %d\r\n" % (i+1))
	file_sbx.close()

	file_shp = open(settings.DATA_DIR+'/output/'+filename+'/'+filename+'.shp', "w+")
	for i in range(10):
		file_shp.write("This is line %d\r\n" % (i+1))
	file_shp.close()

	file_shx = open(settings.DATA_DIR+'/output/'+filename+'/'+filename+'.shx', "w+")
	for i in range(10):
		file_shx.write("This is line %d\r\n" % (i+1))
	file_shx.close()

	file_csv = open(settings.DATA_DIR+'/output/'+filename+'/'+filename+'.csv', "w+")
	for i in range(10):
		file_csv.write("This is line %d\r\n" % (i+1))
	file_csv.close()

	file_png = open(settings.DATA_DIR+'/landsat/'+filename+'/'+filename+'.png', "w+")
	for i in range(10):
		file_png.write("This is line %d\r\n" % (i+1))
	file_png.close()


