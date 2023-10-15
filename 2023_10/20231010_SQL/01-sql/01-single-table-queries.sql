-- 01. Querying data
SELECT
  LastName
FROM
  employees;

SELECT
  LastName, FirstName
FROM
  employees;

SELECT
  *
FROM
  employees;

SELECT
  FirstName AS '이름'
FROM
  employees;

SELECT
  Name, Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks;

-- 02. Sorting data
  -- ORDER BY 조회 결과의 레코드를 결정
SELECT
  FirstName
FROM
  employees
ORDER BY
  FirstName;

SELECT
  FirstName
FROM
  employees
ORDER BY
  FirstName DESC;

SELECT
  Country, City
FROM
  customers
ORDER BY
  Country DESC, City;

SELECT
  Name, Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks
ORDER BY
  Milliseconds DESC;

-- NULL 정렬 예시


-- 03. Filtering data
  -- DISTINCT 조회 결과에서 중복된 레코드를 제거
SELECT
  Country
From
  customers
ORDER BY
  Country;

SELECT DISTINCT
  Country
From
  customers
ORDER BY
  Country;

  -- WHERE 조회 시 특정 검색 조건을 지정
SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  City = 'Prague';

SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  City != 'Prague';

SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL
  AND Country = 'USA';

SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL
  OR Country = 'USA';

SELECT
  Name, Bytes
From
  tracks
WHERE
  Bytes BETWEEN 100000 AND 500000;

SELECT
  Name, Bytes
From
  tracks
WHERE
  Bytes BETWEEN 100000 AND 500000
ORDER BY Bytes;

SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE
  Country in ('Canada', 'Germany', 'France');

SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE
  Country not in ('Canada', 'Germany', 'France');

SELECT
  LastName, FirstName
FROM
  customers
WHERE
  LastName LIKE '%son';

SELECT
  LastName, FirstName
FROM
  customers
WHERE
  FirstName LIKE '___a';

-- 04. Grouping data
SELECT
  Country
FROM
  customers
GROUP BY
  Country;

SELECT
  Country, COUNT(*)
FROM
  customers
GROUP BY
  Country;

SELECT
  Composer,
  AVG(Bytes)
FROM
  tracks
GROUP BY
  Composer
ORDER BY
  AVG(Bytes) DESC;

SELECT
  Composer,
  AVG(Bytes) AS avgOfBytes
FROM
  tracks
GROUP BY
  Composer
ORDER BY
  avgOfBytes DESC;


-- 에러
SELECT
  Composer,
  AVG(Milliseconds / 60000) AS avgOfMinute
FROM
  tracks
WHERE
  avgOfMinute < 10
GROUP BY
  Composer;

-- 에러 해결
SELECT
  Composer,
  AVG(Milliseconds / 60000) AS avgOfMinute
FROM
  tracks
GROUP BY
  Composer
HAVING
  avgOfMinute < 10;