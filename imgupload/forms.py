from django.forms import ModelForm
from django import forms
from imgupload.models import images, YES_OR_NO


class ImageUploadForm(ModelForm):
    public = forms.ChoiceField(label="Do you want this image to be publicly avaliable?", widget=forms.RadioSelect, choices=YES_OR_NO, initial=1)
    class Meta:
        model = images
        exclude = ("uploaded_on",)
        widgets = {
             'public': forms.RadioSelect
        }