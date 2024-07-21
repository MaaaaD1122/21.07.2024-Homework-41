import threading


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f'Deposited {amount}, new balance is {self.balance}')

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f'Withdrew {amount}, new balance is {self.balance}')


def deposit_task(account, amount):
    for i in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):
    for i in range(5):
        account.withdraw(amount)


account = BankAccount(1000)

deposit = threading.Thread(target=deposit_task, args=(account, 100))
withdraw = threading.Thread(target=withdraw_task, args=(account, 150))

deposit.start()
withdraw.start()

deposit.join()
withdraw.join()