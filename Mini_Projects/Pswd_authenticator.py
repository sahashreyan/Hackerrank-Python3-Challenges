import getpass
database = {"shreyan.saha": "shreyan1234", "saha.shreyan": "abcd1234"}
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")
for i in database.keys():
    if username == 1:
        while password != database.get(1):
            password = getpass.getpass("Enter your password again: ")
        break
print("Verified")
    
