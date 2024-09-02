CREATE TABLE BarraDeSonido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    volumenActual INT DEFAULT 50,
    entradaActual ENUM('HDMI', 'Bluetooth', 'AUX', 'Optical') DEFAULT 'HDMI',
    modoSonido ENUM('Bass Boost', 'Surround', 'Vocal Clarity', 'Dynamic', 'Standard') DEFAULT 'Standard'
);

INSERT INTO BarraDeSonido (marca, modelo, precio, volumenActual, entradaActual, modoSonido)
VALUES ('Sony', 'HT-S350', 299.99, 50, 'HDMI', 'Bass Boost');

INSERT INTO BarraDeSonido (marca, modelo, precio, volumenActual, entradaActual, modoSonido)
VALUES ('Samsung', 'HW-Q60T', 399.99, 60, 'Bluetooth', 'Surround');

INSERT INTO BarraDeSonido (marca, modelo, precio, volumenActual, entradaActual, modoSonido)
VALUES ('LG', 'SN5Y', 250.00, 40, 'AUX', 'Vocal Clarity');

INSERT INTO BarraDeSonido (marca, modelo, precio, volumenActual, entradaActual, modoSonido)
VALUES ('JBL', 'Bar 5.1', 499.99, 70, 'Optical', 'Dynamic');

INSERT INTO BarraDeSonido (marca, modelo, precio, volumenActual, entradaActual, modoSonido)
VALUES ('Bose', 'Soundbar 700', 799.00, 55, 'HDMI', 'Standard');

INSERT INTO BarraDeSonido (marca, modelo, precio, volumenActual, entradaActual, modoSonido)
VALUES ('Sonos', 'Beam', 399.00, 65, 'Bluetooth', 'Bass Boost');

INSERT INTO BarraDeSonido (marca, modelo, precio, volumenActual, entradaActual, modoSonido)
VALUES ('Thonet & Vander', 'MagniFi Mini', 299.00, 45, 'AUX', 'Surround');

INSERT INTO BarraDeSonido (marca, modelo, precio, volumenActual, entradaActual, modoSonido)
VALUES ('Yamaha', 'YAS-209', 349.99, 50, 'HDMI', 'Vocal Clarity');

INSERT INTO BarraDeSonido (marca, modelo, precio, volumenActual, entradaActual, modoSonido)
VALUES ('Philips', 'V51-H6', 279.99, 75, 'Optical', 'Dynamic');

INSERT INTO BarraDeSonido (marca, modelo, precio, volumenActual, entradaActual, modoSonido)
VALUES ('Hypersound', 'Cinema 600', 399.99, 60, 'Bluetooth', 'Standard');

SELECT * FROM BarraDeSonido;

SELECT * FROM BarraDeSonido
WHERE marca = 'Sony';

SELECT marca, modelo, precio FROM BarraDeSonido
WHERE precio > 300;

SELECT marca, modelo, modoSonido FROM BarraDeSonido
WHERE modoSonido = 'Surround';

SELECT marca, modelo, precio FROM BarraDeSonido
ORDER BY precio DESC;


