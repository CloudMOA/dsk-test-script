
create database if not exists manager;

create table if not exists manager.host
(
    id          serial
        primary key,
    hosttype    varchar(255),
    hostname    varchar(255),
    ip          varchar(15),
    protocol    varchar(255),
    description text
);

create table if not exists manager.account
(
    id          serial
        primary key,
    hostname    varchar(255),
    accountid   varchar(255),
    password    varchar(255),
    owner       varchar(255),
    description text
);

create table if not exists manager.person
(
    id          serial
        primary key,
    name        varchar(255),
    password    varchar(255),
    email       varchar(255),
    phone       varchar(15),
    accountid   varchar(255),
    permissions varchar(255),
    description text
);

create table if not exists manager.pod_data
(
    kube_flatting_time                       bigint       not null,
    cluster_id                               varchar(255) not null,
    kind                                     varchar(30)  not null,
    kind_status                              varchar(50),
    metadata_uid                             varchar(40)  not null,
    row_index                                integer      not null,
    metadata_name                            text,
    metadata_selflink                        text,
    metadata_resourceversion                 text,
    metadata_creationtimestamp               varchar(25),
    metadata_generatename                    text,
    metadata_namespace                       text,
    metadata_deletiontimestamp               text,
    metadata_deletiongraceperiodseconds      text,
    metadata_labels                          text,
    metadata_ownerreferences                 text,
    metadata_ownerreferences_kind            varchar(30),
    metadata_ownerreferences_uid             varchar(40),
    metadata_annotations                     text,
    spec_hostnetwork                         text,
    spec_priorityclassname                   text,
    spec_enableservicelinks                  text,
    spec_priority                            text,
    spec_schedulername                       text,
    spec_hostpid                             text,
    spec_nodename                            text,
    spec_serviceaccount                      text,
    spec_serviceaccountname                  text,
    spec_dnspolicy                           text,
    spec_terminationgraceperiodseconds       text,
    spec_restartpolicy                       text,
    spec_securitycontext                     text,
    spec_nodeselector_kubernetes_io_hostname text,
    spec_tolerations                         text,
    status_phase                             text,
    status_hostip                            text,
    status_podip                             text,
    status_starttime                         text,
    status_qosclass                          text,
    status_reason                            text,
    status_message                           text,
    create_time                              timestamp default now(),
    primary key (kube_flatting_time, cluster_id, kind, metadata_uid, row_index)
);
