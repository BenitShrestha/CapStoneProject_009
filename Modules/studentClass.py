# Student Class

from teacherClass import Teacher
from errorHandler import NoMatchingIDError, NoMatchingNameError, AuthenticationError
import json 
import os 

class Student(Teacher):
    def __init__(self, name, age, roll_number, email, phone, marks, address):
        # super.__init__(name, '', roll_number, email, phone, address)
        self.name = name
        self.age = age
        self.roll_number = roll_number
        self.email = email
        self.phone = phone
        self.address = address
        self.marks = marks
     
    def accept(self):
        
        # Validate email and phone number
        # if not super().emailcheck(self.email) or not super().phonecheck(self.phone):
        #     return 'Re-enter student details: email or phone number is not valid'
        
        # Construct info dictionary
        info = {
            "name": self.name,
            "age": self.age,
            "roll_number": self.roll_number,
            "email": self.email,
            "phone": self.phone,
            "marks": self.marks,
            "address": self.address
        }
        
        # Check if info already exists in JSON file
        if os.path.exists('students.json'):
            with open('students.json', 'r+') as file:
                try:
                    json_content = json.load(file)
                except json.JSONDecodeError:
                    json_content = []
                
                for record in json_content:
                    if record['email'] == self.email:
                        return 'Student details already exist.'
                    
                json_content.append(info)
                file.seek(0)  # Move to the beginning to write updated content
                json.dump(json_content, file, indent=4)
                
        else:
            with open('students.json', 'w') as file:
                json.dump(info, file, indent=4)
        
        return 'Student details accepted and saved.'

    def display_all(self):
        if os.path.exists('students.json'):
            with open('students.json', 'r') as file:
                json_content = json.load(file)
                for record in json_content:
                        print(f'Name: {record["name"]}\nAge: {record["age"]}\nMarks: {record["marks"]}\nGrade: {record["grade"]}\nAddress: {record["address"]}\nPhone no. {record["phone"]}\n')   
        else:
            print('No student records found.')
            
    def rank(self):
        if os.path.exists('students.json'):
            with open('students.json', 'r') as file:
                json_content = json.load(file)
                rank_list = {
                    record['name']: sum(record['marks'].values())
                    for record in json_content
                }
            sorted_rank_list = dict(sorted(rank_list.items(), key=lambda item: item[1], reverse=True))
            return sorted_rank_list
                          
    def search(self):
        student_search = super().search()
        for keys, value in student_search.items():
            if keys == 'marks':
                sum = 0
                min_marks = 100
                max_marks = 0
                for sub, num in value.items():
                    if num>max_marks:
                        max_marks = num
                        max_sub = sub
                    if num<min_marks:
                        min_marks = num
                        min_sub = sub
                    sum += num
                percentage = round(sum/2, 2)
                if percentage > 40:
                    print(f'{student_search["name"]}, You have passed')
                    print(f'You got {percentage}%')
                    rank_list = self.rank()
                    rnk = 1
                    for rank in rank_list.items():
                        if student_search['name'] != rank[0]:
                            rnk += 1
                        else:
                            print(f'{student_search['name']} has ranked {rnk}')
                else:
                    print(f'{student_search["name"]}, You have failed')
                print(f'Highest score: {max_marks} in {max_sub} and Lowest score: {min_marks} in {min_sub}')
    
    def get_student(self):
        students = {}
        students['name'] = input('Enter name: ')
        students['age'] = input('Enter age: ')
        students['grade'] = input('Enter grade: ')
        students['roll_number'] = input('Enter roll_number: ')
        students['email'] = input('Enter email: ')
        students['phone'] = input('Enter phone: ')

        marks = {}
        marks['maths'] = int(input('Enter marks for maths: '))
        marks['science'] = int(input('Enter marks for science: '))
        students['marks'] = marks
        students['address'] = input('Enter address: ')
    
        return students

    def get_teacher(self):
        teacher = {}
        teacher['name'] = input("Enter name: ")
        teacher['subject'] = input("Enter subject: ")
        teacher['ID'] = input("Enter ID: ")
        teacher['email'] = input("Enter email: ")
        teacher['phone'] = input("Enter phone: ")
        teacher['address'] = input("Enter address: ")
        
        return teacher
           
    def add_entries_std(self):
        flag = False
        print('Enter the new details: ')
        students = self.get_student()
        
        with open('students.json', 'r') as file:
            try:
                json_content = json.load(file)
            except json.JSONDecodeError:
                json_content = []

            for record in json_content:
                if 'roll_number' in record and record['roll_number'] == students['roll_number']:
                    print('Entry already exists')
                    flag = True
                    break

            if not flag:
                json_content.append(students)
                with open('students.json', 'w') as file:
                    json.dump(json_content, file, indent=4)
                    print('Entry Saved')
                    
    def add_entries_teach(self):
        flag = False
        print('Enter the new details: ')
        teachers = self.get_teacher()
        
        with open('teachers.json', 'r') as file:
            try:
                json_content = json.load(file)
            except json.JSONDecodeError:
                json_content = []

            for record in json_content:
                if 'ID' in record and record['ID'] == teachers['ID']:
                    print('Entry already exists')
                    flag = True
                    break

            if not flag:
                json_content.append(teachers)
                with open('teachers.json', 'w') as file:
                    json.dump(json_content, file, indent=4)
                    print('Entry Saved')
            
    def authentication(self):
        flag = False
        try:
            print("Verify yourself to add new entries: ")
            name = input('Enter your name: ')
            ID = input('Enter your ID: ')
            if os.path.exists('teachers.json'):
                with open('teachers.json', 'r') as file:
                    json_content = json.load(file)
                    for record in json_content:
                        if record['name'] == name and record['ID'] == ID:
                            flag = True 
                            print('Verification Completed')
                            opt =  3
                            while(opt != 0):
                                opt = int(input('1: Teacher Entry\t2: Student Entry\t0: Exit:\n'))
                                if opt == 1:
                                    self.add_entries_teach()
                                if opt == 2:
                                    self.add_entries_std()
                                if opt == 0:
                                    break
                        else:
                            raise NoMatchingIDError(ID)

            else:
                raise AuthenticationError()
            
        except NoMatchingIDError as e:
            print(f'Error: {e.message}')
            
        except AuthenticationError as e:
            print(f'Error: {e.message}')
                       
        if not flag:
            print('Verification Failed, Try Again')

def marks_upload():
    dic = {
        'maths' : 0,
        'science' : 0
    }
    for key, value in dic.items():
        marks = input(f'Enter marks for {key}: ')
        dic[key] = marks
    return dic