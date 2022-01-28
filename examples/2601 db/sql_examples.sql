create table books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name varchar,
    author varchar
);

-- delete table
drop table books;

-- select
select * from books where author='lev tolstoi';
select name, id from books;
select * from books;


-- delete record
delete from books where id=2;

-- update record
update books
set author='Lev Tolstoi'
where author='lev tolstoi'



-- insert
insert into books (name, author)
values ('war and peace', 'lev tolstoi');

insert into books (name, author)
values ('1984', 'George Oruell');