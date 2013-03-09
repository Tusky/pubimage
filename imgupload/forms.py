from django.forms import ModelForm
from django import forms
from imgupload.models import images, YES_OR_NO


class ImageUploadForm(ModelForm):
    public = forms.ChoiceField(label="Do you want this image to be publicly avaliable?", widget=forms.RadioSelect, choices=YES_OR_NO, initial=1)

    class Meta:
        model = images
        exclude = ("uploaded_on","uploaded_by","likes","dislikes","views")
        widgets = {
             'public': forms.RadioSelect
        }

    def __init__(self, *args, **kwargs):
        self.uploaded_by = kwargs.pop('uploaded_by')
        super(ImageUploadForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(ImageUploadForm, self).save(commit=False)
        obj.uploaded_by = self.uploaded_by
        obj.save()
        return obj