import requests,zipfile,os,io
from io import StringIO
import asyncio
import aiohttp
import nest_asyncio

nest_asyncio.apply()


download_uris = [
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip'
]

path = 'downloads'


def create_directory():
# Check whether the specified path exists or not
    isExist = os.path.exists(path)

    if not isExist:
        # Create a new directory because it does not exist 
        os.makedirs(path)
        print("The new directory is created!")
    
async def getFiles():
    
    for url in download_uris:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:

                z = zipfile.ZipFile(io.BytesIO(await response.read()))
                if(os.path.exists(path)):
                    z.extractall(path)
                    
                else:
                    create_directory()
                    z.extractall(path)

loop = asyncio.get_event_loop()
loop.run_until_complete(getFiles())

