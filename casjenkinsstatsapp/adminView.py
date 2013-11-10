from django.shortcuts import render_to_response
from django.template import RequestContext
from casjenkinsstatsapp.models import Table


def initPage(request):

    # get data
    tables = Table.objects.all()

    # return data
    return render_to_response('admin.html',
                              {
                                  'tables': tables,
                                  'isAdmin': True
                              },
                              context_instance=RequestContext(request))


def addTable(request):

    GET = request.GET
    tableName = GET.get('tableName').encode()
    tableDescription = GET.get('tableDescription').encode()
    link = GET.get('link').encode()
    maxGuests = int(GET.get('maxGuests').encode())

    table = Table(max_guests=maxGuests, name=tableName, description=tableDescription, link=link)
    table.save()

    return initPage(request)


def deleteTable(request):

    GET = request.GET
    tableId = GET.get('tableId').encode()

    table = Table.objects.get(pk=tableId)
    table.delete()

    return initPage(request)

