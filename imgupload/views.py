from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from imgupload.forms import ImageUploadForm
from imgupload.models import images


@login_required
def upload_new_image(request):
    form = ImageUploadForm()
    if request.POST:
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'upload.html', { "form": form})
        else:
            return render(request, 'upload.html', { "form": form})
    else:
        return render(request, 'upload.html', { "form": form})
