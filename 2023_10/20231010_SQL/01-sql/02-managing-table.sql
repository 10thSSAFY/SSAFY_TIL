CREATE TABLE examples (
  ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
  LastName VARCHAR(50) NOT NULL,
  FirstName VARCHAR(50) NOT NULL
);


ALTER TABLE
  examples
ADD COLUMN
  Country VARCHAR(100) NOT NULL default '';


ALTER TABLE
  examples
ADD COLUMN
  Age INTEGER NOT NULL default '';


ALTER TABLE
  examples
ADD COLUMN
  Address VARCHAR(100) NOT NULL default '';


ALTER TABLE
  examples
RENAME COLUMN
  Address TO PostCode;


-- ALTER TABLE
--   examples
-- DROP COLUMN PostCode;


PRAGMA table_info('examples');