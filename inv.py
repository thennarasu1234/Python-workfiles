import copy

def clone_items(items,deep=False):
    if deep==False:
        copy_1=copy.copy(items)
        return copy_1
    else:
        copy_1=copy.deepcopy(items)
        return copy_1        
    

def normalize(*record):
    return {"name":[x["name"].strip().title() for x in record],"qty":[int(y["qty"]) for y in record]}

def restock(items,target=10):
    dict_1={}
    for i in range(len(items["name"])):
        dict_1[items["name"][i]]=max(0,target-items["qty"][i])
    return dict_1