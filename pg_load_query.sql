select customer.c_id from customer inner join district d on customer.c_w_id = d.d_w_id and customer.c_d_id = d.d_id
inner join history h on customer.c_w_id = h.h_c_w_id and customer.c_d_id = h.h_c_d_id and customer.c_id = h.h_c_id
inner join orders o on customer.c_w_id = o.o_w_id and customer.c_d_id = o.o_d_id and customer.c_id = o.o_c_id
group by customer.c_id
order by customer.c_id
limit 100;

insert into item(i_id, i_im_id, i_name, i_price, i_data)
    values(999899,7723,'FtaOuebsTEST',66.84,'stNesDpTEST');

select * from orders inner join customer c on orders.o_w_id = c.c_w_id and orders.o_d_id = c.c_d_id and orders.o_c_id = c.c_id
inner join history h on c.c_w_id = h.h_c_w_id and c.c_d_id = h.h_c_d_id and c.c_id = h.h_c_id
inner join district d on c.c_w_id = d.d_w_id and c.c_d_id = d.d_id
order by d.d_w_id, c.c_credit_lim
limit 100;

delete from item where i_id=999899;

insert into history(h_c_id, h_c_d_id, h_c_w_id, h_d_id, h_w_id, h_date, h_amount, h_data)
    values(999899,1,1,1,1,'2023-09-07 00:52:51',3723.00,'e3WRFxTEST');

select * from stock
inner join item i on stock.s_i_id = i.i_id
inner join order_line ol on stock.s_w_id = ol.ol_supply_w_id and stock.s_i_id = ol.ol_i_id
inner join orders o on ol.ol_w_id = o.o_w_id and ol.ol_d_id = o.o_d_id and ol.ol_o_id = o.o_id
order by i.i_id, ol.ol_supply_w_id, ol.ol_w_id limit 100;

delete from history where i_id=999899;