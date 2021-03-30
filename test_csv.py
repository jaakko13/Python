import csv


#file = open("")
weekday_counter = 0
weekend_counter = 0



with open("CSV_Testing/monroe-county-crash-data2003-to-2015.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    
    
    for line in reader:
        if line[4] == 'Weekday':
            weekday_counter += 1
        elif line[4] == 'Weekend':
            weekend_counter += 1

    print(weekday_counter, ' crashes happened on a weekday')
    print(weekend_counter, ' crashes happened on a weekend')



