# Create your views here.
import json
from django.http import QueryDict, HttpResponse

from django.shortcuts import render_to_response
from django.template import RequestContext
from casjenkinsstatsapp.models import Guest, Table, Membership


def initPage(request):

    # get event data
    tables = Table.objects.all()

    # return data
    return render_to_response('main.html',
                              {'tables': tables},
                              context_instance=RequestContext(request))


def addGuest(request):

    GET = request.GET
    guest = QueryDict(GET.get('guest').encode())
    tableId = int(GET.get('tableId').encode())

    newGuest = Guest(name=guest.get('name'))
    newGuest.save()
    table = Table.objects.get(pk=tableId)
    membership = Membership(table=table, guest=newGuest)
    membership.save()

    json_response = json.dumps({'guestId': newGuest.pk})
    return HttpResponse(json_response, mimetype='application/json')


def deleteGuest(request):

    GET = request.GET
    guestId = GET.get('guestId').encode()

    guest = Guest.objects.get(pk=guestId)
    guest.delete()

    return initPage(request)

