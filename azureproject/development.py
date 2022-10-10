from pathlib import Path
import os
import requests
import json


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

# azcli_id = "ce2f4037-2d29-4573-a286-cbd5fb528424"
# azid_url = "http://169.254.129.3:8081/msi/token?api-version=2019-08-01&resource=https%3A%2F%2Fmanagement.azure.com%2F&client_id="+azcli_id
# azid_hdr = "a62a33f4-3fa6-4bac-b302-79d5c405762b"
# hdrs = { "X-IDENTITY-HEADER" : azid_hdr }
# azres = requests.get(azid_url, headers=hdrs).json()
# az_tok = azres['access_token']
# print(az_tok)
# tok_url = "https://myvault.secretsvaultcloud.com/v1/token"
# cred = {'grant_type':'azure', 'provider':'azure', 'jwt': az_tok }
# response = requests.post(tok_url, data=cred)
# res = response.json()
# tok = res['accessToken']

# api_url = "https://myvault.secretsvaultcloud.com/v1/secrets/demo/db/postgres/dyna"
# headers =  {"Content-Type":"application/json", "Authorization": tok }
# response = requests.get(api_url, headers=headers)
# res = response.json()
# # res={'task': 'postgres', 'name': '', 'data': {'credentials': {'connectionURL': '172.17.0.2:5432/postgres?sslmode=prefer', 'password': 'cPGqATaC', 'username': 'usr_42cxh'}, 'grantPermissions': {'Type': '', 'what': 'ALL PRIVILEGES', 'where': 'ALL TABLES IN SCHEMA public'}, 'ttl': 1000}, 'success': True}
# print(res)
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
print(DATABASE_URI)

TIME_ZONE = 'UTC'

STATICFILES_DIRS = (str(BASE_DIR.joinpath('static')),)
STATIC_URL = 'static/'

