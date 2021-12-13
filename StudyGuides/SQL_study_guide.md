## AWS RDS
Amazon Relational Database Service (Amazon RDS) is a web service that makes it easier to set up, operate, and scale a relational database in the AWS Cloud. It provides cost-efficient, resizable capacity for an industry-standard relational database and manages common database administration tasks.

AWS RDS automates many tasks:
- managing backups
- software patching
- auto failure detection
- recovery

AWS RDS offers different database types with varying combinations of CPU, memory, storage, and networking capacity . This gives you the flexibility to choose the appropriate mix of resources for your database.

AWS RDS offers multiple types of databases (Oracle, Postgre, etc) which are free to try. The model is "pay as you go"

RDS databases are useful when you need your data to be related (rows and columns) and when you need to link data between tables

Amazon offers different regions that house cloud computing resources, when you set up your AWS RDS you want to select a region close to your location. However, to make your instance fault tolerant, you will want to deploy multiple instances in multiple zones (zones are areas within a region)

There are multiple ways to interact with an AWS RDS:
- AWS Management Console
- AWS CLI
- AWS SDK (programatically)

AWS RDS is a managed service, so you have limited control over your database. Another option is yo use an EC2 and install a database on it. This gives you more control, but you lose the automatic management of your database.
## SQL 
Structured Query Language is tool for interacting with an SQL database. It allows you to create tables, manipulate them, create user rolls, and create some functionality in the database. Relational Databases are orginized in schemas
## Schemas
These are data structures that hold different tables within the database. They are used for organization.

## SQL Sub Languages
### Data Definition Language
These commands help set-up, alter, and drop tables in your database
```sql
--create allows us to make new tables. We define the columns and their types inside parenthesis
create table simple_table(
	first_name varchar(50),
	last_name varchar(50)
);

--alter lets us make changes to tables and their columns
alter table simple_table add column person_id serial;

--truncate will remove all the data within a table without deleting the table itself, as long as their are no constraint issues
truncate table simple_table;

--drop will delete a table and its data, as long as their are no constraint issues
drop table simple_table;

--these commands are not reversable: there is no option to do a rollback
```
### Data Manipulation Language
These are your CRUD (Create, Read, Update, Delete) operators
```sql
--insert is used to add data into a table
insert into names values(default, 'Eric', 'Suminski');

--update is used to change data in a table
update names set first_name = 'Sam' where person_id = 1;

--select is used to get data from a table. This is sometimes categorized under Data Query Language as a 5th sub language
select * from names where person_id = 1;

--delete is used to remove data from a table
delete from names where person_id = 1;
```
### Data Control Language
These commands manage users and their privliges on your database
```sql
--this creates a basic user with the name test with password test. Useful for allowing limited access
CREATE ROLE test NOSUPERUSER NOCREATEDB NOCREATEROLE NOINHERIT LOGIN PASSWORD 'test';

--this allows anyone who logs in as test to perform all actions on the given table
GRANT ALL ON TABLE names TO test;

--this removes all rights to perform actions on the table from test user
REVOKE ALL ON TABLE names FROM test;
```
### Transaction Control Language
These commands start, end, and perform rollbacks on transactions
```sql
begin;
	insert into names values(default, 'Luke', 'Suminski');
    --this creates a spot we can rollback to if needed
	savepoint my_savepoint;
	insert into names values(default, 'Sam', 'Suminski');
    --this will rollback the transaction to the save point, so we lose the Sam info
	rollback to savepoint my_savepoint;
    --this removes the savepoint, good pratice to release savepoints before ending your transactions
	release savepoint my_savepoint;
--this will commit the transaction, can also use commit
end;
```
## Constraints
Constraints are used to limit what can and can't be done with data inside a table. You should be familiar with the following constraints:
- Primary Key
    - marks a column as an identifier: it is a combination of the "unique" and "not null" constraints
- Foreign Key
    - makes the column reference a primary key on another table
- Not Null
    - the column must have a value
- Unique
    - the column must have a unique value within the table
- Check
    - ensures the column meets a determined condition (>0, for example)
- Default
    - lets you create a default value (automatically set with the serial data type)
```sql
create table names(
	person_id serial primary key,-- this is now required to be not null and unique
	first_name varchar(10),
	last_name varchar(10)
);
create table foreign_key_example(
	foreign_key_example_id serial,
	foreign_key int,
    --this makes it so our foreign_key column references the person_id column. Any entries to this table MUST reference someone on the names table
	constraint my_foreign_key foreign key(foreign_key) references names(person_id)
);
create table second_foreign_key_example(
	foreign_key_example_id serial,
	foreign_key int references names(person_id) -- can also make a foreign key this way
);
```
## Functions
There are two kinds of functions in SQL: aggregate and scalar. Aggregate functions work on groups of data, whereas scalar functions work on single pieces of data.

Some common Aggregate functions:
```sql
-- sum(): returns the sum of values in a group of data
select sum(person_id) from names;
-- min(): returns the smallest value in group of data
select min(person_id) from names;
-- max(): returns the largest value in a group of data
select max(person_id) from names;
-- count(): returns the number of rows of data in the group
select count(person_id) from names;
-- avg(): returns the average in a group of data
select avg(person_id) from names;
```

Some common scalar functions:
```sql
--now(): returns the current date and time
select now();
--upper(): returns the string value in all uppercase
select upper(first_name) from names where person_id = 1; 
--lower(): returns the string value in all lowercase
select lower(first_name) from names where person_id = 1;
--length(): returns the length of the value
select length(first_name) from names where person_id = 1;
--round(): takes two arguments, the first is the value to round, the second optional one is the acceptable number of decimal places
select round(person_id, 2) from names where first_name = 'Eric';
```
You can also create your own custom functions in a postgres database
```sql
-- this line creates a new function called addition if there is not one, replaces it if there is. Think of the $$ symbols as {}.
create or replace function addition( num1 int, num2 int) returns int as $$
	-- any local variables need to be declared at the top of the function
	declare
		total int;
	-- actual logic of the function goes between a begin and end statement
	begin
		total = num1 + num2;
		-- make sure to return a value
		return total;
	end
-- you have to declare the language you use to make the function
$$ LANGUAGE plpgsql;

-- this line adds the two inputs together and returns the result. Must be ints or there is an error
select addition(5,5);
```
## Joins
Joins allow you to combine table data by putting their columns next to each other to view their data together. There are many different joins you can use
```sql
create table team(
	team_id serial primary key,
	team_name varchar(50)
);

create table player(
	player_id serial primary key,
	team_id int,
	player_name varchar(50),
	constraint team_fk foreign key(team_id) references team(team_id)
);
-- this will return the data ordered by what team the player is on. It will match the player to their team, and contains all data
select * from player inner join team on team.team_id = player.team_id order by player.team_id ;

```
the outter joins are left, full outer, and right join
```sql
-- this left join returns all data in the team (left) table and any matching records in the player table
select * from team left join player on team.team_id = player.team_id ;

-- this right join returns all the data in the player(right) table and any matching records in the team table
select * from team right join player on team.team_id = player.team_id ;

-- this full outer join returns all data in both the team and player tables
select * from team full outer join player on team.team_id = player.team_id ;
```
think of the cross join as showing possibility (cartesian product)
```sql
--all players will be matched with all teams
select * from team cross join player ;
```
the natural join combines columns with the same name, quick and easy, but sometimes it will return no data. Use sparingly, if at all.
```sql
select * from team natural join player ;
```
## Set Operations
sets allow you to stack tables on top of each other, but this requires columns with the same names to be selected.
```sql
-- returns all id values without any duplicates (make union all to allow duplicates)
select team.team_id from team union select player.team_id from player;

-- this will only return those team_ids that have a player assigned to them
select team_id from team intersect select team_id from player;
```
## Referential Integrity
This is the idea that we should have no orphaned records. If an entry has a foreign key, it NEEDS to reference an existing record. If the primary record is deleted then the foreign record needs to have a response. This response could be to self delete, or even to stop the parent record from being deleted. It is important to maintain referential integrity because there can be serious real-world consequences for having orphaned records (whose bank account is this? Who made this purchase? Whose Social Security Number is this?) You have a few common options to enforce referential integrity:
- on delete cascade: deletes the data that has a foreign relationship to the primary data
- on delete restrict: prevents the primary data from being deleted
- on delete update: allow the foreign key to update, but if it breaks referential integrity the whole transaction will fail
## Multiplicity
This describes the relationship between tables. There are three ways tables can relate:
- one-to-one: only one entity in a table references another
```sql
create table person(
	person_id serial primary key
);

create table brain(
	brain_id serial primary key,
	person_id int unique, --notice the unique constraint: only one brain can be attached to a person
	constraint brain_fk foreign key (person_id) references person(person_id)
);
```
- one-to-many (or many-to-one): many entities in a table can reference one other entity in the other table
```sql
create table team(
	team_id serial primary key
);

create table player(
	player_id serial primary key,
	team_id int, --many players can have the same team id, since they play on the same team
	constraint player_fk foreign key(team_id) references team(team_id)
);
```
- many-to-many: many entities in a table can reference many other entities in another table. Because a direct link can not be established between the two (think teachers and students: many teachers can have many students, and many students can have many teachers) you need to create a junction table (sometimes called a join table).
```sql
create table teacher(
	teacher_id serial primary key
);

create table student(
	student_id serial primary key
);
--notice there are no foreign keys in the student or teacher tables: their relationship is handled by the join table classroom
create table teacher_student_join(
	join_id serial primary key,
	teacher_id int,
	student_id int,
	constraint teacher_fk foreign key(teacher_id) references teacher(teacher_id),
	constraint student_fk foreign key(student_id) references student(student_id)
);
```
## Normalization
Normalization is a way of organizing tables, with higher levels enforcing stricter requirements. You should be familiar with the first three levels of normalization
```sql
--there is no normalization happening here
create table not_1nf(
	first_and_last_name varchar(50),
);
--if there is at least one primary key, and all columns are atomic, then the table is 1NF
create table first_nf(
	person_id serial primary key,
	job varchar(50) primary key,
	first_name varchar(50),
	last_name varchar(50),
	job_title varchar(50)
);
--if 1NF constraints are followed, and the composite key is removed so all columns reference a single primary key, you have 2NF
create table second_nf(
	person_id serial primary key,
	first_name varchar(50),
	last_name varchar(50)
);
--this is 2NF, but the total cost column is unneccessary, since we could get it from items purchased and item price. It is considered a transitive property
create table not_third_nf(
	order_id serial primary key,
	item varchar(50),
	items_purchased int,
	item_price decimal,
	total_cost decimal
);
--this is 3NF: it conforms to 2NF and it has no transitive properties
create table third_nf(
	order_id serial primary key,
	item varchar(50),
	items_purchased int,
	item_price decimal
);
```
## ACID
Any DML actions before a commit are called transactions. Every transaction should have the ACID properties
- Atomicity
    - all transactions must succeed for a commit to happen. If any fail, there is no commit
- Consistency
    - all transactions must enforce existing constraints
- Isolation
    - multiple concurent transactions should not interfere with one another
- Durability
    - committed transactions should be persisted, even if there is some catastrophic failure (power outage, system, crash, etc).
## Connecting to Postgres Database with Python
1. pip install psycopg[binary]
2. create a module to hold your connection object
3. create a method that returns a connection object or raises an Operational Error
```python
from psycopg import connect, OperationalError
# we are using environment variables with Pycharm to hide our login credentials. Need to import os to access them
import os

def create_connection():
    try:
        # use these keyword arguments to apply your login credentials
        conn = connect(
            host=os.environ.get("HOST"),
            dbname=os.environ.get("DB"),
            user=os.environ.get("USER"),
            password=os.environ.get("PASSWORD"),
            port=os.environ.get("PORT")
        )
        # return your connection object
        return conn
    # this exception will be raised if you can't connect to your database
    except OperationalError as e:
        print(str(e))

# you can import this connection object into your DAO objects so they can access your database
connection = create_connection()

# you can use a print statement to make sure your connection object is being created successfully
print(connection)
```
4. import your connection object where it is needed in your Data Access Layer
```python
from data_access_layer.abstract_classes.player_dao import PlayerDAO
# this is the connection object we made above
from util.database_connection import connection
from entities.players import Player


class PlayerPostgresDAO(PlayerDAO):
    def create_player_entry(self, player: Player) -> Player:
        # we will use %s as placeholders for our values
        sql = "insert into player values(%s, %s, %s, default, %s) returning player_id"
        cursor = connection.cursor()
        # we pass in our sql to the cursor's execute method, and inside a tuple we then pass in the
        # values for the insert command
        cursor.execute(sql, (player.first_name, player.last_name, player.jersey_number, player.team_id))
        # only need commit for insert, update, and delete DML statements. This ends the transaction, which persists our changes
        connection.commit()
        player_id = cursor.fetchone()[0]
        player.player_id = player_id
        return player
```
## Data Access Object
Data Access Objects (DAO) are code that directly interact with our database. This helps keep our code modular, which makes for less sphagetti code (hard to read) and helps make debugging easier (seeing an exception raised in a DAO method tells you exactly where to start looking: your DAO object). 
1. To create a DAO first you design an interface (Abstract class in Python) that has all the methods you will use to query the database
```python
from abc import ABC, abstractmethod
# taken from our in class example
from entities.players import Player

# notice I have included all the basic CRUD operations in this abstract class
class PlayerDAO(ABC):

    # create player method
    @abstractmethod
    def create_player_entry(self, player: Player) -> Player:
        pass

    # get player information
    @abstractmethod
    def get_player_information(self, player_id: int) -> Player:
        pass

    # get all player information
    @abstractmethod
    def get_all_players_information(self) -> list[Player]:
        pass

    # update player information
    @abstractmethod
    def update_player_information(self, player: Player) -> Player:
        pass

    # delete player information
    @abstractmethod
    def delete_player_information(self, player_id: int) -> bool:
        pass
```
2. Once your interface is finished you can create an implementation class for the specific database you are working with
```python
from data_access_layer.abstract_classes.player_dao import PlayerDAO
from util.database_connection import connection
from entities.players import Player


class PlayerPostgresDAO(PlayerDAO):
    def create_player_entry(self, player: Player) -> Player:
        # we will use %s as placeholders for our values
        sql = "insert into player values(%s, %s, %s, default, %s) returning player_id"
        cursor = connection.cursor()
        # we pass in our sql to the cursor's execute method, and inside a tuple we then pass in the
        # values for the insert command
        cursor.execute(sql, (player.first_name, player.last_name, player.jersey_number, player.team_id))
        connection.commit()
        player_id = cursor.fetchone()[0]
        player.player_id = player_id
        return player

    def get_player_information(self, player_id: int) -> Player:
        sql = "select * from player where player_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [player_id])
        player_record = cursor.fetchone()
        player = Player(*player_record)
        return player

# so on and so forth
```
3. we now have a Data Access Object that is ready to query our database. If we need to switch databases, all we need to do is create a new implementation class for the new location: our interface (Abstract class in Python) is still valid. This is the benefit of using the DAO design pattern.