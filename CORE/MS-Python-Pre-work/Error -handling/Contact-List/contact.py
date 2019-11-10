import pyperclip
class Contact:
    '''
    Class generate new instances of contacts
    '''
    contact_list =[]#Empty contact list
    def __init__(self,first_name,last_name,phone_number,email):
        '''
        # _init_method that helps us define properties for our objects.

        Args:
        self.first_name=first_name
        self.last_name=last_ name
        self.phone_number =number
        self.email=email
        '''
       
        self.first_name=first_name
        self.last_name=last_name
        self.phone_number=phone_number
        self.email=email
        
    
    def save_contact(self):
        '''save_contact method saves contact objects into contact_list
        '''

        Contact.contact_list.append(self)    

    def delete_contact(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Contact.contact_list.remove(self)

    @classmethod
    def find_by_number(cls,number):
        '''
        is a method that takes in a number and display a contact that matches that number.
        
        Args:
           number:phone number to search for
        Returns:
           Contact of person that matches the number.
           '''

        for contact in cls.contact_list:
             if contact.phone_number == number:
                 return contact  

    @classmethod
    def contact_exist(cls,number):
        '''
        method checking if a contact exists from the contact list.
        Args:
          number:phone no to search if it exixts
        Return:
           Boolean :if True or False  depending if it exists
        '''
        for contact in cls.contact_list:
            if contact.phone_number == number:
                return True


        return False 

    @classmethod
    def display_contacts(cls):
        '''
        method that returns a contact list
        '''

        return cls.contact_list

    @classmethod
    def copy_email(cls,number):
        contact_found = Contact.find_by_number(number)
        pyperclip.copy(contact_found.email)



