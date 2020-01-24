from django.db import models
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField

from filer.models.filemodels import File
from filer import settings as filer_settings

class Dat(File):
	_icon = "DAT"
	# name = models.CharField(max_length=255)
	# file = FilerFileField(null=True, blank=True, on_delete = models.CASCADE, related_name="dat")

@classmethod
def matches_file_type(cls, iname, ifile, request):
    # the extensions we'll recognise for this file type
	filename_extensions = ['.dat', '.DAT',]
	ext = os.path.splitext(iname)[1].lower()
	return ext in filename_extensions

class Tiff(models.Model):
	name = models.CharField(max_length=255)
	file = FilerFileField(null=True, blank=True, on_delete = models.CASCADE, related_name="tiff")
	created_at = models.DateTimeField(auto_now_add=True)

	def matches_file_type(cls, iname, ifile, request):
	    # the extensions we'll recognise for this file type
		filename_extensions = ['.tiff', '.TIFF',]
		ext = os.path.splitext(iname)[1].lower()
		return ext in filename_extensions

class Dbf(models.Model):
	name = models.CharField(max_length=255)
	file = FilerFileField(null=True, blank=True, on_delete = models.CASCADE, related_name="dbf")
	created_at = models.DateTimeField(auto_now_add=True)

	def matches_file_type(cls, iname, ifile, request):
	    # the extensions we'll recognise for this file type
		filename_extensions = ['.dbf', '.DBF',]
		ext = os.path.splitext(iname)[1].lower()
		return ext in filename_extensions

class Prj(models.Model):
	name = models.CharField(max_length=255)
	file = FilerFileField(null=True, blank=True, on_delete = models.CASCADE, related_name="prj")
	created_at = models.DateTimeField(auto_now_add=True)

	def matches_file_type(cls, iname, ifile, request):
	    # the extensions we'll recognise for this file type
		filename_extensions = ['.prj', '.PRJ',]
		ext = os.path.splitext(iname)[1].lower()
		return ext in filename_extensions

class Sbn(models.Model):
	name = models.CharField(max_length=255)
	file = FilerFileField(null=True, blank=True, on_delete = models.CASCADE, related_name="sbn")
	created_at = models.DateTimeField(auto_now_add=True)

	def matches_file_type(cls, iname, ifile, request):
	    # the extensions we'll recognise for this file type
		filename_extensions = ['.sbn', '.SBN',]
		ext = os.path.splitext(iname)[1].lower()
		return ext in filename_extensions

class Sbx(models.Model):
	name = models.CharField(max_length=255)
	file = FilerFileField(null=True, blank=True, on_delete = models.CASCADE, related_name="sbx")
	created_at = models.DateTimeField(auto_now_add=True)

	def matches_file_type(cls, iname, ifile, request):
	    # the extensions we'll recognise for this file type
		filename_extensions = ['.sbx', '.SBX',]
		ext = os.path.splitext(iname)[1].lower()
		return ext in filename_extensions

class Shp(models.Model):
	name = models.CharField(max_length=255)
	file = FilerFileField(null=True, blank=True, on_delete = models.CASCADE, related_name="shp")
	created_at = models.DateTimeField(auto_now_add=True)

	def matches_file_type(cls, iname, ifile, request):
	    # the extensions we'll recognise for this file type
		filename_extensions = ['.shp', '.SHP',]
		ext = os.path.splitext(iname)[1].lower()
		return ext in filename_extensions

class Shx(models.Model):
	name = models.CharField(max_length=255)
	file = FilerFileField(null=True, blank=True, on_delete = models.CASCADE, related_name="shx")
	created_at = models.DateTimeField(auto_now_add=True)

	def matches_file_type(cls, iname, ifile, request):
	    # the extensions we'll recognise for this file type
		filename_extensions = ['.shx', '.SHX',]
		ext = os.path.splitext(iname)[1].lower()
		return ext in filename_extensions

class Csv(models.Model):
	name = models.CharField(max_length=255)
	file = FilerFileField(null=True, blank=True, on_delete = models.CASCADE, related_name="csv")
	created_at = models.DateTimeField(auto_now_add=True)

	def matches_file_type(cls, iname, ifile, request):
	    # the extensions we'll recognise for this file type
		filename_extensions = ['.csv', '.CSV',]
		ext = os.path.splitext(iname)[1].lower()
		return ext in filename_extensions

class Png(models.Model):
	name = models.CharField(max_length=255)
	file = FilerImageField(null=True, blank=True, on_delete = models.CASCADE, related_name="png")
	created_at = models.DateTimeField(auto_now_add=True)

	def matches_file_type(cls, iname, ifile, request):
	    # the extensions we'll recognise for this file type
		filename_extensions = ['.png', '.PNG',]
		ext = os.path.splitext(iname)[1].lower()
		return ext in filename_extensions