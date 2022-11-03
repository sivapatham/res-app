from pathlib import Path
import os
import requests


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = False
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
CSRF_TRUSTED_ORIGINS = ['https://'+ os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []


# tok_url = "https://myvault.secretsvaultcloud.com/v1/token"
# cred = {'grant_type':'password', 'username':'', 'password':'', 'provider':'thy-one'}
# response = requests.post(tok_url, data=cred)
# res = response.json()
# tok = res['accessToken']

# api_url = "https://myvault.secretsvaultcloud.com/v1/secrets/demo/db/postgres/dyna"
# headers =  {"Content-Type":"application/json", "Authorization": tok }
# response = requests.get(api_url, headers=headers)
# #print(response.json())
# res = response.json()
# dbuser = res['data']['credentials']['username']
# dbpass = res['data']['credentials']['password']
# conurl = res['data']['credentials']['connectionURL']
# dbhost = conurl.rpartition('?')[0].rpartition(':')[0]
# dbname = conurl.rpartition('?')[0].rpartition('/')[2]
# print(dbhost, dbname, dbuser, dbpass)

# DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
#     dbuser=res['data']['credentials']['username'],
#     dbpass=res['data']['credentials']['password'],
#     dbhost=conurl.rpartition('?')[0].rpartition(':')[0],
#     dbname=conurl.rpartition('?')[0].rpartition('/')[2]
# )
# print(DATABASE_URI)

DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
   dbuser=os.environ['DBUSER'],
   dbpass=os.environ['DBPASS'],
   dbhost=os.environ['DBHOST'],
   dbname=os.environ['DBNAME']
)

TIME_ZONE = 'UTC'

STATICFILES_DIRS = (str(BASE_DIR.joinpath('static')),)
STATIC_URL = 'static/'

