class BankError(Exception):
    """Base for anything this module raises."""


class InsufficientFundsError(BankError):
    """Withdrawal refused: the account doesn't have the money."""


class BankAccount:

    def __init__(self, balance: int = 0) -> None:
        self.balance: int = balance

    def deposit(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError(f"Deposit amount must be positive, got {amount}")
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError(f"Withdraw amount must be positive, got {amount}")
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw {amount}, balance is {self.balance}"
            )
        self.balance -= amount
