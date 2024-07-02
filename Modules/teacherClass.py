# Teacher Class

import json
import os
from errorHandler import NoMatchingIDError, NoMatchingNameError, AuthenticationError
class Teacher:
    def __init__(self, name, subject, ID, email, phone, address):
        self.name = name
        self.subject = subject
        self.ID = ID
        self.email = email
        self.phone = phone 
        self.address = address
    
    def emailcheck(self, email):
        not_allowed_symbols = ['!', '#', '$', '%', '&', "'", '*', '+', '/', '=', '?', '^', '_', '`', '{', '|', '}', '~']
        
        # Check for valid email format
        if self.email.count('@') != 1:
            return False
        
        # Check for disallowed symbols
        for symbol in not_allowed_symbols:
            if symbol in self.email:
                return False
        
        # Check for consecutive dots
        if '..' in self.email:
            return False
        
        # Split email into parts
        firstPart, secondPart = self.email.split('@')
            
        # Check if first and last characters of email parts are not '.'
        if len(firstPart) > 0 and len(secondPart) > 0:
            if firstPart[0] == '.' or secondPart[-1] == '.':
                return False
        
        return True
    
    def phonecheck(self, phone):
        # Check if phone number length is 10 and does not start with '0'
        if len(self.phone) == 10 and self.phone[0] != '0':
            return True
        else:
            return False

    def accept(self):
        # Validate email and phone number
        if not self.emailcheck(self.email) or not self.phonecheck(self.phone):
            return 'Re-enter teacher details: email or phone number is not valid'
        
        # Construct info dictionary
        info = {
            "name": self.name,
            "subject": self.subject,
            "ID": self.ID,
            "email": self.email,
            "phone": self.phone,
            "address": self.address
        }
        
        # Check if info already exists in JSON file
        if os.path.exists('teachers.json'):
            with open('teachers.json', 'r+') as file:
                try:
                    json_content = json.load(file)
                except json.JSONDecodeError:
                    json_content = []
                
                for record in json_content:
                    if record['email'] == self.email:
                        return 'Teacher details already exist.'
                
                json_content.append(info)
                file.seek(0)  # Move to the beginning to write updated content
                json.dump(json_content, file, indent=4)
        else:
            with open('teachers.json', 'w') as file:
                json.dump([info], file, indent=4)
        
        return 'Teacher details accepted and saved.'
    
    def display_all(self):
        if os.path.exists('teachers.json'):
            with open('teachers.json', 'r') as file:
                json_content = json.load(file)
                for record in json_content:
                    print(f'Name: {record['name']}\nEmail: {record["email"]}\nPhone: {record["phone"]}\n')
        else:
            print('No teacher records found.')
    
    def search(self):
        try:
            name = input('Enter student name: ')
            if os.path.exists('students.json'):
                with open('students.json', 'r+') as file:
                    json_content = json.load(file)
                    for record in json_content:
                        if record['name'] == name:
                            print(f'Name: {record["name"]}\nAge: {record["age"]}\nMarks: {record['marks']}\nGrade: {record["grade"]}\nAddress: {record["address"]}\nPhone no. {record["phone"]}')
                        else:
                            raise NoMatchingNameError(name)
                    return record
                
        except NoMatchingNameError as e:
            print(f'Error: {e.message}')
               
                  

        

    

                
                
            
        

                
                