from brownie import FundMe
from scripts.helpful_scripts import get_account

def fund():
    fund_me = FundMe[-1]
    account = get_account()
    price = fund_me.getPrice()
    print(f'price {price}')
    entrance_fee = fund_me.getEntranceFee()
    print(f'entranceFee {entrance_fee}')
    fund_me.fund({"from": account, "value": entrance_fee})
    print(f'Fund Sucess!')
    
def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})

def main():
    fund()
    withdraw()