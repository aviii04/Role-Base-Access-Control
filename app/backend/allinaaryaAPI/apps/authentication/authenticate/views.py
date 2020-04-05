from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def home(request):
    dev = 3
    # logger.info(request.user)
    # logger.info("afaf")
    # logger.error("Test!!")
    # logger.warning("warning")
    return HttpResponse("Hello1 world")