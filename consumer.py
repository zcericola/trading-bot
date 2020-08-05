import json
from operator import itemgetter
import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_REST_URL = os.getenv("APCA_API_REST_BASE_URL")
API_STREAM_URL = os.getenv("APCA_API_STREAM_BASE_URL")
API_KEY = os.getenv("APCA_API_KEY")
API_SECRET = os.getenv("APCA_API_SECRET")


class Consumer():
    def __init__(self):
        self.apca_headers = {
            'APCA-API-KEY-ID': API_KEY,
            'APCA-API-SECRET-KEY': API_SECRET
        }

    def get(self, is_stream_api, resource, params=''):
        # check whether to use the real-time sockets endpoint or the normal REST api
        connection = None
        if is_stream_api == True:
            connection = API_STREAM_URL
        else:
            connection = API_REST_URL

        destinationURL = f'{connection}/{resource}'
        try:

            print(f'REQUEST INIT - URL: {connection}/{resource}')
            print(f'PARAMS: {params}')
            data = requests.get(
                destinationURL, headers=self.apca_headers, params=params
            )
        except requests.exceptions.Timeout:
            # do something
            print(f'Error: Request has timed out. Please try again.')
        except requests.exceptions.TooManyRedirects:
            # URL bad, do something
            print(f'Error: The URL provided was not valid. Please try again.')
        except requests.exceptions.RequestException as err:
            print(f'Error: The program has experienced an unrecoverable error.')
            raise SystemExit(err)

        # print(f'RESPONSE: {data.text}')
        return json.loads(data.text)


consumer = Consumer()
