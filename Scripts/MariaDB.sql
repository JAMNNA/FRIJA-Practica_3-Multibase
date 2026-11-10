CREATE DATABASE IF NOT EXISTS practica3
CHARACTER SET utf8mb4
COLLATE UTF8MB4_UNICODE_CI;

USE practica3;

-- ============================================================
-- 1. BRANCHES
-- ============================================================

CREATE TABLE branches (
    branch_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    address VARCHAR(150) NOT NULL,
    phone VARCHAR(15),
    status ENUM('ACTIVE','INACTIVE','CLOSED')
        NOT NULL DEFAULT 'ACTIVE',

    INDEX idx_branch_city (city)
) ENGINE=InnoDB;


-- ============================================================
-- 2. USERS
-- ============================================================

CREATE TABLE users (
    user_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    paternal_last_name VARCHAR(50) NOT NULL,
    maternal_last_name VARCHAR(50),
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(15),
    password VARCHAR(255),
    role ENUM(
        'ADMIN',
        'MANAGER',
        'SALES',
        'INVENTORY',
        'CUSTOMER'
    ) NOT NULL,
    branch_id INT UNSIGNED NULL,
    status ENUM(
        'ACTIVE',
        'SUSPENDED',
        'BLOCKED'
    ) NOT NULL DEFAULT 'ACTIVE',

    CONSTRAINT fk_user_branch
        FOREIGN KEY (branch_id)
        REFERENCES branches(branch_id),

    INDEX idx_user_branch (branch_id),
    INDEX idx_user_role (role),
    INDEX idx_user_status (status)
) ENGINE=InnoDB;

USE practica3;


ALTER TABLE users 
ADD COLUMN favorite_product_id VARCHAR(24) NULL AFTER branch_id;

SHOW TABLES;