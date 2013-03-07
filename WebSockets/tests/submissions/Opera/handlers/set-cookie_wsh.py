#!/usr/bin/python

from mod_pywebsocket import common, msgutil, util
from mod_pywebsocket.handshake import hybi


def web_socket_do_extra_handshake(request):
    cookie_id = ''
    if '?' in request.ws_resource:
        cookie_id = request.ws_resource.split('?', 1)[1]
    request.connection.write('HTTP/1.1 101 Switching Protocols:\x0D\x0AConnection: Upgrade\x0D\x0AUpgrade: WebSocket\x0D\x0ASet-Cookie: ws_testws_test_'+cookie_id+'=test; Path=/\x0D\x0ASec-WebSocket-Origin: '+request.ws_origin+'\x0D\x0ASec-WebSocket-Accept: '+hybi.compute_accept(request.headers_in.get(common.SEC_WEBSOCKET_KEY_HEADER))[0]+'\x0D\x0A\x0D\x0A')
    return

def web_socket_transfer_data(request):
    while True:
        return
