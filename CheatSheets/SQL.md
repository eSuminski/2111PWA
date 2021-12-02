# SQL Cheat Sheet
## Common Data Types
Note: not all data types are suppported by every database. Check documentation to be sure.
- Numeric
    - BIT
    - TINYINT
    - BIGINT
    - DECIMAL
    - NUMERIC
    - FLOAT
    - REAL
- Date/Time
    - DATE
    - TIMESTAMP
    - DATETIME
    - TIME
    - YEAR
- Character/String
    - CHAR
    - NCHAR
    - VARCHAR
    - NVARCHAR
    - NTEXT
- Binary
    - BINARY
    - VARBINARY
    - IMAGE
- Miscellaneous
    - CLOB
    - BLOB
    - XML
    - JSON
## Sub Language Key Words
- Data Definition Language
    - create
    - alter
    - truncate
    - drop
- Data Manipulation Language
    - insert
    - update
    - delete
    - select
        - select is sometimes considered part of the Data Query Language sublanguage of SQL
- Data Control Language
    - create
    - grant
    - revoke
- Transaction Control Language
    - begin
    - end
        - commit also works
    - savepoint
        - can use the release keyword to remove savepoints
    - rollback
## Joins and Sets
- Join (place tables next to each other)
    - inner
    - left join
    - right join
    - full outer join
    - cross join
    - natural join
- Set (place columns on top of one another)
    - union
    - intersect