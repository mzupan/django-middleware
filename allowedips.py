from django.conf import settings
from django import http

import struct, socket

class AllowedIPS(object):
    def addressInNetwork(self, ip, net):
        ipblock = ip.split('.')

        for netblock in net.split('.'):
            if netblock != ipblock[i]:
                return False

        return True

    def process_request(self, request):
        for block in settings.ALLOWED_IPS:
            if self.addressInNetwork(request.META['REMOTE_ADDR'], block):
                return None

        return http.HttpResponseForbidden('<h1>Forbidden</h1><p>You can only access this from the office or VPN')
