from django.contrib.auth.models import User
from landsat.google_download import GoogleDownload
from django.conf import settings
from filer.models import File, Folder, Image
import sys, requests, os

# SAMPLE / TEST CODES


def fileProp():
	for f in File.objects.filter(is_public=True):
		sys.stdout.write(u'moving %s to public storage... ' % f.id)
		# f.is_public = False
		f.delete()
		sys.stdout.write(u'done\n')

# Upload processed data to DCAF drive for public access.
# Location of source directory is 'output'.
def uploadFile():
	LOGIN_URL = 'http://localhost:8000/login/?next=/'
	ADD_URL = 'http://localhost:8000/filer/clipboard/operations/upload/no_folder/'
	UN = 'dcafadmin'
	PWD = 'admin'

	session_requests = requests.session()
	result 			 = session_requests.get(LOGIN_URL)
	token 			 = result.cookies['csrftoken']
	login_request	 = session_requests.post(
							LOGIN_URL,
							data={
								'username':UN,
								'password':PWD,
								'csrfmiddlewaretoken':token,
								'next':'/'
							})

	for subdir, dirs, files in os.walk(settings.DATA_DIR+'/output'):
		for filename in files:
			filepath = subdir + os.sep + filename

			# Change ".txt" to file extension that will be used.
			if filepath.endswith(".txt"):
				f = {'file': open(filepath, 'rb')}
				upload_request = requests.post(url=ADD_URL, files=f, cookies=login_request.cookies)
				print(upload_request.text)


# Function for download landsat data
def DownloadLandsat():
	g = GoogleDownload(start='2019-11-01', end='2019-11-01', satellite=8, path='116', row='50', output_path=settings.DATA_DIR+'/landsat')
	g.download()

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


