IN_DATA = LOAD 's3://tguthri1/Input' using PigStorage(',') AS (stn:int, wban:int, yearmoda:int, temp:double, bs0, bs1, bs2, bs3, bs4, bs5, bs6, bs7, bs8, bs9, bs10, bs11, bs12, bs13,bs14,bs15,sndp:double);
IN_STATIONS = LOAD 's3://tguthri1/US_STATIONS' using PigStorage(',') AS (stn:int, wban:int, state:chararray);

FILTERED = FILTER IN_DATA BY sndp != 999.9;

DATA = JOIN FILTERED BY (stn,wban), IN_STATIONS BY (stn,wban);
NEEDED_DATA = foreach DATA generate state, sndp;

GROUPED = group NEEDED_DATA by state;
AVERAGES = foreach GROUPED generate flatten(group), AVG(NEEDED_DATA.sndp), COUNT(NEEDED_DATA.sndp);

STORE AVERAGES INTO 's3://tguthri1/snostuff';
