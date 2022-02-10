from fpdf import FPDF
import json

with open ('resume.json') as f:
    data = json.load(f)

pdf = FPDF('P', 'mm', 'Letter')

pdf.add_page()

#Profile Part
pdf.set_font('Arial', 'B', 14)
pdf.cell(10,10, "Profile", ln= True)

for info in data['Profile']:
    firstName = info['First Name']  
    lastName = info['Last Name']
    name = "Name: " + firstName + " " + lastName
    age = "Age: " + info['Age']
    bday = "Birthday: " + info['Birthday']
    sex = "Sex: " + info['Sex']
    email = "E-mail: " + info['E-mail']
    contactnum = "Contact Number: " + info['Contact Number']

pdf.set_font('Arial', '', 12)
pdf.cell(10,8, txt=name, ln= True)
pdf.cell(10,8, txt=bday, ln= True)
pdf.cell(10,8, txt=age, ln= True)
pdf.cell(10,8, txt=sex, ln= True)
pdf.cell(10,8, txt=email, ln= True)
pdf.cell(10,8, txt=contactnum, ln= True)

#Experience Part
pdf.set_font('Arial', 'B', 14)
pdf.cell(10,10, "Experience", ln= True)

for info in data['Experience']:
    jobs = [
        info['Current Job'], info['First Job']
    ]
    job1 = jobs[0]

    for info in job1:
        occupation1 = "- " + info['Occupation']  + ":"
        company1 = info['Company']
        jobDescripA1 = "    * " + info['Job Description A']
        jobDescripB1 = "    * " + info['Job Description B']
        jobDescripC1 = "    * " + info['Job Description C']

    job2 = jobs[1]

    for info in job2:
        occupation2 = "- " + info['Occupation'] + ":"
        company2 = info['Company']
        jobDescripA2 = "    * " + info['Job Description A']
        jobDescripB2 = "    * " + info['Job Description B']
        jobDescripC2 = "    * " + info['Job Description C']

pdf.set_font('Arial', 'B', 12)
pdf.cell(43,10, txt=occupation1, ln= False)
pdf.set_font('Arial', '', 12)
pdf.cell(0,10, txt=company1, ln= True)
pdf.cell(0,8, txt=jobDescripA1, ln= True)
pdf.cell(0,8, txt=jobDescripB1, ln= True)
pdf.cell(0,8, txt=jobDescripC1, ln= True)

pdf.set_font('Arial', 'B', 12)
pdf.cell(57,10, txt=occupation2, ln= False)
pdf.set_font('Arial', '', 12)
pdf.cell(0,10, txt=company2, ln= True)
pdf.cell(0,8, txt=jobDescripA2, ln= True)
pdf.cell(0,8, txt=jobDescripB2, ln= True)
pdf.cell(0,8, txt=jobDescripC2, ln= True)

#Skills Part
pdf.set_font('Arial', 'B', 14)
pdf.cell(10,10, "Skills", ln= True)

for info in data['Skills']:
    skill1 = "    - " + info['First']
    skill2 = "    - " + info['Second']
    skill3 = "    - " + info['Third']
    skill4 = "    - " + info['Fourth']

pdf.set_font('Arial', '', 12)
pdf.cell(10,8, txt=skill1, ln= True)
pdf.cell(10,8, txt=skill2, ln= True)
pdf.cell(10,8, txt=skill3, ln= True)
pdf.cell(10,8, txt=skill4, ln= True)

#Hobbies Part
pdf.set_font('Arial', 'B', 14)
pdf.cell(10,10, "Hobbies", ln= True)

for info in data['Hobbies']:
    hobby1 = "    - " + info['First']
    hobby2 = "    - " + info['Second']
    hobby3 = "    - " + info['Third']
    hobby4 = "    - " + info['Fourth']

pdf.set_font('Arial', '', 12)
pdf.cell(10,8, txt=hobby1, ln= True)
pdf.cell(10,8, txt=hobby2, ln= True)
pdf.cell(10,8, txt=hobby3, ln= True)
pdf.cell(10,8, txt=hobby4, ln= True)

#Education Part
pdf.set_font('Arial', 'B', 14)
pdf.cell(10,10, "Education", ln= True)

for info in data['Education']:
    courses = [
        info['Second Diploma'], info['First Diploma']
    ]
    educ1 = courses[0]

    for info in educ1:
        course1 = " - " + info['Course'] + ": "
        school1 = info['School']

    educ2 = courses[1]

    for info in educ2:
        course2 = " - " + info['Course'] + ": "
        school2 = info['School']

pdf.set_font('Arial', 'B', 12)
pdf.cell(58,8, txt=course1, ln= False)
pdf.set_font('Arial', '', 12)
pdf.cell(0,8, txt=school1, ln= True)

pdf.set_font('Arial', 'B', 12)
pdf.cell(51,8, txt=course2, ln= False)
pdf.set_font('Arial', '', 12)
pdf.cell(0,8, txt=school2, ln= True)


pdf.output('Forrester_Samuel Gideon.pdf')


