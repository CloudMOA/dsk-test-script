select * from (select metadata_namespace, status_phase, status_reason, count(*) as cnt
    from pod_data group by metadata_namespace, status_phase, status_reason) A
inner join pod_data B on A.status_phase = B.status_phase
inner join pod_data C on A.status_phase = C.status_phase
order by B.metadata_labels asc, B.metadata_name desc, B.spec_hostnetwork desc
limit 100;

select * from pod_data A
left outer join pod_data B on A.kind_status = B.status_phase
left outer join pod_data C on A.kind_status = C.status_phase
order by B.kind_status desc
limit 100;

select id, hostname, accountid, owner, description from account where owner like '%Leo%' limit 100;

select id, hosttype, hostname, ip, protocol, description from host limit 100;

select id, name, email, phone, accountid, permissions, description from person limit 100;

select metadata_name, metadata_namespace, metadata_ownerreferences from pod_data limit 100;