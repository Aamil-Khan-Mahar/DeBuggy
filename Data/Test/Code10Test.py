import unittest
from Code10Correct.py import BankAccount  

class TestBankAccount(unittest.TestCase):

    def test_initial_balance(self):
        account = BankAccount("Alice", 1000)
        self.assertEqual(account.balance, 1000)
        self.assertEqual(account.owner, "Alice")

    def test_deposit_valid(self):
        account = BankAccount("Alice", 1000)
        response = account.deposit(500)
        self.assertEqual(response, "$500 deposited. New balance: $1500")
        self.assertEqual(account.balance, 1500)

    def test_deposit_invalid(self):
        account = BankAccount("Alice", 1000)
        response = account.deposit(-500)
        self.assertEqual(response, "Deposit amount must be positive.")
        self.assertEqual(account.balance, 1000)

    def test_withdraw_valid(self):
        account = BankAccount("Alice", 1000)
        response = account.withdraw(200)
        self.assertEqual(response, "$200 withdrawn. Remaining balance: $800")
        self.assertEqual(account.balance, 800)

    def test_withdraw_invalid(self):
        account = BankAccount("Alice", 1000)
        response = account.withdraw(1500)
        self.assertEqual(response, "Insufficient funds.")
        self.assertEqual(account.balance, 1000)

    def test_withdraw_negative(self):
        account = BankAccount("Alice", 1000)
        response = account.withdraw(-200)
        self.assertEqual(response, "Withdrawal amount must be positive.")
        self.assertEqual(account.balance, 1000)

    def test_check_balance(self):
        account = BankAccount("Alice", 1000)
        response = account.check_balance()
        self.assertEqual(response, "Account owner: Alice, Balance: $1000")

    def test_multiple_transactions(self):
        account = BankAccount("Alice", 1000)
        account.deposit(500)
        account.withdraw(300)
        account.deposit(200)
        account.withdraw(100)
        
        # After these transactions: 1000 + 500 - 300 + 200 - 100 = 1300
        self.assertEqual(account.balance, 1300)

if __name__ == '__main__':
    unittest.main()

