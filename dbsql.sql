create table user(userid integer primary key autoincrement,username text not null,password text not null,email text not null,gender text check(gender  in ('male', 'female')),
    create_at timestamp default CURRENT_TIMESTAMP
);

