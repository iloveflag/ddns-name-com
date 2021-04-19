# get your exist domain id
# curl -u 'username:token' 'https://api.name.com/v4/domains/example.org/records' 

from namecom import Auth, DnsApi
import socket
import time
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
id=   #must be
domainName='' #must be
host=''
username='' #must be
access_token='' #must be
auth = Auth(username, access_token)
api = DnsApi(domainName=domainName, auth=auth)
result = api.update_record(id=id, host=host,type='A', answer=local_ip,ttl=300)
print("update ok:"+host+domainName+"->"+local_ip+"\r"+"time:"+time.asctime(time.localtime(time.time())))

