''' A phone book / contacts app - Creating reading and writing functions '''

import json

def read_from_file():
    json_file = open('entries.json', 'r')
    entries = json.load(json_file)
    return entries
    json_file.close()

'''
def write_to_file():
    jsentries = read_from_file(entries)
    json_file = open('entries.json', 'w')
    json.dump(jsentries, json_file)
    json_file.close()
'''

def list_entries(entries):
    divider = '-'*40
    for email, info in entries.items():
        print(divider)
        print("Email: ", email)
        for key in info:
            print(key + ":", info[key])
        print(divider)

def spec_entry(entries):
    email = input("Which email address would you like to look up? ")
    for email_id, info in entries.items():
        if email == email_id:
            divider = '-'*40
            print(divider)
            print("Email: ", email)
            for key in info:
                print(key + ":", info[key])
            print(divider)
            break
    else:
        print("That email address is not in this phone book.")

def add_entry(entries):
    email = input("Email address: ")
    name = input("Name: ")
    phone = input("Phone: ")
    sec_email = input("Secondary email addresses: ")
    sec_phone = input("Secondary phone numbers: ")
    entries[email] = {"Name": name, "Phone": phone, "Secondary email addresses": sec_email, "Secondary phone numbers": sec_phone}
    json_file = open('entries.json', 'w')
    json.dump(entries, json_file)
    json_file.close()
    print("Success!")

def rm_entry():
    with open('entries.json') as f:
        entries = json.load(f)
        email = input("Which entry would you like to delete? (input e-mail address): ")
        for key in entries.keys():
            if email == key:
                del entries[key]
                print("Entry deleted.")
                break
        else:
            print("That email address is not in this phone book.")
    with open('entries.json', 'w') as f:
        entries = json.dump(entries, f)

while True:
    entries = read_from_file()
    print("What to do?", "1. List all entries", "2. Search by email address", "3. Add entry", "4. Remove entry", "5. Quit programme", sep="\n")
    choice = input("Choice: ")
    if choice == "1":
        list_entries(entries)
        continue
    elif choice == "2":
        spec_entry(entries)
        continue
    elif choice == "3":
        add_entry(entries)
        continue
    elif choice == "4":
        rm_entry()
        continue
    elif choice == "5":
        quit()
    else:
        print("I received invalid input. Please try again.")
        continue
