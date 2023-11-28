import sqlite3

con = sqlite3.connect('history.db')
cur = con.cursor()
cur.execute('CREATE TABLE history(name, year_start, year_end, text, keywords)')

cur.execute("""
            INSERT INTO history VALUES
            ('american revolutionary war', 1775, 1783, 'recognizing the independence and sovereignty of the United States', 'war america revolution'),
            ('world war i', 1914, 1918, ' global conflict fought between two coalitions, the Allied Powers and the Central Powers', 'war allies europe'),
            ('american civil war', 1861, 1865, 'was a civil war in the United States between the Union and the Confederacy', 'war america slavery'),
            ('vietnam war', 1955, 1975, 'was a conflict in Vietnam, Laos, and Cambodia', 'war america communism cold_war')
            """)

con.commit()

