select customer.c_id from customer inner join district d on customer.c_w_id = d.d_w_id and customer.c_d_id = d.d_id
inner join history h on customer.c_w_id = h.h_c_w_id and customer.c_d_id = h.h_c_d_id and customer.c_id = h.h_c_id
inner join orders o on customer.c_w_id = o.o_w_id and customer.c_d_id = o.o_d_id and customer.c_id = o.o_c_id
group by customer.c_id
order by customer.c_id
limit 100;

select * from orders inner join customer c on orders.o_w_id = c.c_w_id and orders.o_d_id = c.c_d_id and orders.o_c_id = c.c_id
inner join history h on c.c_w_id = h.h_c_w_id and c.c_d_id = h.h_c_d_id and c.c_id = h.h_c_id
inner join district d on c.c_w_id = d.d_w_id and c.c_d_id = d.d_id
order by d.d_w_id, c.c_credit_lim
limit 100;

select * from stock
inner join item i on stock.s_i_id = i.i_id
inner join order_line ol on stock.s_w_id = ol.ol_supply_w_id and stock.s_i_id = ol.ol_i_id
inner join orders o on ol.ol_w_id = o.o_w_id and ol.ol_d_id = o.o_d_id and ol.ol_o_id = o.o_id
order by i.i_id, ol.ol_supply_w_id, ol.ol_w_id limit 100;

select * from order_line
inner join orders a on ol_d_id=a.o_d_id and o_c_id=a.o_c_id
inner join history h on a.o_d_id=h.h_c_d_id limit 200;

select * from order_line
inner join orders a on ol_d_id=a.o_d_id and o_c_id=a.o_c_id
union
select * from order_line
inner join orders a on ol_d_id=a.o_d_id and o_c_id=a.o_c_id limit 100;