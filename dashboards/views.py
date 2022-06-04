from django.shortcuts import render

# Create your views here.
def home(request):
    template_name = 'sb-admin-2/index.html'
    context = {}
    return render(request, template_name, context)