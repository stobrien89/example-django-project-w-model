from django.shortcuts import render
# For sending JSON responses
from django.http import JsonResponse
# To serialize objects into json strings
from django.core.serializers import serialize
# To convert json strings into dictionaries
import json

from .models import Turtle
# View class
from django.views import View
# import helper function
from .helpers import GetBody

# class for model routes


class TurtleView(view):
    # Index route
    def get(self, request):
        # get all
        all = Turtle.objects.all()
        # serialize object into json string
        serialized = serialize("json", all)
        # convert json string into a dictionary
        final_data = json.loads(serialized)
        # send json response
        return JsonResponse(final_data, safe=False)

    # Create route
    def post(self, request):
        # get data from request body
        body = GetBody(request)
        print(body)
        # Create new db item
        turtle = Turtle.objects.create(name=body["name"], age=body["age"])
        # Convert new item into json string, then a dict
        final_data = json.loads(serialize("json", [turtle]))
        # Send json response
        return JsonResponse(final_data, safe=False)
