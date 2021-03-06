import sqlite3

# The database will be created in the location where 'py' file is saved
conn = sqlite3.connect('loan_data.db')  
c = conn.cursor() 

# Create table - CLIENTS
c.execute('''CREATE TABLE loan_application ([loanid] INTEGER DEFAULT 1000 PRIMARY KEY AUTOINCREMENT, [name] TEXT, [email]	TEXT, [age] INTEGER, [gender] TEXT,[married] TEXT, [dependents] INTEGER, [education] INTEGER,[employment] INTEGER,[appincome] REAL,[coappincome] REAL, [loan_term] INTEGER,[loan_amount] REAL, [credit_history] INTEGER,[area] TEXT,[loan_status] INTEGER)''')
conn.commit()

print("loan_data created successfully")