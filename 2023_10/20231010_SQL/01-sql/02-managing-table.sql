-- DROP TABLE examples;
CREATE TABLE examples(
  ExamId INTEGER PRIMARY KEY AUTOINCREMENT
  LastName VARCHAR(50) NOT NULL
  FirstName VARCHAR(50) NOT NULL
);

PRAGMA table_info('new_examples');

-- ALTER TABLE ADD COLUMN: 필드 추가
-- ALTER TABLE RENAME COLUMN: 필드 이름 변경
-- ALTER TABLE DROP COLUMN: 필드 삭제
-- ALTER TABLE RENAME TO: 테이블 이름 변경

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

-- 왜인지 오류가 납니다.
ALTER TABLE
  examples
DROP COLUMN
  PostCode;

ALTER TABLE
  examples
RENAME TO new_examples;
