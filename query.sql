select * from (select metadata_namespace, status_phase, status_reason, count(*) as cnt
    from pod_info group by metadata_namespace, status_phase, status_reason) A
inner join pod_info B on A.status_phase = B.status_phase
inner join pod_info C on A.status_phase = C.status_phase
order by B.metadata_labels asc, B.metadata_name desc, B.spec_hostnetwork desc
limit 30000;

select * from pod_info A
left outer join pod_info B on A.kind_status = B.status_phase
left outer join pod_info C on A.kind_status = C.status_phase
order by B.kind_status desc
limit 5000;
