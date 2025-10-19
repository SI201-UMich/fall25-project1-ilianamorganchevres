#Name: Iliana Morgan Chevres
#Student ID: 9037 0030 
#Email: ichevres@umich.edu
#Project 1 
#Collaborators: Used ChatGPT for help with the notation on line 9 and for debugging 
def csv_import(file):
    csv_dict = {}
    import csv
    with open(file, 'r', encoding="utf-8-sig") as f: 
        csv_reader = csv.DictReader(f)
        for i, row in enumerate(csv_reader, start=1):
            csv_dict[i] = row 
    return csv_dict
#make this into a nested dict 


#profit summary dictionary function - makes a nested 
def profit_summary(csv_dict):
    profit_dict = {}

    for store in csv_dict.values():
            region = store['Region']
            category = store['Category']
            profit = float(store['Profit'])

            if region not in profit_dict: 
                profit_dict[region] = {}
            if category not in profit_dict[region]:
                profit_dict[region][category] = 0
            
            profit_dict[region][category] += profit 
    return profit_dict 
    

#average profit for each category in a list containing dicts 
def avg_profit(csv_dict):
    category_totals = {}
    for store in csv_dict.values():
        category = store['Category']
        profit = float(store['Profit'])
        quantity = int(store['Quantity'])

        if category not in category_totals: 
            category_totals[category] = {'total_profit': 0, 'total_quantity': 0}
        
        category_totals[category]['total_profit'] += profit   
        category_totals[category]['total_quantity'] += quantity

        avg_profit = {}
        for category, info in category_totals.items():
            if info['total_quantity']:
                avg_profit[category] = info['total_profit'] / info['total_quantity']
            else: 
                avg_profit[category] = 0
    return avg_profit

#top performers 
def top_performers(csv_dict):
    subcat_profit = {}
    for store in csv_dict.values():
        subcat = store['Sub-Category']
        profit = float(store['Profit'])

        subcat_profit[subcat] = subcat_profit.get(subcat, 0) + profit

    sorted_subcats = sorted(subcat_profit.items(), key=lambda x: x[1], reverse=True)[:5]
    top_perform_dict = {subcat: round(profit, 2) for subcat, profit in sorted_subcats}
    return top_perform_dict

#Percentage of each category by region
def percent_byregion(csv_dict):
    region_data = {}

    for store in csv_dict.values():
        region = store['Region']
        category = store['Category']
        sales = float(store['Sales'])

        if region not in region_data:
            region_data[region] = {'total_sales': 0, 'categories': {}}

        region_data[region]['total_sales'] += sales
        region_data[region]['categories'][category] = (
            region_data[region]['categories'].get(category, 0) + sales
        )

    percent_dict = {}
    for region, info in region_data.items():
        total = info['total_sales']
        percent_dict[region] = {
            category: round((cat_sales / total) * 100, 2)
            for category, cat_sales in info['categories'].items()
        }

    return percent_dict

#write results to file 
def write_results(file, data):
    with open(file, 'w') as f: 
        for key, value in data.items():
            f.write(f"{key}: {value}\n")

#have to make the main function 
def main():
    csv_dict = csv_import("SampleSuperstore.csv")
    
    print("--Profit Summary--")
    print(profit_summary(csv_dict))
    
    print("\n -- Average Profit per Category --")
    print(avg_profit(csv_dict))
    
    print("\n -- Top 5 Subcategories Based on Profit --")
    print(top_performers(csv_dict))

    print("\n -- Category Percentage by Region --")
    print(percent_byregion(csv_dict))

    #output to text file 
    write_results('profit_summary.txt', profit_summary(csv_dict))
    write_results('top_performers.txt', top_performers(csv_dict))
    write_results("avg_profit.txt", avg_profit(csv_dict))
    write_results("percent_byregion.txt", percent_byregion(csv_dict))
main()

