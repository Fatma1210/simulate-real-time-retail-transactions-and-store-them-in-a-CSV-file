import random , time , csv , os
from datetime import datetime
class Transaction : 
   def __init__(self , transaction_id , timestamp , product_id , quantity , price , customer_id) :
      self.transaction_id = transaction_id 
      self.timestamp = timestamp
      self.product_id = product_id
      self.quantity = quantity
      self.price = price
      self.customer_id = customer_id
    

file_Path = "Output.csv"
with open(file_Path , mode = "a" , newline= "") as file : 
   writer = csv.writer(file)
   writer.writerow(["Transaction Id" , "TimeStamp" , "Product Id" , "Quantity" , "Price" , "Customer Id"])
   id = 0 
   while True: 
      id = id + 1 
      transaction = Transaction(id , datetime.now() ,random.randint(1, 5000000) ,  random.randint(1, 5) ,  random.uniform(5 , 100) ,  random.randint(1 , 8982222))
      
      print(transaction.transaction_id , transaction.timestamp , transaction.product_id , transaction.quantity , transaction.price , transaction.customer_id)
      writer.writerow([transaction.transaction_id , transaction.timestamp , transaction.product_id , transaction.quantity , transaction.price , transaction.customer_id]) 
      file.flush() 
      time.sleep(60)


       
