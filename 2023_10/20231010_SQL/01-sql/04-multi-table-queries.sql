-- JOIN 둘 이상의 테이블에서 데이터를 검색하는 방법
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

INSERT INTO
  users(name)
VALUES
  ('하석주'),
  ('송윤미'),
  ('유하선');

INSERT INTO
  articles(title, content, userId)
VALUES
  ('제목1', '내용1', 1),
  ('제목2', '내용2', 2),
  ('제목3', '내용3', 1),
  ('제목4', '내용4', 4),
  ('제목5', '내용5', 1);

-- INNER JOIN 두 테이블에서 값이 일치하는 레코드에 대해서만 결과를 반환
SELECT * FROM articles
INNER JOIN users
  ON articles.userId = users.id;

SELECT articles.title, users.name
FROM articles
INNER JOIN users
  ON users.id = articles.userId
WHERE users.id = 1;

-- LEFT JOIN 오른쪽 테이블의 일치하는 레코드와 함께 왼쪽 테이블의 모든 레코드 반환
SELECT * FROM articles
LEFT JOIN users
  ON articles.userId = users.id;

SELECT *
FROM users
LEFT JOIN articles
  ON articles.userId = users.id
WHERE articles.userId IS NULL;
