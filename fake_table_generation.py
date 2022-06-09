import random as r
import datetime as dt
from datetime import date as d
from prettytable import PrettyTable

# table row count definition
row_count = 1000

# date restrictions from 1st of January 2022 till Today
r_start_date = dt.date(2022,1,1)
r_end_date = d.today()
delta_days = r_end_date - r_start_date
delta_days = delta_days.days # days between date range

# email category names
email_subject_group = ['Purchase','Spam','Friend']

# prettify fake data table
table = PrettyTable()
table.title = 'Fake Data'
table.field_names = ['ID', 'Email Subject', 'Email Date']


# one loop where each row have random date and email subject element
# after generation added to the table 'Fake Data'
for i in range(row_count):
    random_date = r_start_date + dt.timedelta(days = r.randrange(delta_days)) # add random number of days to 1st of January
    random_date = random_date.isoformat() # format date to isformat which is %Y-%m-%d
# Email subject with random number in the end, number is in the range of 1 to delta_days
    random_email_subject = 'Email Subject' + ' ' + r.choice(email_subject_group) + ' ' + str(r.randrange(delta_days))
    table.add_row([i + 1,random_email_subject,random_date]) # adding new row with new values to the table

print(table)