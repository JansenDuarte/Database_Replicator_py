Database_Replicator_py
===

Small helper that allows the creation of .sql files with the insert clause
for every exported values from a db.


How to
===

You need the .csv files of the data you want to insert.

Most of the db engines export data with the primary id.
If your primary id is AUTO_INCREMENT, just use option 'n' when asked to
gerenate the sql with the first index.

Run DbRep.py, and done!



Known Issues
===

The .sql files are generated with no regard to wich field is NUMBER or
VARCHAR. You need to place single quotes accordinly.

The last line will have an additional comma. Just get rid of it.


Future Features
===
I don't know brother! I did this thing in 15 min. If I find a few
different uses for it, or if you want to add something, hit me up
and show me your changes!


Special Thanks
===
Thank you wifey, for keeping up with my shenanigans. And thank you Manolo for helping with the shenanigans!


Cheers! Keep Creating! Love, JD
===