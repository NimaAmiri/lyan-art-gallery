import sqlite3

conn = sqlite3.connect('database.db')
db = conn.cursor()
db.execute(
    "CREATE TABLE IF NOT EXISTS art_works(id INTEGER PRIMARY KEY AUTOINCREMENT, title Text NOT NULL UNIQUE, image_id Text NOT NULL, created_year Text, description Text, image_url Text, artist Text , price Text)"
)
db.execute("delete from art_works")
db.execute("""
INSERT OR IGNORE INTO art_works Values
(NULL,'The Scream', 'the_scream', '1839', 'A painting of a young woman screaming in fear.',  'https://en.wikipedia.org/wiki/The_Scream',
'Edvard Munch', '€10.000,00'),
(NULL,'The Starry Night', 'the_starry_night', '1889', 'A painting of the starry night, painted by Vincent van Gogh.' , 'https://en.wikipedia.org/wiki/Starry_Night','Vincent van Gogh', '€15.000,00'),
(Null,'The Persistence of Memory',
 'the_persistence_of_memory', '1931',
'A painting of a man struggling to remember his past.', 'https://en.wikipedia.org/wiki/The_Persistence_of_Memory','Salvador Dali', '€20.000,00'),
(NULL, 'The Last Supper', 'the_last_supper', '1904', 'A painting of a crowd of people holding a ceremony.', 'https://en.wikipedia.org/wiki/Last_Supper', 'Leonardo da Vinci', '€25.000');
    """)
conn.commit()
#db.execute("delete from art_works")
WORKS = db.execute("SELECT * FROM art_works").fetchall()
conn.close()
print(WORKS)