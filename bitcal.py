import urllib3
import json
http =urllib3.PoolManager()

def trans_cost():
    url = http.request('GET','https://bitcoinfees.earn.com/api/v1/fees/recommended')
    json_obj = json.loads(url.data.decode('utf-8'))
    return json_obj 
json_obj1 = trans_cost() 
#print(json_obj1)


def getPrice(coin_id):
    print("Input coin")
    coin_id = input()
    url_start = 'api.coincap.io/v2/assets/'
    coin = coin_id
    url = http.request('GET',str(url_start + coin))
    json_obj = json.loads(url.data.decode('utf-8'))
    print(json_obj)
    
def exchange_rate(currency, bitcoin):
    exchange_rate = currency/bitcoin
#rate = exchange_rate()
#print('Your bitcoin equals = ', rate)


def calc_sales_amount(bit_amount, trans_amount):
     amount = bit_amount + trans_amount


#amount = calc_sales_amount()
#print("You can sell at", amount, "without making a loss")

"""
print('Amount in crypto choose  A and  Amount in  your currency choose B ')
ans=input()


print("please input how much you wish to sell.")
amount = input()
print("Also input the amount of bitcoin you wish to sell")
input(amount_of_bitcoin)
input(amount_currency)



value_in_usd = exchange_rate * amount_of_bitcoin
"""