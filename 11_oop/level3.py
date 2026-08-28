class User:

    def __init__(self, name, age):
        self.name = name#public
        self._age = age#protected ,it can be accesed but we dont prefer it so we put protected,i will 
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance
        
account = BankAccount(1000)
print(account.__balance)#attribute error



        
        
class User:

    def __init__(self, name, email, age):
        self._name = name
        self._email = email
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Name must not be empty")
        self._name = value.strip()
        
        

    # email
     
    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Email must contain '@'")
        self._email = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not (0 <= value <= 120):
            raise ValueError("Age must be between 0 and 120")
        self._age = value


# ---- Example usage ----
user = User("Ali", "ali@gmail.com", 22)

print(user.name)   # Ali
print(user.email)  # ali@gmail.com
print(user.age)    # 22

# ---- Invalid data tests ----
try:
    user.age = -5
except ValueError as e:
    print("Error setting age:", e)   # Age must be between 0 and 120

try:
    user.email = "hello"
except ValueError as e:
    print("Error setting email:", e) # Email must contain '@'
    
    