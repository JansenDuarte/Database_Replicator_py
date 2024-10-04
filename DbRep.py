import csv
import os

#Place the name of the database
db_name = 'DB_Name'

sql_insert_clause = """
        use {0}
        insert into {1}
        ({2})
        values

        """
sql_value_clause = """({0})"""

#Place the .csv files in this directory
dir_name = os.path.dirname(__file__)
dir_name += '\\DB_Data\\'

csv_files = [f for f in os.listdir(dir_name)]


column_names = ''

#This makes a pretty good .sql, but you still need to fix wich is int or varchar,
#remove the initial index and the last comma of the values

for csv_file in csv_files:

    table_name = csv_file.split('.')[0]
    output_file = open(table_name + '.sql', 'wt')

    with open(dir_name + csv_file, newline='') as csv_file:
        reader = csv.reader(csv_file, quotechar='|')

        row_count = 0;
        values = '';

        for row in reader:
            if row_count == 0:
                column_names = ','.join(row)
                column = sql_insert_clause.format(db_name, table_name, column_names)
                output_file.write(column + '\n')
            else:
                values = ','.join(row)
                values = sql_value_clause.format(values)
                output_file.write(values + ', \n')

            row_count += 1

    output_file.close()