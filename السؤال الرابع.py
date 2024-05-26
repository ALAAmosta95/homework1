# الكلاس الأساسي لحساب البنك
class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(f"تم إيداع {amount} دولار. الرصيد الحالي: {self.balance} دولار")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"تم سحب {amount} دولار. الرصيد الحالي: {self.balance} دولار")
        else:
            print("رصيدك غير كاف للسحب.")

    def get_balance(self):
        return self.balance

# كلاس حساب التوفير الذي يرث من كلاس حساب البنك
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"تم إضافة الفائدة بمبلغ {interest} دولار. الرصيد الحالي: {self.balance} دولار")

    def __str__(self):
        return f"رقم الحساب: {self.account_number}, صاحب الحساب: {self.account_holder}, الرصيد: {self.balance} دولار, معدل الفائدة: {self.interest_rate * 100}%"

# إنشاء كائن حساب بنكي عادي
account = BankAccount("12345", "John Doe")
account.deposit(1000)
account.withdraw(500)
print(f"الرصيد الحالي: {account.get_balance()} دولار")

# إنشاء كائن حساب توفير
savings_account = SavingsAccount("54321", "Jane Smith", 0.05)
savings_account.deposit(2000)
savings_account.apply_interest()
print(savings_account)
