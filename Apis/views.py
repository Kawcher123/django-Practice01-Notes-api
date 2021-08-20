from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint':'/notes/',
            'method':'GET',
            'body':None,
            'description':'Return an array of notes'
        },
         {
            'Endpoint':'/notes/id',
            'method':'GET',
            'body':None,
            'description':'Return a single note of objects'
        },
         {
            'Endpoint':'/notes/create',
            'method':'POST',
            'body':{'body':""},
            'description':'Create new note with data sent in post request'
        },
         {
            'Endpoint':'/notes/update',
            'method':'PUT',
            'body':{'body':""},
            'description':'Creates an existing note with data sent in put request'
        },
         {
            'Endpoint':'/notes/',
            'method':'DELETE',
            'body':None,
            'description':'Deletes and existing note'
        },
    ]
    return Response(routes)


@api_view(['GET'])
def getNotes(requset):
    notes=Note.objects.all()
    serializer=NoteSerializer(notes,many=True)
    return Response(serializer.data)

