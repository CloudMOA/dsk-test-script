
create database if not exists tpcc;

create table if not exists tpcc.warehouse (
w_id int not null,
w_name varchar(10),
w_street_1 varchar(20),
w_street_2 varchar(20),
w_city varchar(20),
w_state char(2),
w_zip char(9),
w_tax decimal(4,2),
w_ytd decimal(12,2),
primary key (w_id) );

create table if not exists tpcc.district (
d_id int not null,
d_w_id int not null,
d_name varchar(10),
d_street_1 varchar(20),
d_street_2 varchar(20),
d_city varchar(20),
d_state char(2),
d_zip char(9),
d_tax decimal(4,2),
d_ytd decimal(12,2),
d_next_o_id int,
primary key (d_w_id, d_id) );

create table if not exists tpcc.customer (
c_id int not null,
c_d_id int not null,
c_w_id int not null,
c_first varchar(16),
c_middle char(2),
c_last varchar(16),
c_street_1 varchar(20),
c_street_2 varchar(20),
c_city varchar(20),
c_state char(2),
c_zip char(9),
c_phone char(16),
c_since datetime,
c_credit char(2),
c_credit_lim bigint,
c_discount decimal(4,2),
c_balance decimal(12,2),
c_ytd_payment decimal(12,2),
c_payment_cnt int,
c_delivery_cnt int,
c_data text,
PRIMARY KEY(c_w_id, c_d_id, c_id) );

create table if not exists tpcc.history (
h_c_id int,
h_c_d_id int,
h_c_w_id int,
h_d_id int,
h_w_id int,
h_date datetime,
h_amount decimal(6,2),
h_data varchar(24) );

create table if not exists tpcc.new_orders (
no_o_id int not null,
no_d_id int not null,
no_w_id int not null,
PRIMARY KEY(no_w_id, no_d_id, no_o_id));

create table if not exists tpcc.orders (
o_id int not null,
o_d_id int not null,
o_w_id int not null,
o_c_id int,
o_entry_d datetime,
o_carrier_id int,
o_ol_cnt int,
o_all_local int,
PRIMARY KEY(o_w_id, o_d_id, o_id) );

create table if not exists tpcc.order_line (
ol_o_id int not null,
ol_d_id int not null,
ol_w_id int not null,
ol_number int not null,
ol_i_id int,
ol_supply_w_id int,
ol_delivery_d datetime,
ol_quantity int,
ol_amount decimal(6,2),
ol_dist_info char(24),
PRIMARY KEY(ol_w_id, ol_d_id, ol_o_id, ol_number) );

create table if not exists tpcc.item (
i_id int not null,
i_im_id int,
i_name varchar(24),
i_price decimal(5,2),
i_data varchar(50),
PRIMARY KEY(i_id) );

create table if not exists tpcc.stock (
s_i_id int not null,
s_w_id int not null,
s_quantity int,
s_dist_01 char(24),
s_dist_02 char(24),
s_dist_03 char(24),
s_dist_04 char(24),
s_dist_05 char(24),
s_dist_06 char(24),
s_dist_07 char(24),
s_dist_08 char(24),
s_dist_09 char(24),
s_dist_10 char(24),
s_ytd decimal(8,0),
s_order_cnt int,
s_remote_cnt int,
s_data varchar(50),
PRIMARY KEY(s_w_id, s_i_id) );

create index if not exists idx_customer ON tpcc.customer (c_w_id,c_d_id,c_last,c_first);
create index if not exists idx_orders ON tpcc.orders (o_w_id,o_d_id,o_c_id,o_id);
create index if not exists fkey_stock_2 ON tpcc.stock (s_i_id);
create index if not exists fkey_order_line_2 ON tpcc.order_line (ol_supply_w_id,ol_i_id);

UPDATE performance_schema.setup_consumers SET ENABLED='YES' WHERE NAME LIKE 'statements_current';
SET GLOBAL innodb_undo_log_truncate=ON;
