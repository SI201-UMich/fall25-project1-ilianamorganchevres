#Project 1 
def csv_import(file):
    import csv
    with open(file, 'r') as f_name: 
        csv_reader = csv.reader(f_name)
    
    for row in csv_reader:
        print(row)

csv_import('SampleSuperstore.csv')
