import requests, json, colorama, uuid
from colorama import init
init()
from colorama import Fore, Style

def isHex(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False

def isId(idx):
    return (isHex(idx) and len(idx) == 20)

def isTransactionId(idx):
    try:
        uuid.UUID(idx)
        return True
    except ValueError:
        return False

tab = ' ' * 4
errors = 0


## POST api/account

print('1. POST api/account')
print(tab * 1, 'Create a new account')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'name': 'Name',
    'surname': 'Surname'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/account', headers = headers, data = data)

if isId(json.loads(r.text)['id']) and len(json.loads(r.text)) == 1 and r.status_code == 200 and list(json.loads(r.text).keys())[0] == 'id':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/account?name=Name&surname=Surname')

if isId(json.loads(r.text)['id']) and len(json.loads(r.text)) == 1 and r.status_code == 200 and list(json.loads(r.text).keys())[0] == 'id':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Invalid request parameters')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'dummy': 'Name',
    'surname': 'Surname'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/account', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/account?dummy=Name&surname=Surname')

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Multiple request parameters')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'name': 'Name',
    'surname': 'Surname',
    'dummy': 'Dummy'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/account', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/account?name=Name&surname=Surname&dummy=Dummy')

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1


## GET api/account

print('2. GET api/account')
print(tab * 1, 'Get all accounts in system')

r = requests.get('http://127.0.0.1:5000/api/account')

check = True
for account in json.loads(r.text):
    if not(isId(account['id']) and len(account) == 4):
        check = False

if check and r.status_code == 200:
    print(Fore.GREEN + tab * 2, 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + tab * 2, 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1


## DELETE api/account

print('3. DELETE api/account')
print(tab * 1, 'Delete account with 2c543e03a7054e2185d1 as id')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'id': '2c543e03a7054e2185d1'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.delete('http://127.0.0.1:5000/api/account', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 200 and list(json.loads(r.text).keys())[0] == 'status':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Delete account with 61bb03b09fab16342174 as id')
print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.delete('http://127.0.0.1:5000/api/account?id=61bb03b09fab16342174')

if len(json.loads(r.text)) == 1 and r.status_code == 200 and list(json.loads(r.text).keys())[0] == 'status':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Invalid request parameters')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'dummy': '2c543e03a7054e2185d1'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.delete('http://127.0.0.1:5000/api/account', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.delete('http://127.0.0.1:5000/api/account?dummy=61bb03b09fab16342174')

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Multiple request parameters')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'id': '2c543e03a7054e2185d1',
    'dummy': 'Dummy'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.delete('http://127.0.0.1:5000/api/account', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.delete('http://127.0.0.1:5000/api/account?id=61bb03b09fab16342174&dummy=Dummy')

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Invalid id')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'id': '2c543e03a7054e2185dz'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.delete('http://127.0.0.1:5000/api/account', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.delete('http://127.0.0.1:5000/api/account?id=61bb03b09fab1634217z')

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Valid but nonexistent id')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'id': '2c543e03a7054e2185d2'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.delete('http://127.0.0.1:5000/api/account', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 404 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.delete('http://127.0.0.1:5000/api/account?id=61bb03b09fab16342175')

if len(json.loads(r.text)) == 1 and r.status_code == 404 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1


## GET api/account/<id>

print('4. GET api/account/<id>')
print(tab * 1, 'Get account info with 58473c2ad561d5eafcf5 as id')

r = requests.get('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf5')

if len(json.loads(r.text)[0]) == 4 and r.status_code == 200 and r.headers['X-Sistema-Bancario'] != '' and ';' in r.headers['X-Sistema-Bancario']:
    print(Fore.GREEN + tab * 2, 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + tab * 2, 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Invalid id')

r = requests.get('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcfz')

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + tab * 2, 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + tab * 2, 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Valid but nonexistent id')

r = requests.get('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf1')

if len(json.loads(r.text)) == 1 and r.status_code == 404 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + tab * 2, 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + tab * 2, 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1


## POST api/account/<id>

print('5. POST api/account/<id>')
print(tab * 1, 'Add 100.55 to id 58473c2ad561d5eafcf5')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'amount': '100.55'
    }
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf5', headers = headers, data = data)

if isTransactionId(json.loads(r.text)['trans_id']) and len(json.loads(r.text)) == 2 and r.status_code == 200:
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf5?amount=100.55')

if isTransactionId(json.loads(r.text)['trans_id']) and len(json.loads(r.text)) == 2 and r.status_code == 200:
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Remove 100.55 from id 58473c2ad561d5eafcf5')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'amount': '-100.55'
    }
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf5', headers = headers, data = data)

if isTransactionId(json.loads(r.text)['trans_id']) and len(json.loads(r.text)) == 2 and r.status_code == 200:
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf5?amount=-100.55')

if isTransactionId(json.loads(r.text)['trans_id']) and len(json.loads(r.text)) == 2 and r.status_code == 200:
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Deposits/Withdraws 0 to id 58473c2ad561d5eafcf5')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'amount': '0'
    }
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf5', headers = headers, data = data)

if isTransactionId(json.loads(r.text)['trans_id']) and len(json.loads(r.text)) == 2 and r.status_code == 200:
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf5?amount=0')

if isTransactionId(json.loads(r.text)['trans_id']) and len(json.loads(r.text)) == 2 and r.status_code == 200:
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Invalid request parameters')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'dummy': '100.55'
    }
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf5', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf5?dummy=100.55')

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Multiple request parameters')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'amount': '100.55',
    'dummy': 'Dummy'
    }
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf5', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf5?amount=100.55&dummy=Dummy')

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Invalid id')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'amount': '100.55'
    }
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcfz', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcfz?amount=100.55')

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Valid but nonexistent id')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'amount': '100.55'
    }
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf1', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 404 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf1?amount=100.55')

if len(json.loads(r.text)) == 1 and r.status_code == 404 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Insufficient amount (-1000000000.1)')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'amount': '-1000000000.1'
    }
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcfz', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcfz?amount=-1000000000.1')

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Add less than the minimum unit value (1.001)')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'amount': '1.001'
    }
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcfz', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcfz?amount=1.001')

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1


## PUT api/account/<id>

print('6. PUT api/account/<id>')
print(tab * 1, 'Overwrite name and surname of id 58473c2ad561d5eafcf5')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'name': 'Chono',
    'surname': 'Xeno'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.put('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf5', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 200 and list(json.loads(r.text).keys())[0] == 'status':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.put('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf5?name=Chong&surname=Xena')

if len(json.loads(r.text)) == 1 and r.status_code == 200 and list(json.loads(r.text).keys())[0] == 'status':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Invalid request parameters')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'dummy': 'Chono',
    'surname': 'Xeno'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.put('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf5', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.put('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf5?dummy=Chong&surname=Xena')

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Multiple request parameters')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'name': 'Chono',
    'surname': 'Xeno',
    'dummy': 'Dummy'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.put('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf5', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.put('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf5?dummy=Chong&surname=Xena&dummy=Dummy')

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Invalid id')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'name': 'Chono',
    'surname': 'Xeno'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.put('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcfz', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.put('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcfz?name=Chono&surname=Xeno')

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Valid but nonexistent id')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'name': 'Chono',
    'surname': 'Xeno'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.put('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf1', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 404 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.put('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf1?name=Chono&surname=Xeno')

if len(json.loads(r.text)) == 1 and r.status_code == 404 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1


## PATCH api/account/<id>

print('7. PATCH api/account/<id>')
print(tab * 1, 'Overwrite name of id 58473c2ad561d5eafcf5')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'name': 'Gnohc'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.patch('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf5', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 200 and list(json.loads(r.text).keys())[0] == 'status':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.patch('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf5?name=Chong')

if len(json.loads(r.text)) == 1 and r.status_code == 200 and list(json.loads(r.text).keys())[0] == 'status':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Overwrite surname of id 58473c2ad561d5eafcf5')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'surname': 'Anex'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.patch('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf5', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 200 and list(json.loads(r.text).keys())[0] == 'status':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.patch('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf5?surname=Xena')

if len(json.loads(r.text)) == 1 and r.status_code == 200 and list(json.loads(r.text).keys())[0] == 'status':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Invalid request parameters')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'dummy': 'Gnohc'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.patch('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf5', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.patch('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf5?dummy=Chong')

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Multiple request parameters')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'name': 'Gnohc',
    'surname': 'Anex'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.patch('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf5', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.patch('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf5?name=Chong&surname=Anex')

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Invalid id')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'name': 'Gnohc'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.patch('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcfz', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.patch('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcfz?name=Chong')

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Valid but nonexistent id')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'name': 'Gnohc'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.patch('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf1', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 404 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.patch('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf1?name=Chong')

if len(json.loads(r.text)) == 1 and r.status_code == 404 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1


## HEAD api/account/<id>

print('8. HEAD api/account/<id>')
print(tab * 1, 'Get name and surname of id 58473c2ad561d5eafcf5')

r = requests.head('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf5')

if r.text == '' and r.headers['X-Sistema-Bancario'] != '' and ';' in r.headers['X-Sistema-Bancario'] and r.status_code == 200:
    print(Fore.GREEN + tab * 2, 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + tab * 2, 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Invalid id')

r = requests.head('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcfz')

if r.status_code == 400: #HEAD requests don't give back a response
    print(Fore.GREEN + tab * 2, 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + tab * 2, 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Valid but nonexistent id')

r = requests.head('http://127.0.0.1:5000/api/account/58473c2ad561d5eafcf1')

if r.status_code == 404: #HEAD requests don't give back a response
    print(Fore.GREEN + tab * 2, 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + tab * 2, 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1


## POST api/transfer

print('9. POST api/transfer')
print(tab * 1, 'Transfer 50 from 58473c2ad561d5eafcf5 to 62393738957e18bbe5a3')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'from': '58473c2ad561d5eafcf5',
    'to': '62393738957e18bbe5a3',
    'amount': '50'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/transfer', headers = headers, data = data)

if isTransactionId(json.loads(r.text)['trans_id']) and len(json.loads(r.text)) == 3 and r.status_code == 200:
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/transfer?from=58473c2ad561d5eafcf5&to=62393738957e18bbe5a3&amount=50')

if isTransactionId(json.loads(r.text)['trans_id']) and len(json.loads(r.text)) == 3 and r.status_code == 200:
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Transfer 0 from 58473c2ad561d5eafcf5 to 62393738957e18bbe5a3')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'from': '58473c2ad561d5eafcf5',
    'to': '62393738957e18bbe5a3',
    'amount': '0'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/transfer', headers = headers, data = data)

if isTransactionId(json.loads(r.text)['trans_id']) and len(json.loads(r.text)) == 3 and r.status_code == 200:
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/transfer?from=58473c2ad561d5eafcf5&to=62393738957e18bbe5a3&amount=0')

if isTransactionId(json.loads(r.text)['trans_id']) and len(json.loads(r.text)) == 3 and r.status_code == 200:
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Transfer 50 from 58473c2ad561d5eafcf5 to themselves')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'from': '58473c2ad561d5eafcf5',
    'to': '58473c2ad561d5eafcf5',
    'amount': '50'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/transfer', headers = headers, data = data)

if isTransactionId(json.loads(r.text)['trans_id']) and len(json.loads(r.text)) == 2 and r.status_code == 200: # receiver and sender balances are the same
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/transfer?from=58473c2ad561d5eafcf5&to=58473c2ad561d5eafcf5&amount=50')

if isTransactionId(json.loads(r.text)['trans_id']) and len(json.loads(r.text)) == 2 and r.status_code == 200:
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Invalid request parameters')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'dummy': '58473c2ad561d5eafcf5',
    'to': '62393738957e18bbe5a3',
    'amount': '50'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/transfer', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/transfer?dummy=58473c2ad561d5eafcf5&to=62393738957e18bbe5a3&amount=50')

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Multiple request parameters')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'from': '58473c2ad561d5eafcf5',
    'to': '62393738957e18bbe5a3',
    'amount': '50',
    'dummy': 'Dummy'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/transfer', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/transfer?from=58473c2ad561d5eafcf5&to=62393738957e18bbe5a3&amount=50&dummy=Dummy')

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Invalid sender id')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'from': '58473c2ad561d5eafcfz',
    'to': '62393738957e18bbe5a3',
    'amount': '50'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/transfer', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/transfer?from=58473c2ad561d5eafcfz&to=62393738957e18bbe5a3&amount=50')

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Valid but nonexistent sender id')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'from': '58473c2ad561d5eafcf1',
    'to': '62393738957e18bbe5a3',
    'amount': '50'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/transfer', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 404 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/transfer?from=58473c2ad561d5eafcf1&to=62393738957e18bbe5a3&amount=50')

if len(json.loads(r.text)) == 1 and r.status_code == 404 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Invalid receiver id')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'from': '58473c2ad561d5eafcf5',
    'to': '62393738957e18bbe5az',
    'amount': '50'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/transfer', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/transfer?from=58473c2ad561d5eafcf5&to=62393738957e18bbe5az&amount=50')

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Valid but nonexistent receiver id')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'from': '58473c2ad561d5eafcf5',
    'to': '62393738957e18bbe5a1',
    'amount': '50'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/transfer', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 404 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/transfer?from=58473c2ad561d5eafcf5&to=62393738957e18bbe5a1&amount=50')

if len(json.loads(r.text)) == 1 and r.status_code == 404 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Negative amount (-50)')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'from': '58473c2ad561d5eafcf5',
    'to': '62393738957e18bbe5a3',
    'amount': '-50'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/transfer', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/transfer?from=58473c2ad561d5eafcf5&to=62393738957e18bbe5a3&amount=-50')

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Insufficient amount (1000000000.1)')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'from': '58473c2ad561d5eafcf5',
    'to': '62393738957e18bbe5a3',
    'amount': '-50'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/transfer', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/transfer?from=58473c2ad561d5eafcf5&to=62393738957e18bbe5a3&amount=1000000000.1')

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Transfer less than the minimum unit value (1.001)')
print(tab * 2, 'JSON:', end = ' ')

data = {
    'from': '58473c2ad561d5eafcf5',
    'to': '62393738957e18bbe5a3',
    'amount': '1.001'
}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/transfer', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/transfer?from=58473c2ad561d5eafcf5&to=62393738957e18bbe5a3&amount=1.001')

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1


## POST api/divert

print('10. POST api/divert')
print(tab * 1, 'Divert transaction with id 989ad9fa-3b7d-492c-bc08-3b3ffa4a9967')
print(tab * 2, 'JSON:', end = ' ')

data = {'id': '989ad9fa-3b7d-492c-bc08-3b3ffa4a9967'}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/divert', headers = headers, data = data)

if isTransactionId(json.loads(r.text)['trans_id']) and len(json.loads(r.text)) == 3 and r.status_code == 200:
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Divert transaction with id e9ce4204-c31a-43f2-bc34-59a4b4986b04')
print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/divert?id=e9ce4204-c31a-43f2-bc34-59a4b4986b04')

if isTransactionId(json.loads(r.text)['trans_id']) and len(json.loads(r.text)) == 3 and r.status_code == 200:
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Invalid request parameters')
print(tab * 2, 'JSON:', end = ' ')

data = {'dummy': '989ad9fa-3b7d-492c-bc08-3b3ffa4a9967'}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/divert', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/divert?dummy=989ad9fa-3b7d-492c-bc08-3b3ffa4a9967')

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Multiple request parameters')
print(tab * 2, 'JSON:', end = ' ')

data = {'id': '989ad9fa-3b7d-492c-bc08-3b3ffa4a9967', 'dummy': 'Dummy'}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/divert', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/divert?id=989ad9fa-3b7d-492c-bc08-3b3ffa4a9967&dummy=Dummy')

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Invalid transaction id')
print(tab * 2, 'JSON:', end = ' ')

data = {'id': '989ad9fa-3b7d-492c-bc08-3b3ffa4a996z'}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/divert', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/divert?id=989ad9fa-3b7d-492c-bc08-3b3ffa4a996z')

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Valid but nonexistent transaction id')
print(tab * 2, 'JSON:', end = ' ')

data = {'id': '989ad9fa-3b7d-492c-bc08-3b3ffa4a9961'}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/divert', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 404 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/divert?id=989ad9fa-3b7d-492c-bc08-3b3ffa4a9961')

if len(json.loads(r.text)) == 1 and r.status_code == 404 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Transaction has no receiver')
print(tab * 2, 'JSON:', end = ' ')

data = {'id': '5ded2e9a-a1c5-41ed-ad80-0ce18c4d5da0'}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/divert', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/divert?id=5ded2e9a-a1c5-41ed-ad80-0ce18c4d5da0')

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 1, 'Ex receiver balance is no more enough')
print(tab * 2, 'JSON:', end = ' ')

data = {'id': '123e4567-e89b-12d3-a456-426614174000'}
data = json.dumps(data)
headers = { "Content-Type": "application/json" }
r = requests.post('http://127.0.0.1:5000/api/divert', headers = headers, data = data)

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print(tab * 2, 'URL-Encoded:', end = ' ')

r = requests.post('http://127.0.0.1:5000/api/divert?id=123e4567-e89b-12d3-a456-426614174000')

if len(json.loads(r.text)) == 1 and r.status_code == 400 and list(json.loads(r.text).keys())[0] == 'error':
    print(Fore.GREEN + 'Done!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
else:
    print(Fore.RED + 'Error!' + Style.RESET_ALL + '(' + str(r.status_code) + ')')
    errors += 1

print('\n--------------------------------\n')

if errors == 0:
    print(Fore.GREEN + 'All tests successfully passed. ' + Style.RESET_ALL + 'No errors where found')
else:
    print(Fore.RED + 'Some tests did not pass. ' + Style.RESET_ALL + str(errors) + ' errors where found during the testing process')