# Library for working with json
import json


def GetBody(request):
    # decode the request body into a unicode string
    unicode = request.body.decode('utf-8')
    # convert unicode string into Python dictionary
    return json.loads(unicode)
