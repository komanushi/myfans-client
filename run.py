import os
from myfans_client.client import MyFansClient

client = MyFansClient(
    email=os.environ['MYFANS_EMAIL'],
    password=os.environ['MYFANS_PASSWORD'],
    debug=True
)
