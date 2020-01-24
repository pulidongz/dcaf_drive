from django.contrib.auth.models import User
from django.conf import settings
from filer.models import File, Folder, Image
import sys, requests

def fileProp():
	for f in File.objects.filter(is_public=True):
		sys.stdout.write(u'moving %s to public storage... ' % f.id)
		# f.is_public = False
		f.delete()
		sys.stdout.write(u'done\n')


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

	file = {'file': open(settings.DATA_DIR+'/landsat/'+'/'+'sampol.txt', 'rb')}

	upload_request = requests.post(url=ADD_URL, files=file, cookies=login_request.cookies)
	print(upload_request.text)