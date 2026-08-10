import pytest

from bank.account import BankAccount


def test_new_account_has_zero_balance():
    assert BankAccount().balance == 0


def test_new_account_with_a_balance_reports_it():
    assert BankAccount(100).balance == 100


def test_deposit_on_empty_account_increases_by_amount():
    test_account = BankAccount()
    initial_balance = test_account.balance
    test_account.deposit(100)
    assert test_account.balance == initial_balance + 100


def test_depositing_zero_should_throw_error():
    test_account = BankAccount()
    with pytest.raises(ValueError):
        test_account.deposit(0)


def test_depositing_into_a_non_empty_account_increases_by_amount():
    test_account = BankAccount(50)
    initial_balance = test_account.balance
    test_account.deposit(100)
    assert test_account.balance == initial_balance + 100


def test_depositing_a_negative_amount_should_throw_error():
    test_account = BankAccount()
    with pytest.raises(ValueError):
        test_account.deposit(-100)


def test_withdraw_less_than_balance_withdraws_correctly():
    test_account = BankAccount(100)
    initial_balance = test_account.balance
    test_account.withdraw(30)
    assert test_account.balance == initial_balance - 30


def test_withdraw_on_exact_balance_leaves_zero():
    test_account = BankAccount(100)
    test_account.withdraw(100)
    assert test_account.balance == 0


# Withdraw — invalid amount

# Taking out zero is an error.
# Taking out a negative amount is an error.

# Withdraw — no overdraft

# 100, no overdraft, take 101 → refused.
# Same case: the balance is still 100 afterwards. The rejected operation must not mutate state. Assert this separately — a pytest.raises block passing tells you nothing about what the balance did.

# Withdraw — with overdraft

# 100, overdraft 50, take 150 → balance -50. Boundary: exactly at the limit, allowed.
# 100, overdraft 50, take 151 → refused.
# An account opened with an overdraft limit reports that limit. Currently nothing constructs one — the parameter would be untested.
