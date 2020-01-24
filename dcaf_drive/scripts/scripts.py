from django.conf import settings
from django.utils.crypto import get_random_string
from landsat.google_download import GoogleDownload
import os

# INSERT CUSTOM PYTHON SCRIPTS HERE

# After generating processed data, use this function to upload file
# to DCAF drive for public access.
# Location of source directory is 'output' folder.
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