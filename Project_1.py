#Name: Iliana Morgan Chevres
#Student ID: 9037 0030 
#Email: ichevres@umich.edu
#Project 1 
#Collaborators: Used ChatGPT for help with the notation on line 9, debugging, and test cases 
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

    for region in profit_dict: 
        for category in profit_dict[region]:
            profit_dict[region][category] = round(profit_dict[region][category], 2)
    
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
                avg_profit[category] = round(info['total_profit'] / info['total_quantity'], 2)
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
        if total > 0: 
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

#test cases 

def test_profit_summary():
    #General test 1 
    test_data = {
        1: {'Region': 'West', 'Category': 'Furniture', 'Profit': '100'},
        2: {'Region': 'West', 'Category': 'Office Supplies', 'Profit': '50'},
        3: {'Region': 'East', 'Category': 'Furniture', 'Profit': '75'}
    }
    expected = {'West': {'Furniture': 100.0, 'Office Supplies': 50.0}, 'East': {'Furniture': 75.0}}
    assert profit_summary(test_data) == expected, "Test Case 1 failed"

    #general test 2 
    test_data[4] = {'Region': 'West', 'Category': 'Furniture', 'Profit': '25'}
    result = profit_summary(test_data)
    assert result['West']['Furniture'] == 125.0, "General case 2 failed"

    #edge case 1 
    assert profit_summary({}) == {}, "Edge case 1 failed"

    # edge case 2
    test_data = {1: {'Region': 'South', 'Category': 'Technology', 'Profit': '-10'}}
    result = profit_summary(test_data)
    assert result['South']['Technology'] == -10.0, "Edge case 2 failed"

    print("All profit_summary() tests passed.")

def test_avg_profit():
    print("\n--- Testing avg_profit() ---")

    # general case 1
    test_data = {
        1: {'Category': 'Furniture', 'Profit': '100', 'Quantity': '5'},
        2: {'Category': 'Furniture', 'Profit': '50', 'Quantity': '5'},
        3: {'Category': 'Office Supplies', 'Profit': '60', 'Quantity': '3'}
    }
    result = avg_profit(test_data)
    assert result['Furniture'] == 15.0, "General case 1 failed"
    assert result['Office Supplies'] == 20.0, "General case 1 failed"

    # general case 2: different mix
    test_data[4] = {'Category': 'Office Supplies', 'Profit': '30', 'Quantity': '3'}
    result = avg_profit(test_data)
    assert result['Office Supplies'] == 15.0, "General case 2 failed"

    # edge case 1: zero quantity
    test_data = {1: {'Category': 'Furniture', 'Profit': '10', 'Quantity': '0'}}
    result = avg_profit(test_data)
    assert result['Furniture'] == 0, "Edge case 1 failed"

    # edge case 2: empty input
    assert avg_profit({}) == {}, "Edge case 2 failed"

    print("All avg_profit() tests passed.")


def test_top_performers():
    print("\n--- Testing top_performers() ---")

    # general case 1
    test_data = {
        1: {'Sub-Category': 'Chairs', 'Profit': '200'},
        2: {'Sub-Category': 'Tables', 'Profit': '300'},
        3: {'Sub-Category': 'Binders', 'Profit': '150'},
        4: {'Sub-Category': 'Phones', 'Profit': '400'}
    }
    result = top_performers(test_data)
    assert 'Phones' in result, "General case 1 failed"
    assert max(result.values()) == 400.0, "General case 1 failed"

    # general case 2: multiple top items
    test_data[5] = {'Sub-Category': 'Accessories', 'Profit': '500'}
    result = top_performers(test_data)
    assert len(result) <= 5, "General case 2 failed"

    # edge case 1: fewer than 5 sub-categories
    small_data = {
        1: {'Sub-Category': 'Paper', 'Profit': '50'},
        2: {'Sub-Category': 'Envelopes', 'Profit': '75'}
    }
    result = top_performers(small_data)
    assert len(result) == 2, "Edge case 1 failed"

    # edge case 2: all negative profits
    neg_data = {
        1: {'Sub-Category': 'Phones', 'Profit': '-100'},
        2: {'Sub-Category': 'Chairs', 'Profit': '-200'}
    }
    result = top_performers(neg_data)
    assert all(p <= 0 for p in result.values()), "Edge case 2 failed"

    print("All top_performers() tests passed.")


def test_percent_byregion():
    print("\n--- Testing percent_byregion() ---")

    # general case 1
    test_data = {
        1: {'Region': 'West', 'Category': 'Furniture', 'Sales': '200'},
        2: {'Region': 'West', 'Category': 'Technology', 'Sales': '800'},
        3: {'Region': 'East', 'Category': 'Furniture', 'Sales': '100'}
    }
    result = percent_byregion(test_data)
    assert round(result['West']['Furniture'], 2) == 20.0, "General case 1 failed"
    assert round(result['West']['Technology'], 2) == 80.0, "General case 1 failed"

    # general case 2: add more regions
    test_data[4] = {'Region': 'South', 'Category': 'Furniture', 'Sales': '300'}
    result = percent_byregion(test_data)
    assert 'South' in result, "General case 2 failed"

    # edge case 1: zero total sales
    test_data = {1: {'Region': 'West', 'Category': 'Furniture', 'Sales': '0'}}
    result = percent_byregion(test_data)
    assert result['West']['Furniture'] == 0.0, "Edge case 1 failed"

    # edge case 2: empty dataset
    assert percent_byregion({}) == {}, "Edge case 2 failed"

    print("All percent_byregion() tests passed.")

#calling everything 
main()
test_profit_summary()
test_percent_byregion()
test_top_performers()
test_avg_profit()