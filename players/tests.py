from django.test import TestCase

# Create your tests here.
from django.contrib.staticfiles import finders
from django.http import HttpResponse

def test_static(request):
    result = ''
    if finders.find('css/bootstrap.min.css'):
        result += 'Bootstrap CSS found.<br>'
    else:
        result += 'Bootstrap CSS not found.<br>'

    if finders.find('js/bootstrap.bundle.min.js'):
        result += 'Bootstrap JS found.<br>'
    else:
        result += 'Bootstrap JS not found.<br>'
    
    return HttpResponse(result)
