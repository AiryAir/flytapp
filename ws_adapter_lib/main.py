from ws_adapter.ws_adapter import FlytOSWSAdapter
import yaml
import asyncio
import json




if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # topic_callback_dict = {"/flytos/mavros/global_position/global":global_position_cb}
    topic_callback_dict = {}

    ws_adapter = FlytOSWSAdapter(auth_token="Token c25f2beaa3607503a8790c3dcb14cc3cb093f42b",vehicle_id="PrZvPMc6",
                                 message_cb_dict=topic_callback_dict)
    # loop.run_forever()
    loop.run_forever()
    loop.close()
