import sqlite3
con = sqlite3.connect('history.db')
cur = con.cursor()

#  print all values of 'name' column
res = cur.execute('SELECT name FROM history')
print(res.fetchall())

# print name and year_start for all entries sorted by year_start
for row in cur.execute('SELECT year_start, name FROM history ORDER BY year_start'):
    print(row[0], row[1])
    
for row in cur.execute('SELECT name FROM history WHERE year_start<1900 ORDER by year_start'):
    print(row)
    
for row in cur.execute('SELECT * FROM history WHERE keywords LIKE "%america%" AND year_start<1870'):
    print('axis ->', row)


