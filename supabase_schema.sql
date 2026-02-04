CREATE TABLE items (
    id BIGSERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    location VARCHAR(255) NOT NULL,
    seller_name VARCHAR(255) NOT NULL,
    contact VARCHAR(255) NOT NULL,
    description TEXT
);