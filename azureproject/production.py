import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

DEBUG = False
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
CSRF_TRUSTED_ORIGINS = ['https://'+ os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []

# Configure Postgres database; the full username for PostgreSQL flexible server is
# username (not @sever-name).
# DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
#     dbuser=os.environ['DBUSER'],
#     dbpass=os.environ['DBPASS'],
#     dbhost=os.environ['DBHOST'],
#     dbname=os.environ['DBNAME']
# )
# print(DATABASE_URI)

azcli_id = "ce2f4037-2d29-4573-a286-cbd5fb528424"
azid_url = "http://169.254.129.3:8081/msi/token?api-version=2019-08-01&resource=https%3A%2F%2Fmanagement.azure.com%2F&client_id="+azcli_id
azid_hdr = "a62a33f4-3fa6-4bac-b302-79d5c405762b"
hdrs = { "X-IDENTITY-HEADER" : azid_hdr }
azres = requests.get(azid_url, headers=hdrs).json()
az_tok = azres['access_token']
print(az_tok)
tok_url = "https://myvault.secretsvaultcloud.com/v1/token"
cred = {'grant_type':'azure', 'provider':'azure', 'jwt': az_tok }
response = requests.post(tok_url, data=cred)
res = response.json()
tok = res['accessToken']

api_url = "https://myvault.secretsvaultcloud.com/v1/secrets/demo/db/postgres/dyna"
headers =  {"Content-Type":"application/json", "Authorization": tok }
response = requests.get(api_url, headers=headers)
res = response.json()
print(res)
dbuser = res['data']['credentials']['username']
dbpass = res['data']['credentials']['password']
conurl = res['data']['credentials']['connectionURL']
dbhost = conurl.rpartition('?')[0].rpartition(':')[0]
dbname = conurl.rpartition('?')[0].rpartition('/')[2]
print(dbhost, dbname, dbuser, dbpass)

DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=res['data']['credentials']['username'],
    dbpass=res['data']['credentials']['password'],
    dbhost=conurl.rpartition('?')[0].rpartition(':')[0],
    dbname=conurl.rpartition('?')[0].rpartition('/')[2]
)
print(DATABASE_URI)


