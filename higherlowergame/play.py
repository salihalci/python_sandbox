from game_data import data

import random

#{'name': 'Priyanka Chopra Jonas', 'follower_count': 53, 'description': 'Actress and musician', 'country': 'India'}
def format_data(account):
    account_name =account["name"]
    account_description = account["description"]
    account_country =account["country"]
    account_follower_count = account["follower_count"]
    return f"{account_name}, a {account_description} from {account_country}"

account_a = random.choice(data)
account_b = random.choice(data)

if account_a == account_b :
    account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}")
print(f"Compare B: {format_data(account_b)}")


