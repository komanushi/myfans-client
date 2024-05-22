import os
from myfans_client.client import MyFansClient

client = MyFansClient(
    email=os.environ['MYFANS_EMAIL'],
    password=os.environ['MYFANS_PASSWORD'],
    debug=True
)

# b402b98e-b3f1-491b-b572-341b7a17dc7f
for row in client.get_follows(
    user_id='b402b98e-b3f1-491b-b572-341b7a17dc7f',
    start_page=1,
    max_page=2
):
    print(row)

for row in client.get_followed(
    user_id='b402b98e-b3f1-491b-b572-341b7a17dc7f',
    start_page=1,
    max_page=2
):
    print(row)
