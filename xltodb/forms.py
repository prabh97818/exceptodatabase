from django import forms
from django.core.validators import FileExtensionValidator

class Upload_File(forms.Form):
    upload_file = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['xls','xlsx'])])