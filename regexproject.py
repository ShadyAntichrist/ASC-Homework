#!/usr/bin/python

import re, xlwt, xlrd, csv, pandas, sqlite3, glob

con = sqlite3.connect("customer_forms")

curdb = con.cursor()

book = xlwt.Workbook()

sheet1 = book.add_sheet("Sheet 2")

sheet2 = book.add_sheet("Sheet 3")

phoneRegex = re.compile(r'''(
	(Phone\sNumber:)
	(\s)
	(\d{3}|\(\d{3}\))?
	(\s|-|\.)?		 #\s(white space)
	(\d{3})
	(\s|-|\.)
	(\d{4})
	(\s*(ext|x|ext.)\s*(\d{2,5}))?		#*(0 or more) ?(0 or 1)
	)''', re.X)
emailRegex = re.compile(r'''(
	(?<![*&#@$(){}\/])[a-zA-Z0-9._%+-]+            #+(1 or more)
	@
	[a-zA-Z0-9.-]+
	(\.[a-zA-Z]{2,4})
	)''', re.X)
firstNameRegex = re.compile(r'''(
	(First\sName:)
	(\s)
	([A-Za-z']+)				#Rest of name lowercase
	)''', re.X)
lastNameRegex = re.compile(r'''(
        (Last\sName:)
	(\s)
	([A-Za-z'-]+)
        )''', re.X)
courseNameRegex = re.compile(r'''(
        (Course\sName:)
	(\s)
	([A-Za-z ]+) 			 #Possible extra words
        )''', re.X)
areaCodeStateRegex = re.compile(r'''(
	([A-Z]{2})			#State Abbreviation
	(\s)+
	(\d{5})				#5 digit zip code
	)''', re.X)
downPaymentRegex = re.compile(r'''(
	(Down\sPayment:)
	(\s)
	(\$\d+)
	)''', re.X)

phoneNums = []
emails = []
firstNames = []
lastNames = []
downPayments = []
courseNames = []
address = []

for file in glob.glob('/root/Desktop/CustomerForms/CustomerForm[1-7].txt'):
	with open(file) as f:
		text = f.read()
	for groups in firstNameRegex.findall(text):
		firstNames.append(groups[3])
	for groups in lastNameRegex.findall(text):
		lastNames.append(groups[3])
	for groups in phoneRegex.findall(text):
        	phoneNum = '-'.join([groups[3], groups[5], groups[7]])
#        	if groups[8] != '':
#               	phoneNum += ' x' + groups[8]
        	phoneNums.append(phoneNum)
	for groups in emailRegex.findall(text):
        	emails.append(groups[0])
	for groups in courseNameRegex.findall(text):
		courseNames.append(groups[3])
	for groups in areaCodeStateRegex.findall(text):
                address.append(groups[0])
	for groups in downPaymentRegex.findall(text):
                downPayments.append(groups[3])

if len(phoneNums) > 0:
	sheet1.write(0, 0, "First_Name")
	sheet1.write(0, 1, "Last_Name")
	sheet1.write(0, 2, "Email")
	sheet1.write(0, 3, "Address")
	sheet1.write(0, 4, "Course_Name")
	sheet1.write(0, 5, "Phone")

	sheet2.write(0, 0, "First_Name")
	sheet2.write(0, 1, "Last_Name")
	sheet2.write(0, 2, "Course_Name")
	sheet2.write(0, 3, "Down_Payment")

	a = 1
	r = 1
	s = 1
	t = 1
	u = 1
	v = 1
	u = 1
	w = 1
	x = 1
	y = 1
	z = 1
	for name in firstNames:
		sheet1.write(v, 0, name)
		v += 1
	for name in lastNames:
		sheet1.write(u, 1, name)
		u += 1
	for email in emails:
                sheet1.write(w, 2, email)
                w += 1
	for item in address:
                sheet1.write(x, 3, item)
                x += 1
	for course in courseNames:
                sheet1.write(y, 4, course)
                y += 1
	for number in phoneNums:
		sheet1.write(z, 5, number)
		z += 1
	for name in firstNames:
       		sheet2.write(r, 0, name)
        	r += 1
	for name in lastNames:
		sheet2.write(s, 1, name)

		s += 1
	for course in courseNames:
		sheet2.write(t, 2, course)
		t += 1
	for payment in downPayments:
		sheet2.write(a, 3, payment)
		a += 1
	book.save("College_Forms.xls")

	with xlrd.open_workbook('College_Forms.xls') as wb:
		sh = wb.sheet_by_name("Sheet 2")
		with open('customer_info.csv', 'w+') as f:
			c = csv.writer(f)
			for r in range(sh.nrows):
				c.writerow(sh.row_values(r))

		sh2 = wb.sheet_by_name("Sheet 3")

		with open('accounts_recievable.csv', 'w+') as f:
			c = csv.writer(f)

			for r in range(sh2.nrows):
                                c.writerow(sh2.row_values(r))
	with open('customer_info.csv', 'r') as fin:
		dr = csv.DictReader(fin)
		to_db = [(i['First_Name'], i['Last_Name'], i['Email'], i['Address'], i['Course_Name'], i['Phone']) for i in dr]
	curdb.executemany("INSERT INTO customer_info VALUES (?,?,?,?,?,?);", to_db)
	con.commit()

	with open('accounts_recievable.csv', 'r') as fin:
                dr = csv.DictReader(fin)
                to_db = [(i['First_Name'], i['Last_Name'], i['Course_Name'], i['Down_Payment']) for i in dr]
	curdb.executemany("INSERT INTO accounts_recievable VALUES (?,?,?,?);", to_db)
	con.commit()

else:
	print("No phone numbers or email addresses were found.")
