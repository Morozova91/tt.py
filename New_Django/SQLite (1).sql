CREATE TABLE IF NOT EXISTS New_table_author(
  id INTEGER PRIMARY KEY,
  Author TEXT,
  Title TEXT,
  Price INTEGER,
  Data TEXT);
  


INSERT INTO New_table_author(Author, Title, Price, Data) VALUES('Nabokov', 'Lolita', 153, '1948-1953'), 
                                                      ('Dostoevskiy', 'Idiot', 185, '1868');

SELECT * 
FROM New_table_author;