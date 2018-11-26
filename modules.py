import os
import datetime
from datetime import datetime
import tabulate
from tabulate import tabulate
from playsound import playsound
import qrdata
from qrdata import qrdata

#-----------------------------------------------------------------------------------------------------
class Item:
	def __init__(self, name, price, qty):
		self.name = name
		self.price = float(price)
		self.qty = float(qty)
		self.amount = self.price * self.qty
	def __str__(self):
		return "item: " + str(self.name) + ", "+"price: "+str(self.price)
	def __repr__(self):
		lst = [self.name, self.price, self.qty, self.amount]
		return lst

#-----------------------------------------------------------------------------------------------------
class Inventory:
	def __init__(self, items=[]):
		self.items = items
	def add(self, item):
		self.items.append(item)
	def plus(self, x, y):
		for i in self.items:
			if str(i.name) == str(x):
				i.qty = float(i.qty) + float(y)
			else:
				pass
	def rem(self, x):
		for i in self.items:
			if str(i.name) == str(x):
				item = i
				self.items.pop(item)
	def sub(self, x, y):
		for i in self.items:
			if str(i.name) == str(x):
				if int(i.qty) >= int(y):
					i.qty = int(i.qty) - int(y)
				else:
					print("Insufficient stocks.")
			else:
				pass 
	def itable(self):
		invlist = []
		for i in self.items:
			product = [str(i.name), i.price, i.qty]
			invlist.append(product)
		print(tabulate(invlist, headers = ["Name", "Price", "Quantity"], tablefmt = "fancy_grid"))			
		
	def getprice(self, item):
		for i in self.items:
			if str(i.name) == str(item):
				return float(i.price)
			else:
				pass

	def find(self, x):
		for i in self.items:
			if str(i.name) == str(item):
				return True
			else:
				print("No stock of the product")

#----------------------------------------------------------------------------------------------------------
class Cash:
	def __init__(self, denom, qty):
		self.denom = float(denom)
		self.qty = float(qty)
		self.amount = self.denom * self.qty
	
	def __repr__(self):
		return str(self.denom) + " " + str(self.qty)

class Cashes:
	def __init__(self, cashes=[]):
		self.cashes = cashes
	def __repr__(self):
		lst = []
		for i in self.cashes:
			lst.append(str(i))	
		return str(self.cashes)

	def add(self, cash):
		self.cashes.append(cash)
	def plus(self, x, y):
		for i in self.cashes:
			if float(i.denom) == float(x):
				i.qty = float(i.qty) + float(y)
			else:
				pass
	def sub(self, x, y):
		for i in self.cashes:
			if float(i.denom) == float(x):
				i.qty = float(i.qty) - float(y)
			else:
				pass
	
	def ctable(self):
		cashlist = []
		for i in self.cashes:
			money = [str(i.denom), i.qty]
			cashlist.append(money)
		print(tabulate(cashlist, headers=["Denomination", "Quantity"], tablefmt="fancy_grid"))
	
#-----------------------------------------------------------------------------------------------------------------
class Customer:
	def __init__(self):
		cust_id = 1
		curr_time = str(datetime.now().time())
		curr_date = str(datetime.now().date())
		found = False
		if os.path.exists(curr_date+".txt"):
			fh = open(curr_date+".txt", "r")
			for line in fh:
				if ("Customer"+str(cust_id)) in line:
					found = True
				
				if found:
					cust_id += 1
					found = False
					continue
			fh.close()
		else:
			pass
		self.cust_id = str(cust_id)
		self.date = curr_date
		self.time = curr_time
		self.bought_items = qrdata()
		self.payment = self.payment()
			
	def payment(self):
		total_payment = 0
		denompayment = {}
		payment = []
		while True:
			pay_money = float(input("Enter payment denomination: "))
			count = float(input("Enter count of denomination: "))
			denompayment[pay_money] = count
			add_more = input("Add more payment? Y/N ")
			if add_more == 'y':
				continue
			else:
				break
		
		for k, v in denompayment.items():
			total_payment += float(k) * float(v)
		payment.append(total_payment)
		payment.append(denompayment)
		print("Payment of Customer:\n", payment)
		return payment
				
	def cust_total(self, inventory):
		total = 0.0
		for i in self.bought_items:
			total += inventory.getprice(i)
		return total
	
	def getchange(self, customer_change):
		change = float(self.payment[0]) -  float(customer_change)
		return change
		
	def changedenom(self, total_change, cashinv):
		change = float(total_change)
		denomchange = {}
		denomqty = 0
		for m in cashinv.cashes[::-1]:
			if float(m.denom) <= change:
				denomqty = change // float(m.denom)
				change = change % float(m.denom)
				denomchange[m.denom] = denomqty	
			if change == 0:
				break
		return denomchange
		print(denomchange)

	def bought(self):
		bought = qrdata()
		return bought

	def __repr__(self):
		rep = ""
		for i in self.profile():
			rep += str(i) + '\n'
		return rep

#-----------------------------------------------------------------------------------------------------
class Record:
	def __init__(self, records=[]):
		self.records = records
	def add(self, record):
		self.records.append(record)
	def write_record(self,curr_date):
		for i in self.records:
			fh = open(str(curr_date)+".txt", "a")
			fh.write(i + '\n')
		fh.write('\n')
		fh.close()	

#----------------------------------------------------------------------------------------------------
def interact():
	print("Options in Point of Sale:")
	print("I - Access Inventory")
	print("T - Transact")
	print("A - View Account")
	print("R - View Records")
	print("X - Exit")
	action = input("Enter Action: ")
	return action
