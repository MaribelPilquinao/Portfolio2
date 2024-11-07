from django.shortcuts import render
from .models import Project, Icon, Education, Contact

def home(request):
    projects = Project.objects.all()
    icons = Icon.objects.all()
    educations = Education.objects.all()
    context = {
        'projects': projects,
        'icons': icons,
        'educations':educations
    }
    return render(request, 'home.html', context)

def contact_view(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    return render(request, 'home.html', {'phone': contact.phone, 'msg': contact.msj})
