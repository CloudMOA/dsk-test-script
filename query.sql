select * from (select metadata_namespace, status_phase, status_reason, count(*) as cnt
    from pod_data group by metadata_namespace, status_phase, status_reason) A
inner join pod_data B on A.status_phase = B.status_phase
order by B.metadata_labels asc, B.metadata_name desc, B.spec_hostnetwork desc
limit 10000;