from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from imgupload.forms import ImageUploadForm
from imgupload.models import images


@login_required
def upload_new_image(request):
    form = ImageUploadForm(uploaded_by=request.user)
    if request.POST:
        form = ImageUploadForm(request.POST, request.FILES, uploaded_by=request.user)
        if form.is_valid():
            form.save()
            return redirect("manage")
        else:
            return render(request, 'upload.html', { "form": form})
    else:
        return render(request, 'upload.html', { "form": form})

@login_required
def manage_images(request):
    images_to_list = images.objects.filter(uploaded_by = request.user)
    return render(request, 'manage.html', { "images": images_to_list})

@login_required
def remove_image(request, image_id):
    images.objects.get(pk=image_id, uploaded_by=request.user).delete()
    return redirect("manage")

def show_image(request, image_id):
    imageStuff = images.objects.get(pk=image_id)
    imageStuff.views += 1
    imageStuff.save()
    return render(request, 'single_image.html', { "image": imageStuff})

def like_image(request, image_id):
    imageStuff = images.objects.get(pk=image_id)
    imageStuff.likes += 1
    imageStuff.save()
    return redirect("show_image", image_id)

def dislike_image(request, image_id):
    imageStuff = images.objects.get(pk=image_id)
    imageStuff.dislikes += 1
    imageStuff.save()
    return redirect("show_image", image_id)

def top10_list(request):
    images_list = images.objects.filter(public = True).order_by("-likes")[:10]
    return render(request, 'top10.html', { "images": images_list})

