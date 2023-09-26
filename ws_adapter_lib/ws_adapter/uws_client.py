# /* ------------- COPYRIGHT NOTICE ---------------
#
# Copyright (C) 2019 FlytBase, Inc. All Rights Reserved.
# Do not remove this copyright notice.
# Do not use, reuse, copy, merge, publish, sub-license, sell, distribute or modify this code - except without explicit,
# written permission from FlytBase, Inc.
# Contact info@flytbase.com for full license information.
# Author: FlytBase, Inc
# ------------- COPYRIGHT NOTICE ---------------*/

# python3 test_client_uws.py wss dev.flytbase.com 443 /websocket

__copyright__ = "Copyright (C) 2019 FlytBase, Inc. All Rights Reserved. " \
                "Do not remove this copyright notice. " \
                "Do not use, reuse, copy, merge, publish, sub-license, sell, distribute " \
                "or modify this code - except without explicit, written permission from FlytBase, Inc."
__license__ = "Contact info@flytbase.com for full license information."
__author__ = "FlytBase, Inc"

import asyncio
import json
import logging
import math
from re import T
import sys
import os
import yaml

from autobahn.asyncio.websocket import WebSocketClientProtocol, WebSocketClientFactory

logger = logging.getLogger('TestClientUWS')
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s : %(name)s : %(levelname)s : %(message)s')

# This object contains the authorization token and vehicleid for the docking station.
# This information can be fetched from https://my.flytbase.com/devices/ after the docking station has been
# registered with the users account. Make sure that this information is accurate

class FlytOSProtocols(WebSocketClientProtocol):
    """
    This class provides a protocol for websocket communication between FlytNow (simulated by this class) and FlytCloud
    """

    def __init__(self, *args, token, vehicle_id, message_cb_dict, **kwargs):
        super().__init__(*args, **kwargs)
        self.if_connected = False
        self.token = token
        self.vehicle_id = vehicle_id
        self.message_cb_dict = message_cb_dict
        # self.drone_ds = DroneDataStructure(vehicle_id=vehicle_id)

    def onConnect(self, response):
        """
        Callback triggered after websocket connection is successful
        @param response:
        @return:
        """
        logger.info(f"Server connected for vehicle {self.vehicle_id}: {response.peer}",
                    extra={'device_id': self.vehicle_id})
        
    

    async def onOpen(self):
        """
        Callback triggered after websocket connection is open.
        Here the first call sent is to authenticate the user by sending an authorization call
        @return:
        """
        logger.info(f"WebSocket connection open for vehicle {self.vehicle_id}",
                    extra={'device_id': self.vehicle_id})
        self.send_auth()

    def onMessage(self, payload, isBinary):
        """
        Function triggered every time a message is received on the websocket connection
        @param payload: JSON decoded message that has been received
        @param isBinary: Boolean to define if the message is a binary message or not
        @return:
        """
        if isBinary:
            logger.warning("Binary message received: {0} bytes".format(len(payload)))
        else:
            payload_dec = payload.decode('utf8')
            try:
                res = json.loads(payload_dec)
                if isinstance(res, dict):
                    if res["op"] == "service_response":
                        if res["service"] == '/websocket_auth':
                            if res["result"]:
                                logger.info(f"Successfully authorized connection for vehicle {self.vehicle_id}",
                                            extra={'device_id': self.vehicle_id})

                                self.if_connected = True
                    if res["op"] == "publish":
                        print(f"Message received: {res}")
                        if res["topic"] in self.message_cb_dict:
                            self.message_cb_dict[res["topic"]](message=res)

            except Exception as e:
                logger.exception(f'Encountered Exception while processing message from ws'
                                 f' for vehicle {self.vehicle_id}: {e}', extra={'device_id': self.vehicle_id})

    def onClose(self, wasClean, code, reason):
        """
        Function triggered when websocket connection is closed.
        @param wasClean:
        @param code:
        @param reason:
        @return:
        """
        self.if_connected = False
        logger.info(f"WebSocket connection closed for vehicle {self.vehicle_id} due to {reason} "
                    f"and code {code}",
                    extra={'device_id': self.vehicle_id})

    def send_auth(self):
        """
        Function to send an authorization service call to FlytCloud with the specific user credentials.
        If user credentials are not valid FlytCloud will automatically terminate the connection
        @return:
        """
        auth_body = {'authorization': self.token, 'vehicleid': self.vehicle_id}

        logger.info(f"==========================================================="
                    f"Sending authorization message for vehicle {self.vehicle_id}",
                    extra={'device_id': self.vehicle_id})
        service_call_object = {"op": "call_service", "id": 123, "service": "/websocket_auth",
                               "args": auth_body}
        srv_call = json.dumps(service_call_object)
        self.sendMessage(srv_call.encode('utf-8'))

    async def _sendMessage(self, resp):
        """
        Function to act as wrapper over the base websocket function to send a message over the websocket connection
        @param resp:
        @return:
        """
        self.sendMessage(resp)
