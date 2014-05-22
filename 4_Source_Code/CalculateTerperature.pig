IN_DATA = LOAD 's3://tguthri1/Input' using PigStorage(',') AS (stn:int, wban:int, yearmoda:int, temp:double);
IN_STATIONS = LOAD 's3://tguthri1/US_STATIONS' using PigStorage(',') AS (stn:int, wban:int, state:chararray);

DATA = JOIN IN_DATA BY (stn,wban), IN_STATIONS BY (stn,wban);
NEEDED_DATA = foreach DATA generate yearmoda/100 as yearmo, temp, state;

GROUPED = group NEEDED_DATA by (state, yearmo);
AVERAGES = foreach GROUPED generate flatten(group), AVG(NEEDED_DATA.temp);

STORE AVERAGES INTO 's3://tguthri1/stuff';
