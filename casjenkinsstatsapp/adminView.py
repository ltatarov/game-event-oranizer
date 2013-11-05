from django.shortcuts import render_to_response
from django.template import RequestContext
from casjenkinsstatsapp import STATUS_OK, STATUS_FAIL
from casjenkinsstatsapp.models import Table


def initPage(request):

    # get data
    eventData = None

    # return data
    return render_to_response('admin.html',
                              {'eventData': eventData},
                              context_instance=RequestContext(request))


def addTable(request, table):

    table = Table(max_guests=table.get('maxGuests'), name=table.get('name'), description=table.get('description'))
    table.save()

    #TODO: find better way to assert guest created
    assertTable = Table.objects.get(pk=table.pk)
    if assertTable:
        status = STATUS_OK
    else:
        status = STATUS_FAIL
    return render_to_response('admin.html',
                              {'status': status},
                              context_instance=RequestContext(request))


def removeTable(request, tableId):

    table = Table.objects.get(pk=tableId)
    table.delete()

    #TODO: find better way to assert guest deleted
    assertTable = Table.objects.get(pk=tableId)
    if assertTable:
        status = STATUS_FAIL
    else:
        status = STATUS_OK
    return render_to_response('admin.html',
                              {'status': status},
                              context_instance=RequestContext(request))

