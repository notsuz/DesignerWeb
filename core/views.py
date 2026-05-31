from django.shortcuts import render
from .models import Projects,UiDesign

# Create your views here.
def index(request):
    
    project=Projects.objects.all()
    uidesign=UiDesign.objects.all()
    
    context={
        'project':project,
        'uidesign':uidesign
    }
    return render(request, 'core/index.html',context)


