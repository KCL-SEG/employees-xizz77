"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, commission, contract_type, salary, hours, commission_type, num_contracts) -> None:
        self.name = name
        self.commission = commission
        self.contract_type = contract_type
        self.salary = salary
        self.hours = hours
        self.contract_type = contract_type
        self.num_contracts = num_contracts
        self.commission_type = commission_type
    
    # bonus or contract commission and commission = 0 means none
    def get_pay(self):
        total_pay = 0
        if self.contract_type == "hourly":
            total_pay += self.salary * self.hours
        elif self.contract_type == "monthly":
            total_pay += self.salary

        if self.commission_type == "contract":
            total_pay += self.num_contracts * self.commission
        elif self.commission_type == "bonus":
            total_pay+= self.commission
        
        return total_pay
    
    def __str__(self) -> str:
        if self.contract_type == "monthly" and self.commission == 0:
            return f"{self.name} works on a monthly salary of {self.get_pay()}. Their total pay is {self.get_pay()}."
        elif self.contract_type == "hourly" and self.commission == 0:
            return f"{self.name} works on a contract of {self.hours} hours at {self.salary}/hour. Their total pay is {self.get_pay()}."
        elif self.contract_type == "monthly" and self.commission_type == "contract":
            return f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.num_contracts} contract(s) at {self.commission}/contract. Their total pay is {self.get_pay()}."
        elif self.contract_type == "hourly" and self.commission_type == "contract":
            return f"{self.name} works on a contract of {self.hours} hours at {self.salary}/hour and receives a commission for {self.num_contracts} contract(s) at {self.commission}/contract. Their total pay is {self.get_pay()}."
        elif self.contract_type == "monthly" and self.commission_type == "bonus":
            return f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.commission}. Their total pay is {self.get_pay()}."
        elif self.contract_type == "hourly" and self.commission_type == "bonus":
            return f"{self.name} works on a contract of {self.hours} hours at {self.salary}/hour and receives a bonus commission of {self.commission}. Their total pay is {self.get_pay()}."
        

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',0,"monthly",4000,0, "", 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 0,"hourly", 25, 100, "", 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 200,"monthly",3000, 0, "contract", 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 220, "hourly", 25, 150, "contract", 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 1500, "monthly", 2000, 0, "bonus", 0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 600, "hourly", 30, 120, "bonus", 0)

print(str(charlie))
print(charlie.get_pay())
