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

from ws_adapter.uws_client import FlytOSProtocols
from autobahn.asyncio.websocket import WebSocketClientFactory


logger = logging.getLogger('WSAdapter')
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s : %(name)s : %(levelname)s : %(message)s')



class FlytOSWSAdapter:
    """
    This class provides a protocol for websocket communication between FlytNow (simulated by this class) and FlytCloud
    reference: https://devdocs.flytbase.com/    
    """

    def __init__(self,vehicle_id,auth_token,message_cb_dict):

        try:
            target_url = "wss://dev.flytbase.com/websocket"
            self.factory = WebSocketClientFactory(target_url)
            self.protocol = FlytOSProtocols(token=auth_token,vehicle_id=vehicle_id,message_cb_dict=message_cb_dict)
            self.factory.protocol = lambda: self.protocol

            self.loop = asyncio.get_event_loop()
            coro = self.loop.create_connection(self.factory, 'dev.flytbase.com', 443, ssl=True)
            self.loop.run_until_complete(coro)
        except Exception as e:
            logger.exception(f"Exception occured while initializing WSAdapter: {e},exc_info=True")

    async def publish(self,message):
        try:
            message_body = json.dumps(message)
            await self.protocol._sendMessage(message_body.encode('utf-8'))
        except Exception as e:
            logger.exception("Exception occured while publishing message: {e},exc_info=True")

    async def send_takeoff(self,takeoff_alt):
        try:
            takeoff_call = {"op": "call_service", "id": 123, "service": "navigation/take_off",
                                    "args": {"takeoff_alt": takeoff_alt}}
            # srv_call = json.dumps(takeoff_call)
            await self.publish(takeoff_call)
        except Exception as e:
            logger.exception("Exception occured while sending takeoff call: {e},exc_info=True")
    
    async def arm(self):
        try:
            arm_call = {"op": "call_service", "id": 123, "service": "navigation/arm",
                                    "args": {}}
            await self.publish(arm_call)
        except Exception as e:
            logger.exception("Exception occured while sending arm call: {e},exc_info=True")


    async def disarm(self):
        try:
            disarm_call = {"op": "call_service", "id": 123, "service": "navigation/disarm",
                                    "args": {}}
            await self.publish(disarm_call)
        except Exception as e:
            logger.exception("Exception occured while sending disarm call: {e},exc_info=True")

    async def land(self):
        try:
            land_call = {"op": "call_service", "id": 123, "service": "navigation/land",
                                    "args": {}}
            await self.publish(land_call)
        except Exception as e:
            logger.exception("Exception occured while sending land call: {e},exc_info=True")

    async def set_mode(self,mode):
        try:
            set_mode_call = {"op": "call_service", "id": 123, "service": "navigation/set_mode",
                                    "args": {"mode": mode}}
            await self.publish(set_mode_call)
        except Exception as e:
            logger.exception("Exception occured while sending set_mode call: {e},exc_info=True")

    async def position_set_global(self,latitude,longitude,relative_altitude,yaw, yaw_valid, tolerance):
        try:
            position_set_global_call = {"op": "call_service", "id": 123, "service": "navigation/position_set_global",
                                    "args": {"lat_x": latitude,"long_y": longitude,"rel_alt_z": relative_altitude,"yaw": yaw,
                                             "yaw_valid": yaw_valid,"tolerance": tolerance}}
            await self.publish(position_set_global_call)
        except Exception as e:
            logger.exception("Exception occured while sending position_set_global call: {e},exc_info=True")

    

    


        




