import modules
from modules import *
import datetime
from datetime import datetime

inv = Inventory([])
inv.add(Item("bread", 50.0, 100))
inv.add(Item("coffee", 7.5, 100))
inv.add(Item("tea", 15.0, 100))

cashes = Cashes([])
cashes.add(Cash(0.25, 50))
cashes.add(Cash(1, 50))
cashes.add(Cash(5, 50))
cashes.add(Cash(10, 50))
cashes.add(Cash(20, 50))
cashes.add(Cash(50, 50))
cashes.add(Cash(100, 50))
cashes.add(Cash(200, 50))
cashes.add(Cash(500, 50))
cashes.add(Cash(1000, 50))

print("Welcome to Point of Sale!(POS) \nWhat do you want to do?")
while True:
	currdate = datetime.now().date()
	action = interact()
	if action == 'i':
		print("Current Inventory:")
		inv.itable()
	elif action == 'a':
		print("Current Account:")
		cashes.ctable()
	elif action == 'r':
		record_date = str(input("Enter date of record you want to access in the format YYYY-MM-DD \nRecord Date: "))
		print("Records for the date " + record_date)
		fh = open(record_date+".txt", "r")
		for line in fh:
			print(line.strip('\n'))
		fh.close()
	elif action == 'x':
		print("Goodbye! Have a nice day!")
		break
	elif action == 't':
		new_customer = Customer()
		print("Items bought:")
		for i in new_customer.bought_items:
			print(str(i))
			inv.sub(i, 1)
		total = new_customer.cust_total(inv)
		print("Total to pay of Customer:", total)
		cust_total = "Total to pay of Customer: "+ str(total)
		change = new_customer.getchange(total)
		print("Change to Customer:", change)
		cust_change = "Total change to Customer: " + str(change)
		for k, v in new_customer.payment[1].items():
			cashes.plus(k, v)
		denomchange = new_customer.changedenom(change, cashes)
		for k, v in denomchange.items():
			cashes.sub(k, v)	
		print(denomchange)
		cust_record = Record()
		cust_record.add("Customer"+new_customer.cust_id)
		cust_record.add("Date of Transaction: "+new_customer.date)
		cust_record.add("Time of Transaction: "+new_customer.time)
		cust_record.add("Products bought: "+str(new_customer.bought_items))
		cust_record.add(cust_total)
		cust_record.add("Payment of Customer: "+str(new_customer.payment))
		cust_record.add(cust_change)
		cust_record.add(str(denomchange))
		cust_record.write_record(currdate)
		print('\n')
