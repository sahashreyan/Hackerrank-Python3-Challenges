import whois

def is_reg(domain_name):
    try:
        w = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(w.domain_name)
    
domains = ["github.com","google.com","facbook.com","unknownrandomdomain.com"] #Include the list of domain names you want to check

for domain in domains:
    print(domain, "is registered" if is_reg(domain) else "is not registered")
    