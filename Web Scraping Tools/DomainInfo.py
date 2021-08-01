import whois
import datetime as datetime

def is_reg(domain_name):
    try:
        w = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(w.domain_name)
    
domain_name = "google.com"

if is_reg(domain_name):
    whois_info = whois.whois(domain_name)

#print the company that manages the domain name
print("Domain registrar:", whois_info.registrar)

# print the WHOIS server
print("WHOIS server:", whois_info.whois_server)

 # get the creation time
print("Domain creation date:", whois_info.creation_date)

# get expiration date
print("Expiration date:", whois_info.expiration_date)

# print all other info
print(whois_info)
