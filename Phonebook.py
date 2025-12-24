class Contact:

    phone_directory = []

    def __init__(self , name , phone_number):
        self.name = name
        self.phone_number = phone_number
        Contact.phone_directory.append(self)


    def show_contact(self):
        return f"Name: {self.name}\nPhone Number: {self.phone_number}"

    @classmethod
    def show_all_contact(cls):
        if(len(cls.phone_directory) == 0):
            print("No phone number in phone directory")
        else:
            for contact in cls.phone_directory:
                print(contact.show_contact())
    @classmethod
    def search_contact(cls, search_name):
        for contact in cls.phone_directory:
            if contact.name.lower() == search_name.lower():
                return contact.phone_number
        return None

    @staticmethod
    def validate_phone_number(number):
        if len(number) >= 8 and number.isdigit():
            return True
        else:
            return False
            
        #return f"{search_name} not found in phone directory"
n_contacts = int(input("How many contacts do you want add? "))

for i in range(n_contacts):
    name = input("Enter the name of the contact")
    phone_number = input("Enter the phone number")
    if Contact.validate_phone_number(phone_number):
        Contact(name, phone_number)
    else:
        print(f"Invalid phone number for {name} , phone number must be 8 digits and should only contain numbers in it")
"""
c1 = Contact("John",phone_number='1234567890')
c2 = Contact("Michael",phone_number='9234567890')
c3 = Contact("tom",phone_number='99934567890')
"""
#print(Contact.phone_directory)


#print(c1.show_contact())
#print(c2.show_contact())
#print(c3.show_contact())

Contact.show_all_contact()
#print(Contact.search_contact("john"))
#print(Contact.search_contact("Michael"))