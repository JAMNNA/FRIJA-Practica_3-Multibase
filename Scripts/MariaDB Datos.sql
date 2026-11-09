-- Datos de prueba
USE practica3;

INSERT INTO branches
(branch_id, name, city, address, phone, status)
VALUES
(1, 'Tijuana Branch', 'Tijuana', 'Zona Centro', '6641234567', 'ACTIVE'),
(2, 'Mexicali Branch', 'Mexicali', 'Zona Centro', '6861234567', 'ACTIVE'),
(3, 'Monterrey Branch', 'Monterrey', 'Zona Centro', '8181234567', 'ACTIVE'),
(4, 'Guadalajara Branch', 'Guadalajara', 'Zona Centro', '3311234567', 'ACTIVE');

INSERT INTO users
(
    user_id,
    first_name,
    paternal_last_name,
    maternal_last_name,
    email,
    phone,
    password,
    role,
    branch_id,
    STATUS,
    favorite_product_id
)
VALUES
(1, 'Carlos', 'Ramirez', 'Lopez',
 'admin@frija.com', '6641111111', '$2b$12$HASH_DE_PRUEBA',
 'ADMIN', 1, 'ACTIVE','6af02c51f6632370424847a3'),

(2, 'Ana', 'Garcia', 'Torres',
 'manager@frija.com', '6642222222', '$2b$12$HASH_DE_PRUEBA',
 'MANAGER', 1, 'ACTIVE','6af02c51f6632370424847a4'),

(3, 'Luis', 'Hernandez', 'Mora',
 'sales@frija.com', '6863333333', '$2b$12$HASH_DE_PRUEBA',
 'SALES', 2, 'ACTIVE','6af02c51f6632370424847a5'),

(4, 'Maria', 'Fernandez', 'Cruz',
 'inventory@frija.com', '8184444444', '$2b$12$HASH_DE_PRUEBA',
 'INVENTORY', 3, 'ACTIVE','6af02c51f6632370424847a6'),

(5, 'Jorge', 'Sanchez', 'Diaz',
 'customer@frija.com', '3315555555', '$2b$12$HASH_DE_PRUEBA',
 'CUSTOMER', NULL, 'ACTIVE','6af02c51f6632370424847a7');
 
 SELECT * FROM users;
 
