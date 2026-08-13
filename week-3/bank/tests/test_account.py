import pytest

from bank.account import BankAccount, InsufficientFundsError


@pytest.fixture
def empty_account() -> BankAccount:
    return BankAccount()


def test_new_account_has_zero_balance() -> None:
    assert BankAccount().balance == 0


def test_new_account_with_a_balance_is_correct() -> None:
    assert BankAccount(100).balance == 100


def test_deposit_on_empty_account_increases_correctly(
    empty_account: BankAccount,
) -> None:
    initial_balance = empty_account.balance
    empty_account.deposit(100)
    assert empty_account.balance == initial_balance + 100


@pytest.mark.parametrize("invalid_input", [0, -100])
def test_depositing_invalid_amount_throws_error(
    empty_account: BankAccount, invalid_input: int
) -> None:
    with pytest.raises(ValueError):
        empty_account.deposit(invalid_input)


def test_depositing_into_an_account_increases_correctly() -> None:
    test_account = BankAccount(50)
    initial_balance = test_account.balance
    test_account.deposit(100)
    assert test_account.balance == initial_balance + 100


def test_withdraw_less_than_balance_withdraws_correctly() -> None:
    test_account = BankAccount(100)
    initial_balance = test_account.balance
    test_account.withdraw(30)
    assert test_account.balance == initial_balance - 30


def test_withdraw_on_exact_balance_leaves_zero() -> None:
    test_account = BankAccount(100)
    test_account.withdraw(100)
    assert test_account.balance == 0


@pytest.mark.parametrize("invalid_input", [0, -10])
def test_withdraw_invalid_amount_throws_error(invalid_input: int) -> None:
    test_account = BankAccount(10)
    with pytest.raises(ValueError):
        test_account.withdraw(invalid_input)


def test_no_overdraft_withdraw_more_than_balance_throws_error() -> None:
    test_account = BankAccount(100)
    with pytest.raises(InsufficientFundsError):
        test_account.withdraw(101)


def test_no_overdraft_withdraw_more_than_balance_does_not_change_balance() -> None:
    test_account = BankAccount(100)
    with pytest.raises(InsufficientFundsError):
        test_account.withdraw(101)
    assert test_account.balance == 100


def test_overdraft_withdraw_to_limit() -> None:
    test_account = BankAccount(100, overdraft=50)
    test_account.withdraw(150)
    assert test_account.balance == -50


def test_overdraft_withdraw_past_limit() -> None:
    test_account = BankAccount(100, overdraft=50)
    with pytest.raises(InsufficientFundsError):
        test_account.withdraw(151)


def test_account_with_overdraft_reports_correct_limit() -> None:
    test_account = BankAccount(100, overdraft=50)
    assert test_account.overdraft == 50
