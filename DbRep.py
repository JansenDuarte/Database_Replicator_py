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
csv_path = os.path.dirname(__file__) + '\\DB_Data\\'
gen_path = os.path.dirname(__file__) + '\\Generated_SQLs\\'

csv_files = [f for f in os.listdir(csv_path)]

column_names = ''
item_separator = ',\t'

#This makes a pretty good .sql, but you still need to fix wich is int or varchar,
#remove the initial index and the last comma of the values

useIndex = input("Generate sql with the first index? [y/n]")

if useIndex == 'y' or useIndex == 'Y':
	useIndex = True
else:
     useIndex = False


for csv_file in csv_files:

    table_name = csv_file.split('.')[0]
    output_file = open(gen_path + table_name + '.sql', 'wt')

	#	utf-8-sig encoding is used to remove garbage from the start of the file
    with open(csv_path + csv_file, encoding="utf-8-sig") as csv_file:
        reader = csv.reader(csv_file, quotechar='"', skipinitialspace=True)
        
        row_count = 0;
        values = '';

        for row in reader:
            if row_count == 0:
                if useIndex:
                     column_names = item_separator.join(row)
                else:
                     column_names = item_separator.join(row)
                     column_names = column_names.split(item_separator, 1)[1]
                     
                column = sql_insert_clause.format(db_name, table_name, column_names)
                output_file.write(column + '\n')
                
            else:
                if useIndex:
                     values = item_separator.join(row)
                else:
                     values = item_separator.join(row)
                     values = values.split(item_separator, 1)[1]
                     
                values = sql_value_clause.format(values)
                output_file.write(values + ',\n')

            row_count += 1

    output_file.close()