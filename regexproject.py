#!/usr/bin/python

import re, xlwt

book = xlwt.Workbook()

sheet1 = book.add_sheet("Sheet 1")

phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?    #\d(0-9), {3}(3 times), |(or), \(escape () )
	(\s|-|\.)?	#\s(white space)
	(\d{3})
	(\s|-|\.)
	(\d{4})
	(\s*(ext|x|ext.)\s*(\d{2,5}))?		#*(0 or more) ?(0 or 1)
	)''', re.X)
emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+
	@
	[a-zA-Z0-9.-]+
	(\.[a-zA-Z]{2,4})
	)''', re.X)
with open('parse.txt') as f:
	text = f.read()

matches = []
phoneNums = []
emails = []

for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)
	phoneNums.append(phoneNum)
for groups in emailRegex.findall(text):
	matches.append(groups[0])
	emails.append(groups[0])
if len(matches) > 0:
	with open('phoneEmail.txt', 'a+') as file:
		for item in matches:
			file.write("%s\n" % item)
			file.close
	sheet1.write(0, 0, "PhoneNumbers:")
	sheet1.write(0, 1, "EmailAddresses:")
	x = 1
	y = 1
	for num in phoneNums:
		sheet1.write(x, 0, num)
		x += 1
	for email in emails:
		sheet1.write(y, 1, email)
		y += 1
	book.save("Phone_Email.xls")
else:
	print("No phone numbers or email addresses were found.")
