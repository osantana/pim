# tag::initial-test-view[]
from django.http import HttpResponse


def hello(request):
    return HttpResponse('Hello World!')
# end::initial-test-view[]
