#encoding: utf-8 
#imports
import OpenSSL
import ssl, socket
import argparse
from datetime import datetime
import pytz

#argument(domain)
parser = argparse.ArgumentParser()
parser.add_argument("domain")
args = parser.parse_args()
domain = args.domain

#Checks server SSL certificate for expiry.
cert = ssl.get_server_certificate(
(domain, 443), ssl_version=ssl.PROTOCOL_TLSv1)
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
x509info = x509.get_notAfter()

# Date format
num_days = 7
exp_day = x509info[6:8].decode('utf-8')
exp_month = x509info[4:6].decode('utf-8')
exp_year = x509info[:4].decode('utf-8')

exp_date = str(exp_day) + ' '+ str(exp_month) + ' ' + str(exp_year)
expire_date = datetime.strptime(exp_date, "%d %m %Y")

#Outputs
print("SSL Certificate for", domain, "will be expired on", exp_date  )
expire_in = expire_date - datetime.now()
expire_in = str(expire_in).split(' ')[0] 
if  expire_in <= 0:
    print("SSL Certificate for", domain, "is allready expired")
else:
    print("SSL Certification for", domain , "will expire",expire_in,"days later") 


