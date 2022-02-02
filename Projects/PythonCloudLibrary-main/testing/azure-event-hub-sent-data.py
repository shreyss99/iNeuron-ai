import asyncio
import uuid

from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData
import json
import pandas as pd
from project_library_layer.datetime_libray.date_time import get_time,get_date
async def start_sending(prediction_label,project_name,execution_id):
    # Create a producer client to send messages to the event hub.
    # Specify a connection string to your event hubs namespace and
    # the event hub name.
    connection_string="Endpoint=sb://avnish327030.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=BwK0zozJe+Oz46F5BgpHUtq5zkzqMKCzPdc2kOg2WW8="
    event_hub_name="streaming-data-327030"
    producer = EventHubProducerClient.from_connection_string(conn_str=connection_string, eventhub_name=event_hub_name)
    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()
        directory=r"company_name/project/{}".format(project_name)
        data = {'predictions':prediction_label, 'project_name': project_name,'execution_id':"{}/{}_{}_{}".format(directory,execution_id,get_date().replace('-','_'),get_time().replace(':','_'))}
        print(data)
        event_data_batch.add(EventData(str(json.dumps(data))))
        await producer.send_batch(event_data_batch)

"""
loop = asyncio.get_event_loop()
loop.run_until_complete(run())

"""
def start_call(prediction_label,project_name,execution_id):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_sending(prediction_label,project_name,execution_id))
    loop.close()


start_call(prediction_label="No",project_name="sentiment_analysis",execution_id=str(uuid.uuid4()))