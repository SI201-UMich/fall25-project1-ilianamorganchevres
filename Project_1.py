#Name: Iliana Morgan Chevres
#Student ID: 9037 0030 
#Email: ichevres@umich.edu
#Project 1 
def csv_import(file):
    import csv
    with open(file, 'r') as f_name: 
        csv_reader = csv.reader(f_name)
        for row in csv_reader:
            print(row)
    #file.close()
#make this into a nested dict 
csv_import('SampleSuperstore.csv')

#profit summary dictionary function - makes a nested 
def profit_summary(csv_dict):
    profit_dict = []
    for key,value in csv_dict.items():
        region = value[6] 
        category = value[1]
        profit_dict[region] = x
        profit_dict[category] = x
    return profit_dict 
    
#dictionary where teh keys are regions and categories and values are profits 
#average profit for each category in a dictionary 
def avg_profit(csv_dict):
    pass 
#top performers 
def top_performers(csv_dict):
    pass 

#Percentage of each category by region
def percent_byregion(csv_dict):
    pass 

#have to make the main function 
main()
pass 