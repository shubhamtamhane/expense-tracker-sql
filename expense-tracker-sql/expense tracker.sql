USE expense_tracker;

CREATE TABLE userdata(
  UID INT NOT NULL AUTO_INCREMENT,
  FirstName VARCHAR(45) NOT NULL,
  LastName VARCHAR(45) NULL,
  email VARCHAR(45) NOT NULL,
  state VARCHAR(45) NULL,
  country VARCHAR(45) NULL,
  password VARCHAR(45) NOT NULL,
  phone VARCHAR(10) NULL,
  PRIMARY KEY (UID));

Select * FROM userdata;

INSERT INTO userdata(FirstName, LastName, email, state, country, password, phone) VALUES ('sripal', 'Nomula', 'srnomula@iu.edu', 'IN', 'US', 'password', '6692462594');

-- Creating tables for distinct categories of data
CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL
);
INSERT INTO Categories (Name) VALUES ('food'), ('accomodation'), ('activities'), ('travel'), ('groceries'), ('dining'), ('education'), ('online'), ('salary');
ALTER TABLE Categories CHANGE column Name category varchar(255);

CREATE TABLE PaymentMethods (
    PaymentMethodID INT PRIMARY KEY AUTO_INCREMENT,
    Method VARCHAR(255) NOT NULL
);
INSERT INTO PaymentMethods (Method) VALUES ('cash'), ('credit-traveld'), ('coupon');
Select * FROM PaymentMethods;

CREATE TABLE Locations (
    LocationID INT PRIMARY KEY AUTO_INCREMENT,
    city VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL
);
INSERT INTO Locations (city, country) VALUES ('chicago', 'USA'), ('fremont', 'USA');
Select * FROM Locations;


DROP TABLE Transactions;

CREATE TABLE Transactions (
    TransactionID INT PRIMARY KEY AUTO_INCREMENT,
    Date DATE NOT NULL,
    CategoryID INT,
    PaymentMethodID INT,
    LocationID INT,
    Amount DECIMAL(10, 2),
    Details VARCHAR(255),
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID),
    FOREIGN KEY (PaymentMethodID) REFERENCES PaymentMethods(PaymentMethodID),
    FOREIGN KEY (LocationID) REFERENCES Locations(LocationID)
);
Alter table Transactions
ADD COLUMN UID INT;

ALTER TABLE transactions 
ADD CONSTRAINT fk  FOREIGN KEY (UID) REFERENCES userdata(UID) ON DELETE NO ACTION ON UPDATE NO ACTION;

DELETE FROM Transactions;
ALTER TABLE transactions AUTO_INCREMENT = 1;



-- Populating the Transactions table data
INSERT INTO Transactions (Date, CategoryID, PaymentMethodID, LocationID, Amount, Details, UID) VALUES
('2018-09-19', 
(SELECT CategoryID FROM Categories WHERE category = 'food'), 
(SELECT PaymentMethodID FROM PaymentMethods WHERE Method = 'cash'), 
(SELECT LocationID FROM Locations WHERE city = 'chicago'), 
60.96, 'salad', 1);

DELETE FROM Transactions WHERE TransactionID = 2;
INSERT INTO Transactions (Date, CategoryID, PaymentMethodID, LocationID, Amount, Details, UID) VALUES
('2018-09-20', 
(SELECT CategoryID FROM Categories WHERE category = 'accomodation'), 
(SELECT PaymentMethodID FROM PaymentMethods WHERE Method = 'cash'), 
(SELECT LocationID FROM Locations WHERE city = 'fremont'), 
420, 'september', 1);

INSERT INTO Transactions (Date, CategoryID, PaymentMethodID, LocationID, Amount, Details, UID) VALUES
('2018-09-21', 
(SELECT CategoryID FROM Categories WHERE category = 'accomodation'), 
(SELECT PaymentMethodID FROM PaymentMethods WHERE Method = 'cash'), 
(SELECT LocationID FROM Locations WHERE city = 'fremont'), 
660, 'deposit', 1);

-- Repeat this pattern for each row of data you wish to insert


SELECT * FROM Transactions;
