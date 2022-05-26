import json
import jsonpickle

class RPA:

    def __init__(self, firstName, lastName, companyName, roleinCompany, address, email, phoneNumber):
        self.__name = firstName
        self.__lastname = lastName
        self.__company = companyName
        self.__rolecompany = roleinCompany
        self.__address = address
        self.__email = email
        self.__phoneNumber = phoneNumber


challange_1 = RPA ('John', 'Smith', 'IT Solutions', 'Analyst', '98 North Road', 'jsmith@itsolutions.co.uk',
                   '40716543298')
challange_2 = RPA ('Jane', 'Dorsey', 'MediCare', 'Medical Engineer', '11 Crown Street', 'jdorsey@mc.com', '40791345621')
challange_3 = RPA ('Albert', 'Kipling', 'Waterfront', 'Accountant', '22 Guild Street', 'kipling@waterfront.com',
                   '40735416854')
challange_4 = RPA ('Michael', 'Robertson', 'MediCare', 'IT Specialist', '17 Farburn Terrace', 'mrobertson@mc.com',
                   '40733652145')
challange_5 = RPA ('Doug', 'Derrick', 'Timepath Inc.', 'Analyst', '99 Shire Oak Road', 'dderrick@timepath.co.uk',
                   '40799885412')
challange_6 = RPA ('Jessie', 'Marlowe', 'Aperture Inc.', 'Scientist', '27 Cheshire Street', 'jmarlowe@aperture.us',
                   '40733154268')
challange_7 = RPA ('Stan', 'Hamm', 'Sugarwell', 'Advisor', '10 Dam Road', 'shamm@sugarwell.org', '40712462257')
challange_8 = RPA ('Michelle', 'Norton', 'Aperture Inc.', 'Scientist', '13 White Rabbit Street', 'mnorton@aperture.us',
                   '40731254562')
challange_9 = RPA ('Stacy', 'Shelby', 'TechDev', 'HR Manager', '19 Pineapple Boulevard', 'sshelby@techdev.com',
                   '40741785214')
challange_10 = RPA ('Lara', 'Palmer', 'Timepath Inc.', 'Programmer', '87 Orange Street', 'lpalmer@timepath.co.uk',
                    '40731653845')

list = []
list.append (challange_1)
list.append (challange_2)
list.append (challange_3)
list.append (challange_4)
list.append (challange_5)
list.append (challange_6)
list.append (challange_7)
list.append (challange_8)
list.append (challange_9)
list.append (challange_10)

with open ('challange.json', 'w') as arq:
    arq.write (jsonpickle.encode (list))