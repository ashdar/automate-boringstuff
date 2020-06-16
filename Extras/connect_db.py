import pyodbc
cnxn = pyodbc.connect(r'Driver={SQL Server};Server=ARES\SQL2016;Database=master;Trusted_Connection=yes;')
cursor = cnxn.cursor()
cursor.execute("SELECT @@SERVERNAME WhereAmI, SUSER_SNAME() WhoAmI, GETDATE() 'RightNow'")
print("{: >20} {: >20} {: >40}".format("WhereAmI", 'WhoAmI', "RightNow"))
while 1:
    row = cursor.fetchone()
    if not row:
        break
    print("{: >20} {: >20} {: >40}".format(row.WhereAmI, row.WhoAmI, str(row.RightNow)))
    # print(row.WhereAmI, row.WhoAmI, row.RightNow)
cnxn.close()