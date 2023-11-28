import sqlite3

con = sqlite3.connect('history.db')
cur = con.cursor()

data = [
    ('spanish-american war', 1898, 1898, 'The main issue was Cuban independence. Revolts had been occurring for some years in Cuba against Spanish colonial rule', 'war cuba america spain independence'),
    ('french and indian war', 1754, 1763, 'The French and Indian War (1754-1763) was a theater of the Seven Years" War', 'war france native_americans america colonialism'),
    ('world war ii', 1939, 1945, "The vast majority of the world's countries, including all the great powers, fought as part of two opposing military alliances: the Allies and the Axis", 'war allies axis hitler churchill')
]

cur.executemany('INSERT INTO history VALUES (?, ?, ?, ?, ?)', data)
con.commit()