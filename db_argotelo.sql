-- Active: 1782960658797@@gateway01.ap-southeast-1.prod.aws.tidbcloud.com@4000
use db_project_argotelo;

CREATE TABLE roles (
    id INT PRIMARY KEY AUTO_INCREMENT,
    role_name VARCHAR(30) NOT NULL UNIQUE
);

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,

    role_id INT NOT NULL,

    fullname VARCHAR(100) NOT NULL,

    username VARCHAR(50) NOT NULL UNIQUE,

    password VARCHAR(255) NOT NULL,

    email VARCHAR(100),

    phone VARCHAR(20),

    status ENUM('Active','Inactive') DEFAULT 'Active',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(role_id)
    REFERENCES roles(id)
);

CREATE TABLE categories (

    id INT PRIMARY KEY AUTO_INCREMENT,

    category_name VARCHAR(100) NOT NULL

);

CREATE TABLE menus (

    id INT PRIMARY KEY AUTO_INCREMENT,

    category_id INT,

    menu_name VARCHAR(100),

    description TEXT,

    price DECIMAL(12,2),

    image_url TEXT,

    status ENUM('Available','Unavailable')
    DEFAULT 'Available',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(category_id)
    REFERENCES categories(id)

);

CREATE TABLE suppliers (

    id INT PRIMARY KEY AUTO_INCREMENT,

    supplier_name VARCHAR(100),

    phone VARCHAR(20),

    address TEXT

);

CREATE TABLE inventories (

    id INT PRIMARY KEY AUTO_INCREMENT,

    supplier_id INT,

    item_name VARCHAR(100),

    unit VARCHAR(30),

    stock DECIMAL(10,2),

    minimum_stock DECIMAL(10,2),

    FOREIGN KEY(supplier_id)
    REFERENCES suppliers(id)

);

CREATE TABLE stock_logs (

    id INT PRIMARY KEY AUTO_INCREMENT,

    inventory_id INT,

    qty DECIMAL(10,2),

    type ENUM('IN','OUT'),

    note TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(inventory_id)
    REFERENCES inventories(id)

);

CREATE TABLE transactions (

    id INT PRIMARY KEY AUTO_INCREMENT,

    invoice_number VARCHAR(50) UNIQUE,

    cashier_id INT,

    subtotal DECIMAL(12,2),

    tax DECIMAL(12,2),

    total DECIMAL(12,2),

    payment_status ENUM(
        'Pending',
        'Paid',
        'Cancelled'
    ),

    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(cashier_id)
    REFERENCES users(id)

);

CREATE TABLE transaction_details (

    id INT PRIMARY KEY AUTO_INCREMENT,

    transaction_id INT,

    menu_id INT,

    quantity INT,

    price DECIMAL(12,2),

    subtotal DECIMAL(12,2),

    FOREIGN KEY(transaction_id)
    REFERENCES transactions(id),

    FOREIGN KEY(menu_id)
    REFERENCES menus(id)

);

CREATE TABLE payments (

    id INT PRIMARY KEY AUTO_INCREMENT,

    transaction_id INT,

    payment_method VARCHAR(50),

    midtrans_order_id VARCHAR(100),

    midtrans_transaction_id VARCHAR(100),

    payment_status VARCHAR(50),

    paid_at DATETIME,

    FOREIGN KEY(transaction_id)
    REFERENCES transactions(id)

);

CREATE TABLE attendance (

    id INT PRIMARY KEY AUTO_INCREMENT,

    user_id INT,

    check_in DATETIME,

    check_out DATETIME,

    status VARCHAR(30),

    FOREIGN KEY(user_id)
    REFERENCES users(id)

);

CREATE TABLE shifts (

    id INT PRIMARY KEY AUTO_INCREMENT,

    shift_name VARCHAR(50),

    start_time TIME,

    end_time TIME

);

show tables;