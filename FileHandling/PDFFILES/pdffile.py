import csv

import PyPDF2
import re
def reading_pdf(filename):

    reader=PyPDF2.PdfReader(filename)
    page = reader.pages[0]

    text=page.extract_text()
    print(text)

    #Reading Specific data using RE
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    emails=re.findall(email_pattern,text)
    print(emails)

    #Writing emails into a csv file
    # Convert each email to a list
    each_emails = [[email] for email in emails]
    print(each_emails)
    with open('emails.csv','a',newline='') as csvfile:
        writer=csv.writer(csvfile,delimiter=',')
        writer.writerows(each_emails)


reading_pdf('sample.pdf')