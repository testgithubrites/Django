from django.http import HttpResponse

def index(request):
    return HttpResponse('''<h1><a href="https://www.linkedin.com/in/shrutinagpal/">Linkedin</a></h1>''')
