import json
with open("/Users/santhosh-13119/Desktop/sample.json") as file:                                             #PATH
    data=json.load(file)
    transactions=data["TRANSACTIONS"]
    for item in transactions:
        #print(f"module_name= {item['module_name']}, transaction_id= {item['transaction_id']}\n")
        print(f"https://crm.zoho.in/crm/org60005938078/tab/{item['module_name']}/{item['transaction_id']}")   