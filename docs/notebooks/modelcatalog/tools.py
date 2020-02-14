from pprint import pprint
from tabulate import tabulate
from IPython.display import HTML, display
import texttable as tt

#Method to print a resource as a table
def create_table(resource, **karwgs):
    if isinstance(resource, object) and not isinstance(resource, dict) :
        try:
            resource = resource.to_dict()
        except:
            pass
    
    table = []
    for key, value in resource.items():
        if 'filter' in karwgs and key not in karwgs['filter']:
            continue
        if isinstance(value, dict) or key == "type":
            continue
        table.append([key,value])
    return table

def print_resource(resource, **karwgs):
    tab = tt.Texttable()
    headings = ['Property', 'Value']
    tab.header(headings)    
    table = create_table(resource, **karwgs)
    tab.add_rows(table, header=False)
    print(tab.draw())

def print_resources(resources, **karwgs):
    tab = tt.Texttable()
    headings = ['Property', 'Value']
    tab.header(headings)
    for resource in resources:
        table = create_table(resource, **karwgs)
        tab.add_rows(table, header=False)
        print(tab.draw())
        print("\n")
    

# def print_resources(resources, **karwgs):
#     headings = ['Property', 'Value']

#     for resource in resources:
#         table = create_table(resource, **karwgs)
#         print(tabulate(table, headers=headings, tablefmt="github"))
#         print("\n")

#Method to print a resource as a table
# def create_table(resource, **karwgs):
#     if isinstance(resource, object) and not isinstance(resource, dict) :
#         try:
#             resource = resource.to_dict()
#         except:
#             pass
    
#     table = []
#     for key, value in resource.items():
#         if 'filter' in karwgs and key not in karwgs['filter']:
#             continue
#         if isinstance(value, dict) or key == "type":
#             continue
#         table.append([key,value])
#     return table

# def print_resource(resource, **karwgs):
#     headings = ['Property', 'Value']
#     table = create_table(resource, **karwgs)
#     print(tabulate(table, headers=headings, tablefmt="github"))
        


# def print_resources(resources, **karwgs):
#     headings = ['Property', 'Value']

#     for resource in resources:
#         table = create_table(resource, **karwgs)
#         print(tabulate(table, headers=headings, tablefmt="github"))
#         print("\n")
        
