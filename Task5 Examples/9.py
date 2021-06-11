print("\n")
class Scheme:
    scheme_id = 0
    scheme_name = ""
    outgoing_rate = 0
    message_charge = 0

    def __init__(self,id,name,rate,charge):
        self.scheme_id = id
        self.scheme_name = name
        self.outgoing_rate = rate
        self.message_charge = charge
    
    def display(self): 
        print("Scheme Id: ",self.scheme_id)
        print("Scheme Name: ",self.scheme_name)
        print("Outgoing Rate: ",self.outgoing_rate)
        print("Message Charge: ",self.message_charge)


class Customer(Scheme):
    def __init__(self,id,name,mobile):
        self.cust_id = id
        self.cust_name = name
        self.mobile_no = mobile 

    def display(self):
        print("Customer Id : ",self.cust_id)
        print("Customer Name : ",self.cust_name)
        print("Customer Mobile : ",self.mobile_no)


c1 = Scheme(1,"Double Data",449,"Rs 8/Day") 
c2 = Customer(3,"Rahul",9898987656)
c1.display()
c2.display()
print("\n")
