# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from casjenkinsstatsapp import STATUS_OK, STATUS_FAIL
from casjenkinsstatsapp.models import Guest, Table


def initPage(request):

    # get event data
    tables = Table.objects.all()

    # return data
    return render_to_response('main.html',
                              {'tables': tables},
                              context_instance=RequestContext(request))


def addGuest(request, tableId, guest):

    table = Table.objects.get(pk=tableId)
    newGuest = Guest(name=guest.get('name'), table=table)
    newGuest.save()

    #TODO: find better way to assert guest created
    assertGuest = Guest.objects.get(pk=newGuest.pk)
    if assertGuest:
        status = STATUS_OK
    else:
        status = STATUS_FAIL
    return render_to_response('main.html',
                              {'status': status},
                              context_instance=RequestContext(request))


def removeGuest(request, guestId):
    guest = Guest.objects.get(pk=guestId)
    guest.delete()

    #TODO: find better way to assert guest deleted
    assertGuest = Guest.objects.get(pk=guestId)
    if assertGuest:
        status = STATUS_FAIL
    else:
        status = STATUS_OK
    return render_to_response('main.html',
                              {'status': status},
                              context_instance=RequestContext(request))

