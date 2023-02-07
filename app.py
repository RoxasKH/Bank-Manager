from flask import Flask, render_template, request, jsonify, Response
from datetime import datetime
import secrets, sqlite3, uuid, requests, json

app = Flask(__name__)

HOST_APP_URL = 'http://127.0.0.1:5000'
DB_PATH = 'database.db'

def connect():
	connection = sqlite3.connect(DB_PATH)
	connection.row_factory = sqlite3.Row
	return connection

def createAccountId():
	return secrets.token_hex(10)

def createTransactionId():
	return str(uuid.uuid4())

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

def stringToDateTime(s):
	return datetime.strptime(s, '%Y-%m-%d %H:%M:%S')

def getBalance(idx):
	connection = connect()
	balance_cursor = connection.cursor().execute('SELECT balance FROM accounts WHERE id = ?', (idx,))

	columns = [column[0] for column in balance_cursor.description]

	balance_list = []
	for row in balance_cursor.fetchall():
		balance_list.append(dict(zip(columns, row)))

	return float(balance_list[0]['balance'])

def checkId(idx):
	connection = connect()
	accounts = connection.cursor().execute('SELECT name FROM accounts WHERE id = ?', (idx,))
	columns = [column[0] for column in accounts.description]
	results = []
	for row in accounts.fetchall():
	    results.append(dict(zip(columns, row)))
	connection.close()
	return results

def checkTransactionId(idx):
	connection = connect()
	accounts = connection.cursor().execute('SELECT accountId FROM transactions WHERE id = ?', (idx,))
	columns = [column[0] for column in accounts.description]
	results = []
	for row in accounts.fetchall():
	    results.append(dict(zip(columns, row)))
	connection.close()
	return results

def nameOrSurname(request):

	parameters = []

	if(request.headers.get('Content-Type') == 'application/json'):
		if(len(request.json) != 1):
			return 'invalid request parameters'
		elif(list(request.json.keys())[0] == 'name'):
			parameters = ['name', request.json['name']]
		elif(list(request.json.keys())[0] == 'surname'):
			parameters = ['surname', request.json['surname']]
		else:
			return 'invalid request parameters'
	else:
		if(len(request.args) != 1):
			return 'invalid request parameters'
		elif(list(request.args.keys())[0] == 'name'):
			parameters = ['name', request.args['name']]
		elif(list(request.args.keys())[0] == 'surname'):
			parameters = ['surname', request.args['surname']]
		else:
			return 'invalid request parameters'

	return parameters



@app.route('/')
def index():
	return render_template('index.html')


@app.route('/transfer')
def transfer_gui():
	return render_template('transfer.html')


@app.route('/api/account', methods = ['GET', 'POST', 'DELETE'])
def accounts():
	match request.method:
		case 'POST':
			try:
				idx = createAccountId()

				if(request.headers.get('Content-Type') == 'application/json'):

					keys = list(request.json.keys())

					if((len(request.json) == 2) and ((keys[0] == 'surname' and keys[1] == 'name') or (keys[0] == 'name' and keys[1] == 'surname'))):
						name = request.json['name']
						surname = request.json['surname']
					else:
						return jsonify({'error': 'invalid request parameters'}), 400

				else:

					keys = list(request.args.keys())

					if((len(request.args) == 2) and ((keys[0] == 'surname' and keys[1] == 'name') or (keys[0] == 'name' and keys[1] == 'surname'))):
						name = request.args['name']
						surname = request.args['surname']
					else:
						return jsonify({'error': 'invalid request parameters'}), 400

				connection = connect()
				connection.execute(
					'INSERT INTO accounts (id, name, surname) VALUES (?, ?, ?)',
					(idx, name, surname)
				)
				connection.commit()
				connection.close()
				return jsonify({'id':idx})

			except Exception as e:
				return jsonify({'error': str(e)}), 500

		case 'DELETE':
			try:
				if(request.headers.get('Content-Type') == 'application/json'):

					keys = list(request.json.keys())

					if(len(request.json) != 1 or keys[0] != 'id'):
						return jsonify({'error': 'invalid request parameters'}), 400

					idx = request.json['id']
				else:

					keys = list(request.args.keys())

					if(len(request.args) != 1 or keys[0] != 'id'):
						return jsonify({'error': 'invalid request parameters'}), 400

					idx = request.args.get('id')

				if(isId(idx)):

					if(checkId(idx) == []):
						return jsonify({'error': 'ID not found'}), 404

					connection = connect()
					connection.execute('DELETE FROM accounts WHERE id = ?', (idx,))
					connection.commit()
					connection.close()
					return jsonify({'status': 'Account '+ idx +' deleted successfully.'})
				else:
					return jsonify({'error': 'invalid ID'}), 400

			except Exception as e:
				return jsonify({'error': str(e)}), 500
			
			
		case _:
			try:
				connection = connect()
				accounts = connection.cursor().execute('SELECT * FROM accounts')
				columns = [column[0] for column in accounts.description]
				results = []
				for row in accounts.fetchall():
				    results.append(dict(zip(columns, row)))
				connection.close()
				return jsonify(results)

			except Exception as e:
				return jsonify({'error': str(e)}), 500


@app.route('/api/account/<string:idx>', methods = ['GET', 'POST', 'PUT', 'PATCH', 'HEAD'])
def account(idx):

	if(isId(idx)):
		
		if(checkId(idx) == []):
			return jsonify({'error': 'ID not found'}), 404


		match request.method:
			case 'POST':

				try:
					trans_id = createTransactionId()

					if(request.headers.get('Content-Type') == 'application/json'):

						keys = list(request.json.keys())

						if(len(request.json) != 1 or keys[0] != 'amount'):
							return jsonify({'error': 'invalid request parameters'}), 400

						amount = float(request.json['amount'])

					else:

						keys = list(request.args.keys())

						if(len(request.args) != 1 or keys[0] != 'amount'):
							return jsonify({'error': 'invalid request parameters'}), 400

						amount = float(request.args.get('amount'))

					balance = getBalance(idx);

					if(amount < 0 and (balance + amount) < 0):
						return jsonify({'error': 'insufficient balance'}), 400
					elif(len(str(amount).rsplit('.')[-1]) > 2):
						return jsonify({'error': 'minimum unit value is 0.01'}), 400
					else:
						connection = connect()
						connection.execute(
							'INSERT INTO transactions (id, amount, accountId) VALUES (?, ?, ?)',
							(trans_id, amount, idx)
						)
						connection.execute('UPDATE accounts SET balance = ? WHERE id = ?', (str(balance + amount), idx))
						connection.commit()
						connection.close()

						updated_balance = getBalance(idx)

						return jsonify({'updated_balance':str(updated_balance), 'trans_id':trans_id})
				
				except Exception as e:
					return jsonify({'error': str(e)}), 500

			case 'PUT':

				try:
					if(request.headers.get('Content-Type') == 'application/json'):

						keys = list(request.json.keys())

						if((len(request.json) == 2) and ((keys[0] == 'surname' and keys[1] == 'name') or (keys[0] == 'name' and keys[1] == 'surname'))):
							name = request.json['name']
							surname = request.json['surname']
						else:
							return jsonify({'error': 'invalid request parameters'}), 400

					else:

						keys = list(request.args.keys())

						if((len(request.args) == 2) and ((keys[0] == 'surname' and keys[1] == 'name') or (keys[0] == 'name' and keys[1] == 'surname'))):
							name = request.args['name']
							surname = request.args['surname']
						else:
							return jsonify({'error': 'invalid request parameters'}), 400

					connection = connect()
					connection.execute('UPDATE accounts SET name = ?, surname= ? WHERE id = ?', (name, surname, idx))
					connection.commit()
					connection.close()

					return jsonify({'status': 'Data updated successfully'})

				except Exception as e:
					return jsonify({'error': str(e)}), 500

			case 'PATCH':

				try:
					parameters = nameOrSurname(request)

					if(parameters[0] == 'name' or parameters[0] == 'surname'):

						connection = connect()

						query = 'UPDATE accounts SET ' + parameters[0] + ' = ? WHERE id = ?'

						connection.execute(query, (parameters[1], idx))
						connection.commit()
						connection.close()

						return jsonify({'status': 'Data updated successfully'})

					else:
						return jsonify({'error': parameters}), 400

				except Exception as e:
					return jsonify({'error': str(e)}), 500

			case 'HEAD':

				try:
					connection = connect()
					account_cursor = connection.cursor().execute('SELECT name, surname FROM accounts WHERE id = ?', (idx,))

					columns = [column[0] for column in account_cursor.description]
					account = []
					for row in account_cursor.fetchall():
					    account.append(dict(zip(columns, row)))
					
					name = account[0]['name']
					surname = account[0]['surname']

					connection.close()

					return Response(headers = {'X-Sistema-Bancario': name + ';' + surname})

				except Exception as e:
					return jsonify({'error': str(e)}), 500

			case _:

				try:
					connection = connect()
					account = connection.cursor().execute('SELECT name, surname, balance FROM accounts WHERE id = ?', (idx,))
					transactions = connection.cursor().execute(
						'SELECT T.id, data, receiver FROM accounts as A JOIN transactions as T ON A.id = T.accountId WHERE A.id = ?', 
						(idx,)
					)

					# get columns name for account table
					columns = [column[0] for column in account.description]

					results = []
					for row in account.fetchall():
					    results.append(dict(zip(columns, row)))

					# reget columns name, this time for transaction table
					columns = [column[0] for column in transactions.description]

					transactions_id_list = []
					for row in transactions.fetchall():
					    transactions_id_list.append(dict(zip(columns, row)))

					# datetime conversion isn't really needed to sort as it would sort anyway alphabetically on strings
					ordered_transactions_id_list = sorted(transactions_id_list, key = lambda k: stringToDateTime(k['data']))

					results[0]['transactions'] = ordered_transactions_id_list

					name = results[0]['name']
					surname = results[0]['surname']

					response = jsonify(results)

					connection.close()

					# you can return tuples in the form of (response, status), (response, headers), or (response, status, headers)
					return jsonify(results), {'X-Sistema-Bancario': name + ';' + surname}

				except Exception as e:
					return jsonify({'error': str(e)}), 500

	else:
		return jsonify({'error': 'invalid ID'}), 400


@app.route('/api/transfer', methods = ['POST'])
def transfer():

	try:
		trans_id = createTransactionId()

		if(request.headers.get('Content-Type') == 'application/json'):

			keys = list(request.json.keys())
			parameter_string = 'fromtoamount'

			for x in keys:
				parameter_string = parameter_string.replace(x, '', 1)

			if((len(request.json) == 3) and (parameter_string == '')):
				sender_id = request.json['from']
				receiver_id = request.json['to']
				amount = float(request.json['amount'])
			else:
				return jsonify({'error': 'invalid request parameters'}), 400

		else:

			keys = list(request.args.keys())
			parameter_string = 'fromtoamount'

			for x in keys:
				parameter_string = parameter_string.replace(x, '', 1)

			if((len(request.args) == 3) and (parameter_string == '')):
				sender_id = request.args['from']
				receiver_id = request.args['to']
				amount = float(request.args['amount'])
			else:
				return jsonify({'error': 'invalid request parameters'}), 400

		if(isId(sender_id)):
			if(checkId(sender_id) == []):
				return jsonify({'error': 'sender ID not found'}), 404
		else:
			return jsonify({'error': 'invalid sender ID'}), 400

		if(isId(receiver_id)):
			if(checkId(receiver_id) == []):
				return jsonify({'error': 'receiver ID not found'}), 404
		else:
			return jsonify({'error': 'invalid receiver ID'}), 400

		initial_sender_balance = getBalance(sender_id)
		initial_receiver_balance = getBalance(receiver_id)

		if(amount < 0):
			return jsonify({'error': 'amount should be a positive number'}), 400
		elif(amount > 0 and (initial_sender_balance - amount) < 0):
			return jsonify({'error': 'insufficient balance'}), 400
		elif(len(str(amount).rsplit('.')[-1]) > 2):
			return jsonify({'error': 'minimum unit value is 0.01'}), 400
		else:
			connection = connect()

			connection.execute(
				'INSERT INTO transactions (id, amount, accountId, receiver) VALUES (?, ?, ?, ?)',
				(trans_id, amount, sender_id, receiver_id)
			)

			if(sender_id != receiver_id):
				connection.execute('UPDATE accounts SET balance = ? WHERE id = ?', (str(initial_sender_balance - amount), sender_id))
				connection.execute('UPDATE accounts SET balance = ? WHERE id = ?', (str(initial_receiver_balance + amount), receiver_id))

			connection.commit()
			connection.close()

			updated_sender_balance = getBalance(sender_id)
			updated_receiver_balance = getBalance(receiver_id)

			return jsonify({sender_id:str(updated_sender_balance), receiver_id:str(updated_receiver_balance), 'trans_id':trans_id})

	except Exception as e:
		return jsonify({'error': str(e)}), 500


@app.route('/api/divert', methods = ['POST'])
def divert():

	try:
		trans_id = createTransactionId()

		if(request.headers.get('Content-Type') == 'application/json'):

			keys = list(request.json.keys())

			if(len(request.json) != 1 or keys[0] != 'id'):
				return jsonify({'error': 'invalid request parameters'}), 400

			divert_id = request.json['id']

		else:

			keys = list(request.args.keys())

			if(len(request.args) != 1 or keys[0] != 'id'):
				return jsonify({'error': 'invalid request parameters'}), 400

			divert_id = request.args['id']

		if(not isTransactionId(divert_id)):
			return jsonify({'error': 'invalid transaction ID'}), 400

		if(checkTransactionId(divert_id) == []):
			return jsonify({'error': 'transaction ID not found'}), 404

		connection = connect()
		old_transaction_cursor = connection.cursor().execute('SELECT amount, accountId, receiver FROM transactions WHERE id = ?', (divert_id,))

		columns = [column[0] for column in old_transaction_cursor.description]
		old_transaction = []
		for row in old_transaction_cursor.fetchall():
		    old_transaction.append(dict(zip(columns, row)))

		ex_receiver = old_transaction[0]['receiver']
		ex_sender = old_transaction[0]['accountId']
		amount = float(old_transaction[0]['amount'])

		connection.close()

		if(ex_receiver is None):
			return jsonify({'error': 'transaction invalid for divert, no receiver found'}), 400
		elif(getBalance(ex_receiver) - amount < 0): # no need to check if amount < 0 as it wouldn't have a receiver either
			return jsonify({'error': 'cannot divert transaction, ex receiver balance is not enough'}), 400
		else:
			sender = ex_receiver
			receiver = ex_sender
			divert = requests.post(HOST_APP_URL + '/api/transfer', headers = {'Content-Type': 'application/json'}, json = {'from': sender, 'to': receiver, 'amount': str(amount)})
			return divert.content, divert.status_code

	except Exception as e:
		return jsonify({'error': str(e)}), 500