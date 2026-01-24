-- ======================================
-- Database: de_ecomm
-- Purpose: Create schema for DE project
-- ======================================

DROP DATABASE IF EXISTS de_ecomm;

CREATE DATABASE de_ecomm;

USE de_ecomm;

-- =========================================
-- DIMENSION TABLES
-- =========================================

-- =====================
-- TABLE: products
-- =====================

CREATE TABLE products (
  product_id INT PRIMARY KEY,
  product_name VARCHAR(100),
  category VARCHAR(50),
  supplier_id INT,
  cost_price DECIMAL(10, 2)
);

-- =====================
-- TABLE: customers
-- =====================

CREATE TABLE customers (
  customer_id INT PRIMARY KEY,
  customer_name VARCHAR(100),
  email VARCHAR(100),
  phone VARCHAR(25),
  city VARCHAR(75),
  state VARCHAR(75),
  country VARCHAR(75)
);

-- =====================
-- TABLE: suppliers
-- =====================
CREATE TABLE suppliers (
  supplier_id INT PRIMARY KEY,
  supplier_name VARCHAR(100),
  email VARCHAR(100),
  phone VARCHAR(25),
  city VARCHAR(75),
  state VARCHAR(75),
  country VARCHAR(75)
);

-- =====================
-- TABLE: stores
-- =====================

CREATE TABLE stores (
  store_id INT PRIMARY KEY,
  store_name VARCHAR(100),
  city VARCHAR(75),
  state VARCHAR(75),
  country VARCHAR(75)
);

-- =====================
-- TABLE: warehouses
-- =====================
CREATE TABLE warehouses (
  warehouse_id INT PRIMARY KEY,
  warehouse_name VARCHAR(100),
  city VARCHAR(75),
  state VARCHAR(75),
  country VARCHAR(75)
);

-- =========================================
-- FACT TABLES
-- =========================================

-- =====================
-- TABLE: sales
-- =====================
CREATE TABLE sales (
  sale_id INT,
  sale_date DATE,
  product_id INT,
  customer_id INT,
  store_id INT,
  quantity INT,
  unit_price DECIMAL(10, 2),
  PRIMARY KEY (sale_id, product_id)
);

-- =====================
-- TABLE: returns
-- =====================
CREATE TABLE returns (
  return_id INT PRIMARY KEY,
  sale_id INT,
  product_id INT,
  return_date DATE,
  quantity_returned INT,
  unit_price DECIMAL(10,2)
);

-- =====================
-- TABLE: inventory
-- =====================
CREATE TABLE inventory (
  inventory_id INT PRIMARY KEY,
  product_id INT,
  warehouse_id INT,
  quantity_available INT,
  snapshot_date DATE
);
