# Database_Replicator_py
 Helper for replicating database data
-----

Small helper that allows the creation of .sql files with the insert clause
for every exported values from a db.
-----

## Known Issues

You need the .csv files of the data you want to export.

The .sql files generated with no regard to wich field is NUMBER or
VARCHAR. You need to place single quotes accordinly.

Most of the db engines export data with the primary id.
If your primary id is AUTO_INCREMENT, you need to remove it manualy
from the .sql (easier than removing it from the .csv)
-----

## Future Features

I don't know brother! I did this thing in 15 min. If I find a few
different uses for it, or if you want to add something, hit me up
and show me your changes!

Cheers! Keep creating! Love, JD!