import csv


def write_contacts_to_file(filename, contacts):
    with open(filename, "w", newline = '', encoding="utf-8") as file:
        fieldnames = contacts[0].keys()
        writer = csv.DictWriter(file, delimiter = ",", fieldnames = fieldnames)
        writer.writeheader()
        for row in contacts:
            writer.writerow(row)
    

def read_contacts_from_file(filename):
    with open(filename, "r", newline = '', encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=",")
        contacts = []
        header = next(reader)
        for row in reader:
            if row[3] == "False": 
                row[3] = False 
            else: row[3] = True
            contacts.append(dict(zip(header, row)))
        return contacts


        
if __name__=="__main__":

    a = [   
            {'name': 'Allen Raymond', 
            'email': 'nulla.ante@vestibul.co.uk', 
            'phone': '(992) 914-3792', 
            'favorite': False}, 
            {'name': 'Chaim Lewis', 
            'email': 'dui.in@egetlacus.ca', 
            'phone': '(294) 840-6685', 
            'favorite': False}, 
            {'name': 'Kennedy Lane', 
            'email': 'mattis.Cras@nonenimMauris.net', 
            'phone': '(542) 451-7038', 
            'favorite': True}, 
            {'name': 'Wylie Pope', 
            'email': 'est@utquamvel.net', 
            'phone': '(692) 802-2949', 
            'favorite': False}, 
            {'name': 'Cyrus Jackson', 
            'email': 'nibh@semsempererat.com', 
            'phone': '(501) 472-5218', 
            'favorite': True}
        ]
    write_contacts_to_file("list.csv", a)
    print(read_contacts_from_file("list.csv"))
