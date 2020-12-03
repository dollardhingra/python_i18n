from django.utils.translation import gettext as _

def my_view(request):
    greetings = _("Hello, world!")
    return HttpResponse("greetings")