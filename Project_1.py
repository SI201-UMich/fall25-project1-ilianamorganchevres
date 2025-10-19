#Name: Iliana Morgan Chevres
#Student ID: 9037 0030 
#Email: ichevres@umich.edu
#Project 1 
def csv_import(file):
    csv_dict = {}
    import csv
    with open(file, 'r') as f: 
        csv_reader = csv.DictReader(f)
        for i, row in enumerate(csv_reader, start=1):
            csv_dict[i] = row 
    return csv_dict
#make this into a nested dict 


#profit summary dictionary function - makes a nested 
def profit_summary(csv_dict):
    profit_dict = {}
    for store in csv_dict.values():
        for key in store.keys():
            if key == 'Region': 
                region = store['Region']
                profit_dict['Region'] = region
            if key == 'Category':
                category = store['Category']
                profit_dict['Category'] = category
    return profit_dict 
    #its only going through one, not all of them 

#average profit for each category in a list containing dicts 
def avg_profit(csv_dict):
    avg_profit = []
    for store in csv_dict.values():
        for key, value in store.items():
            count = 0 
            profit = 0 
            region = store['Region']
            category = store['Category']
            profit = store['Profit']
            count += 1 
            avg = float(profit) / count 
            
            if key == 'Region':
                inner_region_dict = {f"Region: {region}, Average Profit: {avg}"}
                avg_profit.append(inner_region_dict)
            if key == "Category":
                inner_category_dict = {f"Category: {category}, Average Profit: {avg}"}
                avg_profit.append(inner_category_dict)
    return avg_profit

#top performers 
def top_performers(csv_dict):
    pass 

#Percentage of each category by region
def percent_byregion(csv_dict):
    pass 

#write results to file 
def write_results(file, data):
    with open(filename, 'w') as f: 
        for key, value in data.items():
            f.write(f"{key}: {value}\n")
            
#have to make the main function 
def main():
    csv_dict = csv_import("SampleSuperstore.csv")
    
    profit_summary(csv_dict)
    avg_profit(csv_dict)
    top_performers(csv_dict)
    percent_byregion(csv_dict)

    #output to text file 
    write_results('profit_summary.txt', profit_summary(csv_dict))
    write_results('top_performers.txt', top_performers(csv_dict))

main()

