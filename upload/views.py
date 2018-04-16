from django.shortcuts import render,HttpResponseRedirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm
from core.models import VideoDetails
# Create your views here.
def handle_uploaded_file(f):
    with open('home/anirudh/eschool/media/' + f.title + '.pdf', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = VideoDetails(document=request.FILES['file'])
            
            instance.teacher = request.user
            instance.course = form.cleaned_data['course']
            instance.video_name = form.cleaned_data['vid_name']
            instance.save()
            return HttpResponseRedirect('/')
    else:
        form = UploadFileForm()
    return render(request, 'upload/index.html', {'form': form})