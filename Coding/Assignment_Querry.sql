Create database Assignment_Courrier_Management;
use Assignment_Courrier_Management;
use coding_Challenge2;

CREATE TABLE Courier (
    courierID INT IDENTITY(1,1) PRIMARY KEY,
    tracking_number BIGINT UNIQUE NOT NULL,
    sender_name VARCHAR(100) NOT NULL,
    sender_address VARCHAR(255) NOT NULL,
    receiver_name VARCHAR(100) NOT NULL,
    receiver_address VARCHAR(255) NOT NULL,
    weight DECIMAL(5,2) NOT NULL,
    status VARCHAR(50) NOT NULL,
    delivery_date DATE NULL,
    user_id INT NOT NULL
);

select * from Courier;

CREATE TABLE Employee (
    employeeID INT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    contact_number VARCHAR(15) NOT NULL,
    role VARCHAR(50) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL
);

select * from Employee;

CREATE TABLE Location (
    locationID INT IDENTITY(1,1) PRIMARY KEY,
    location_name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL
);

CREATE TABLE Payment (
    paymentID BIGINT IDENTITY(1,1) PRIMARY KEY,
    courierID INT NOT NULL FOREIGN KEY REFERENCES Courier(courierID),
    amount DECIMAL(10, 2) NOT NULL,
    payment_date DATE NOT NULL
);

CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,  -- Remove IDENTITY property
    employee_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    contact_number VARCHAR(20) NOT NULL,
    role VARCHAR(50) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL
);


ALTER TABLE Courier ADD employeeID INT;
ALTER TABLE Courier ADD CONSTRAINT FK_Employee_Courier FOREIGN KEY (employeeID) REFERENCES Employee(employeeID);

--select * from Courier;
DROP TABLE Courier;
DROP DATABASE Assignment_Courrier_Management;



