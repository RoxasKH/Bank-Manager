DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS transactions;

CREATE TABLE accounts (
	id TEXT PRIMARY KEY NOT NULL,
	name TEXT NOT NULL,
	surname TEXT NOT NULL,
	balance TEXT DEFAULT '0' NOT NULL
);

CREATE TABLE transactions (
	id TEXT PRIMARY KEY NOT NULL,
	amount TEXT NOT NULL,
	accountId TEXT NOT NULL,
	data DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
	receiver TEXT
);


INSERT INTO accounts (id, name, surname, balance) VALUES ('58473c2ad561d5eafcf5', 'Chong', 'Xena', '1000.10');
INSERT INTO accounts (id, name, surname, balance) VALUES ('62393738957e18bbe5a3', 'Micheal', 'Morbius', '1000000000.10');
/* Should've been one morbillion, but i doubt a variable type can handle 100 x 34 Trillion, so i chose a pretty big number instead*/
/* Source: https://www.urbandictionary.com/define.php?term=morbillion*/
INSERT INTO accounts (id, name, surname, balance) VALUES ('2c543e03a7054e2185d1', 'Dummy', 'Account', '0');
INSERT INTO accounts (id, name, surname, balance) VALUES ('61bb03b09fab16342174', 'Dummy2', 'Account', '0');

INSERT INTO transactions (id, amount, accountId, data) VALUES ('b6b03036-6a91-4f1d-a2f3-a6ece0e2569a', '-100', '58473c2ad561d5eafcf5', '2022-06-10 14:37:00');
INSERT INTO transactions (id, amount, accountId, data) VALUES ('5ded2e9a-a1c5-41ed-ad80-0ce18c4d5da0', '300', '58473c2ad561d5eafcf5', '2021-06-10 14:37:00');

INSERT INTO transactions (id, amount, accountId, data, receiver) VALUES ('989ad9fa-3b7d-492c-bc08-3b3ffa4a9967', '300', '62393738957e18bbe5a3', '2021-06-10 14:37:00', '58473c2ad561d5eafcf5');
INSERT INTO transactions (id, amount, accountId, data, receiver) VALUES ('e9ce4204-c31a-43f2-bc34-59a4b4986b04', '200', '62393738957e18bbe5a3', '2021-06-10 14:37:00', '58473c2ad561d5eafcf5');
INSERT INTO transactions (id, amount, accountId, data, receiver) VALUES ('123e4567-e89b-12d3-a456-426614174000', '1000000', '62393738957e18bbe5a3', '2021-06-10 14:37:00', '58473c2ad561d5eafcf5');