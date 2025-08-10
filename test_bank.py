# -*- coding: utf-8 -*-
"""
Created on Sun Aug 10 11:34:33 2025

@author: Admin
"""

# test_bank.py
import pytest
from bank import SavingsAccount, CurrentAccount

def test_savings_account_operations():
    account = SavingsAccount("TestUser", 1000)
    
    # Test deposit
    assert account.deposit(500) == "Deposited ₹500. New balance: ₹1500"
    assert account.get_balance() == 1500

    # Test withdraw within balance
    assert account.withdraw(200) == "SavingsAccount: Withdrew ₹200. New balance: ₹1300"

    # Test withdraw exceeding balance
    assert account.withdraw(2000) == "SavingsAccount: Insufficient funds!"

    # Test interest addition
    interest_message = account.add_interest()
    assert "Interest of ₹" in interest_message
    assert account.get_balance() > 1300


def test_current_account_operations():
    account = CurrentAccount("TestUser2", 1000, overdraft_limit=2000)

    # Test deposit
    assert account.deposit(500) == "Deposited ₹500. New balance: ₹1500"
    assert account.get_balance() == 1500

    # Test withdraw within balance
    assert account.withdraw(1000) == "CurrentAccount: Withdrew ₹1000. New balance: ₹500"

    # Test withdraw within overdraft
    assert account.withdraw(2000) == "CurrentAccount: Withdrew ₹2000. New balance: ₹-1500"

    # Test exceeding overdraft
    assert account.withdraw(5000) == "CurrentAccount: Overdraft limit exceeded!"
