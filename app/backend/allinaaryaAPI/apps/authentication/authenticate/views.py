import logging

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from apps.utils.User.checkPrivilege import has_privilege
from apps.utils.User.Privilege import Privilege

logger = logging.getLogger(__name__)



@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
@has_privilege([Privilege.TEST_PRIVILEGE, Privilege.TEST_PRIVILEGE2])
def home(request):
    logger.info("Info")
    logger.error("Error!!")
    logger.warning("Warning")
    return HttpResponse("Hello1 world")