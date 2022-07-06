# ![Bank Manager Logo](static/favicon.ico?raw=true "Logo") - Bank Manager
> A simplified banking system webapp written with the help of the Flask Python framework.

![Bank Manager Showcase](showcase.png?raw=true "Showcase of the webapp")

The program allows the managing of a simplified banking system, defining accounts and their transactions, and offers basic banking services as:

- Account creation
- Account closure
- Deposit and withdrawal of money
- Moving money from one account to another

Exposing functionalities through REST endpoints and an HTML interface.

The request body can be in JSON format or URL-encoded format, as the program supports and is able to manage both.
The body of the response for a REST endpoint, if present, must always be in JSON format.

The project was successfully tested on Windows 10 Home 64-bit 21H1 build 19043.

## Table of Contents

- [Chosen languages for the implementation](#chosen-languages-for-the-implementation)
	- [Requirements](#requirements)
	- [Running the app](#running-the-app)
- [API (REST endpoints)](#api-rest-endpoints)
	- [/api/account](#apiaccount)
		- [GET:](#get)
		- [POST:](#post)
		- [DELETE:](#delete)
	- [/api/account/{accountId}](#apiaccountaccountId)
		- [GET:](#get)
		- [POST:](#post)
		- [PUT:](#put)
		- [PATCH:](#patch)
		- [HEAD:](#head)
	- [/api/transfer](#apitransfer)
		- [POST:](#post)
	- [/api/divert](#apidivert)
		- [POST:](#post)
- [Frontend GUI (HTML)](#frontend-gui-html)
	- [/ (the root endpoint of the server)](#-the-root-endpoint-of-the-server)
	- [/transfer](#transfer)
- [Testing](#testing)
- [Some details and resources](#some-details-and-resources)
- [Useful tools](#useful-tools)
	- [SQLite DB Browser](#sqlite-db-browser)
	- [Advanced REST Client (ARC)](advanced-rest-client-arc)


## Chosen languages for the implementation

For the webapp the following languages were used:

- Python with [Flask framework](https://flask.palletsprojects.com/en/2.1.x/) (and [Requests HTTP library](https://requests.readthedocs.io/en/latest/)): used for defining the REST api and managing the backend codes with queries to the database, and also for testing the app
- HTML5 + CSS3 + JavaScript with [Jquery framework](https://jquery.com/): used for the frontend part of the app, and so its GUI and [AJAX requests](https://api.jquery.com/jQuery.ajax/) to the REST endpoints
- [SQLite3](https://www.sqlite.org/index.html): for the local SQL database stored on the secondary memory

### Requirements

So, to run the app, you will need to install Python on your system (3.10 or later is needed, as the [_pattern matching_](https://docs.python.org/3.10/whatsnew/3.10.html#pep-634-structural-pattern-matching) match-case was used, the project was specifically coded and run on Python 3.10.5). Everything else you need is a modern browser of your choice.

After installing Python, you will need to install the Flask framework and Requests library through pip, launching these commands:

```sh
$ pip install flask
$ pip install requests
$ pip install colorama -- (this is just needed for the colored output during testing, but it should be preinstalled)
```

### Running the app

To run the webapp on your computer, you need to perform these steps:

1. Download the project folder
2. From your terminal, move to the project folder path
3. Run the `python init_db.py` command to initialize the SQL database (some entries are automatically added to the db in this step as they're needed for testing)
4. Run the `set FLASK_APP=app` command
5. Run the  `set FLASK_ENV=development` command
6. At last, run the `flask run` command to start the local server.

You can now access the app at the localhost webaddress on the 5000 port, and so through http://localhost:5000/ or http://127.0.0.1:5000/.

Remember that this sends you to the main GUI page, but you can also check the API endpoints through your browser.

Alternatively, on windows you can run the `run_server.bat` batch file in the project folder to start the server. Keep in mind that this batch file contains the python commands as well, and therefore it'll reinitialize the SQLite3 database everytime you launch it.


## API (REST endpoints)

The server implements the following endpoints with their HTTP methods:


### /api/account

##### GET:
returns the list of all accounts in the system.
##### POST:
create a new account with the following fields:
```sh
name
surname
```
and the new id of the account created is returned in the response body. 
The id of an account is one 20-character string representing a sequence of bytes, generated randomly if necessary, encoded in hexadecimal (for example, an _accountId_ could be `1087b347f1a59277eb98`).
##### DELETE:
delete the account with the _id_ specified by the URL id parameter.


### /api/account/{accountId}

##### GET: 
returns the _name_ and _surname_ of the owner as well as the _balance_ with a list of the identifiers of all _transactions_ carried out by _accountId_, in chronological order ascending (from the oldest to the most recent).
Also, it introduces a response header with **X-Sistema-Bancario** key. The header value must express the name and surname of the owner in the format `name;surname`.
##### POST: 
make a deposit of money with an amount specified by the _amount_ key in the body of the request. 
If amount is negative, a withdrawal is made. In case of negative amount, the server generates an error if the account balance is insufficient, informing the client of the failure.
If successful, in the body of the response the new account balance is returned and a _deposit/withdrawal ID_ in **UUID v4** format.
##### PUT:
change (overwrite) name and surname of the account owner. In the body therefore the following keys must be present:
```sh
name
surname
```
##### PATCH:
change (overwrite) name or surname of the account owner. In the body must therefore be present only one of the following keys:
```sh
name
surname
```
##### HEAD:
Returns the owner's first and last name in a keyed response header **X-Banking-System**. The header value is in `name;surname` format.
There is no response body.


### /api/transfer

##### POST:
make a movement of money with a positive amount from an account to a other.
_amount_ is specified in the request body. The server generates an error if the balance of the starting account is not sufficient, informing the client of the failure.
If successful, the new account _balances_ are returned in the body of the response involved in the transaction, separated by _accountId_ and a _transaction identifier_ in **UUID v4** format.
The body of the request therefore has the following fields:
```sh
from
to
amount
```

### /api/divert

##### POST:
cancels a transaction with the id specified by the _id_ key in the request body that is.
It creates a new transaction with a new **UUID v4** that reverses the transfer of money between the accounts affected by the transaction with identification _id_ of the amount that the transaction involved, but only if the balance of the previous account beneficiary allows this operation. Otherwise it generates an appropriate error.


## Frontend GUI (HTML)
The HTML resources offered by the server must be offered by the enpoints indicated with the following functionality.

Both pages have input control logic before sending a request to the backend. For example, if a user enters an account that does not consist of 20 hexadecimal digits, the page gives an error without attempting to send a request to the backend.
That said, the backend always re-checks the input before processing the request. If the input is incorrect, it returns an appropriate error that the page is able to report to the user.

This input control logic was implemented with [Client-side form validation](https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation).

The pages are able to display errors with an appropriate message to the users when they occurs thanks to the implementation of the `error` function of the _jquery $.ajax_ method.


### / (the root endpoint of the server)
this HTML page shows the user a prompt with a text field in which to enter an _account identifier_ and, at the press of a button, the page is populated with information regarding the owner of the account and the history of transactions with any associated recipient of the move money (not present if it was a withdrawal/deposit) and the amount involved, without reloading that is, without a new GET request to the endpoint `/`.
Requests for whatever nature to other endpoints are obviously granted to retrieve the information of the account to be shown on the page.
The transactions shown by the page are ordered by date.
All information as described are displayed in an HTML table.
In case of insertion of a new account number and subsequent pressing of the button, the page repopulates with information regarding the new account no longer showing any data from the old one.

### /transfer
this HTML page shows the user a prompt with three text fields in which to enter _sender_ account, _receiver_ account and an _amount_ to transfer, and, pressing a button, the relevant transaction must be registered in the system.
Page also provides feedback to the user regarding the outcome of the operation.


## Testing

It is possible to run a test of the webapp funcionalities.

In order to do this, open another terminal in your project folder and run the command

```sh
python test.py
```

_Note: keep in mind that the testing is based on the database entries that are generated when the database is initialized. If you run the test multiple times, it's certain that you'll encounter some error in the testing process due to insufficient amount for withdrawals after the first testing or other problems. To make sure the tests pass, remember to reinitialize the database as described above before running the testing script._

Below here you can see an example of a successful testing session.

![Tests](tests.png?raw=true "Tests")

## Some details and resources

In Flask, headers and status codes can be returned along with the [response as a tuple](https://flask.palletsprojects.com/en/2.1.x/quickstart/#about-responses) in one of the following forms

```sh
(response, status),
(response, headers),
(response, status, headers).
```
The status value will override the status code and headers can be a list or dictionary of additional header values.

Way of [getting the data received in a Flask request](https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request).

[Python uuid module](https://docs.python.org/3/library/uuid.html) was used to generate UUID v4 transactions IDs.

[Python secrets module](https://docs.python.org/3/library/secrets.html) was used to generate 20-character hex accounts IDs.

To check if account IDs were hexadecimal, integer conversion check was used as is [more efficient in most cases](https://stackoverflow.com/questions/11592261/check-if-a-string-is-hexadecimal).

Webapp favicon was created with [Text to Favicon Generator](https://favicon.io/favicon-generator/).

_Settings:_
```sh
color: #FFF
background-color: #00B3A6
text: B
background: rounded
font-family: leckerly-one
font-variant: regular 400 normal
font-size: 110
```

CSS loading div made with [Pure CSS Loaders](https://loading.io/css/) (even if you'll probably barely see it).

[Material design](https://material.io/design/color/dark-theme.html#anatomy) was used (probably not in the best way) as a guideline/inspiration for the webapp palette.
This was the [exact palette followed](https://lh3.googleusercontent.com/Cevz7vdDQhFJ4fDf9p12CfO7kS3mETAzkyDavYS0cPKHjZh6RZvg8rv1AE3SLS8xdqEOH-1s8q2gw0Hq29phLqcWVHWTSvotFDk2=w1064-v0).

Validation Errors [can be customized using CSS](https://www.cognitoforms.com/blog/106/css-tips-and-tricks-for-customizing-error-messages).

For a detailed description of HTTP Codes, you can check [RCF](https://www.rfc-editor.org/rfc/rfc7231).

400 HTTP code was used for well formed but invalid IDs instead of 422 due to reasons that can be found [here](https://softwareengineering.stackexchange.com/questions/329229/should-i-return-an-http-400-bad-request-status-if-a-parameter-is-syntactically).

[SQLite CURRENT_TIMESTAMP](https://www.sqlite.org/lang_datefunc.html) is UTC (or GMT).

The transaction amounts are saved as strings in the database due to inconsistency SQLite3 problems and suitably converted into float on the backend side, otherwise there would have been unwanted approximations and [`DECIMAL (10, 2)` could not be used to truncate results](https://stackoverflow.com/questions/21757722/how-to-use-sqlite-decimal-precision-notation).
_Note: some approximations are still happening, and i have no idea why._

## Useful tools

A list of tools that may be useful when developing and testing a similar webapp.

### SQLite DB Browser

This can be used to check the current state of the SQLite 3 database graphically on Windows.
https://sqlitebrowser.org/

### Advanced REST Client (ARC)

This can be used to make HTTP requests to the API for further testing as an alternative to the more known Postman. It's open-source, made in Electron and doesn't need an account.
https://install.advancedrestclient.com/install