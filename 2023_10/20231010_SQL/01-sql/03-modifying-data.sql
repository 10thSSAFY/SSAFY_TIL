CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100) NOT NULL,
  content VARCHAR(200) NOT NULL,
  createdAT DATE NOT NULL
);

INSERT INTO
  articles(title, content, createdAT)
VALUES
  ('hello', 'world', '2000-01-01');

INSERT INTO
  articles(title, content, createdAT)
VALUES
  ('title1', 'content1', '1900-01-01'),
  ('title2', 'content2', '1800-01-01'),
  ('title3', 'content3', '1700-01-01');

INSERT INTO
  articles(title, content, createdAT)
VALUES
  ('mytitle', 'mycontent', DATE());

UPDATE
  articles
SET
  title = 'new title'
WHERE
  id=1;

UPDATE
  articles
SET
  title = 'update Title',
  content = 'update Content'
WHERE
  id = 2;

DELETE FROM
  articles
WHERE
  id = 1;

DELETE FROM
  articles
WHERE id IN (
    SELECT id FROM articles
    ORDER BY createdAt
    LIMIT 2
  );

DROP TABLE users;
DROP TABLE articles;

CREATE TABLE users(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) NOT NULL
);

CREATE TABLE articles(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(50) NOT NULL,
  content VARCHAR(100) NOT NULL,
  userId INTEGER NOT NULL,
  FOREIGN KEY (userId)
    REFERENCES users(id)
);

INSERT INTO users
  (name)
VALUES
  ('하석주'),
  ('송윤미'),
  ('유하선');

INSERT INTO articles
  (title, content, userId)
VALUES
  ('제목1', '내용1', 1),
  ('제목2', '내용2', 2),
  ('제목3', '내용3', 1),
  ('제목4', '내용4', 4),
  ('제목5', '내용5', 1);

SELECT * FROM articles
INNER JOIN users
  ON articles.userId = users.id;
-- WHERE userId = 1;

SELECT * FROM articles
INNER JOIN users
  ON articles.userId = users.id
WHERE users.name = '하석주';

SELECT * FROM articles
LEFT JOIN users
  ON articles.userId = users.id;

SELECT * FROM users
LEFT JOIN articles
  ON users.id = articles.userId
WHERE UserId is NULL;
