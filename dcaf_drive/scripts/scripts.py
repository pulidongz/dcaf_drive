from django.conf import settings
from landsat.google_download import GoogleDownload

class DownloadLandsat():
	g = GoogleDownload(start='2019-11-01', end='2019-11-01', satellite=8, path='116', row='50', output_path=settings.DATA_DIR+'/landsat')
	g.download()

class Ping():
  print("Hello from a function")