from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    template = loader.get_template('home_page.html')
    return HttpResponse(template.render({}, request))
