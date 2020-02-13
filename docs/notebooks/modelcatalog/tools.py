from pprint import pprint
import texttable as tt

#Method to print a resource as a table
def print_resource(resource, **karwgs):
    if isinstance(resource, object) and not isinstance(resource, dict) :
        try:
            resource = resource.to_dict()
        except:
            pass
    
    tab = tt.Texttable()
    headings = ['Property', 'Value']
    tab.header(headings)
    for key, value in resource.items():
        if 'filter' in karwgs and key not in karwgs['filter']:
            continue
        if isinstance(value, dict) or key == "type":
            continue
        tab.add_row([key,value])
    print(tab.draw())
    
def print_resources(resources, **karwgs):
    for resource in resources:
        print_resource(resource, **karwgs)
