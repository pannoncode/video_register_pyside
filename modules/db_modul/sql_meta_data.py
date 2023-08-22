create_table = """
create table if not exists data_register(
id serial primary key,
data_id varchar(50),
data_date date,
data_title varchar(100),
data_desc varchar(250),
data_link varchar(250)
)
"""

insert_data = """
insert into data_register(data_id, data_date, data_title, data_desc, data_link) 
values (:data_id, :data_date, :data_title, :data_desc, :data_link)
"""

select_all_data = """
select * from data_register
"""

delete_all_data = """
DELETE FROM data_register;
"""

delete_row = """
delete from data_register where id = '{id}'
"""

update_row = """
update data_register set data_id = '{serial}', data_date = '{date}', data_title = '{title}', data_desc = '{desc}', data_link = '{link}'
where id = '{id}'
"""
