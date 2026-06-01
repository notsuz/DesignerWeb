from django.shortcuts import render
from .models import Projects,UiDesign,Logo

# Create your views here.
def index(request):
    
    project=Projects.objects.all()
    uidesign=UiDesign.objects.all()
    logo=Logo.objects.all()
    
    context={
        'project':project,
        'uidesign':uidesign,
        'logo':logo
    }
    return render(request, 'core/index.html',context)


