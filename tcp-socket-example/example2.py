import socket
import json
import binascii
import sys
import struct
from struct import *

# Server IP/Port
ip = '127.0.0.1'
port = 8888
remote_host = (ip, port)

# JSON Command
command = {
    "tag": "example2_req"
}

command_json = json.dumps(command)
length = len(command_json)

packer = struct.Struct('>h{}s'.format(length))
packed_data = packer.pack(length, command_json)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server
    sock.connect(remote_host)

    # Send data
    print >> sys.stdout, 'sending "%s"' % binascii.hexlify(packed_data)
    sock.sendall(packed_data)

    data = sock.recv(2)
    unpacked_data = unpack('>h', data)
    response_len = unpacked_data[0]     # First 2 bytes (short int) is the length of the response
    if response_len > 0:
        response = sock.recv(response_len)
        print 'Response (len = %d): %s' % (response_len, repr(response))

        # Check the tag of the response
        respJsonObj = json.loads(response)
        if respJsonObj['tag'] == 'callback':
            print 'Card Detected Event'

            # Continue reading final response
            data = sock.recv(2)
            unpacked_data = unpack('>h', data)
            response_len = unpacked_data[0]  # First 2 bytes (short int) is the length of the response
            if response_len > 0:
                response = sock.recv(response_len)
                print 'Response (len = %d): %s' % (response_len, repr(response))

except Exception as e:
    print >> sys.stderr, e

finally:
        sock.close()


