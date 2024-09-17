# -- Создание таблицы пользователей
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     age INTEGER,
#     email TEXT
# );
#
# -- Создание таблицы заказов с внешним ключом на таблицу пользователей
# CREATE TABLE IF NOT EXISTS orders (
#     order_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     user_id INTEGER,
#     product TEXT,
#     price REAL,
#     order_date TEXT,
#     FOREIGN KEY (user_id) REFERENCES users(id)
# );
#
# -- Вставка данных в таблицу пользователей
# INSERT INTO users (name, age, email)
# VALUES
#     ('Alice', 30, 'alice@example.com'),
#     ('Bob', 25, 'bob@example.com'),
#     ('Charlie', 35, 'charlie@example.com');
#
# -- Вставка данных в таблицу заказов
# INSERT INTO orders (user_id, product, price, order_date)
# VALUES
#     (1, 'Ноутбук', 999.99, '2024-09-01'),
#     (2, 'Телефон', 499.99, '2024-09-02'),
#     (1, 'Планшет', 299.99, '2024-09-03');
#
# -- Выбор всех данных из таблицы пользователей
# SELECT * FROM users;
#
# -- Выбор всех данных из таблицы заказов
# SELECT * FROM orders;
#
# -- Выбор пользователей старше 30 лет
# SELECT * FROM users WHERE age > 30;
#
# -- Соединение таблиц пользователей и заказов для отображения продуктов, купленных пользователями
# SELECT users.name, orders.product, orders.price
# FROM users
# JOIN orders ON users.id = orders.user_id;
#
# -- Обновление возраста Алисы
# UPDATE users
# SET age = 32
# WHERE name = 'Alice';
#
# -- Удаление записи пользователя Боба
# DELETE FROM users
# WHERE name = 'Bob';
#
# -- Проверка оставшихся пользователей
# SELECT * FROM users;
#
# -- Подсчет общего числа пользователей
# SELECT COUNT(*) AS total_users FROM users;
#
# -- Сумма всех заказов
# SELECT SUM(price) AS total_revenue FROM orders;
#
# -- Группировка заказов по пользователю и подсчет их общего числа
# SELECT user_id, COUNT(*) AS total_orders
# FROM orders
# GROUP BY user_id;
#
# -- Использование подзапроса для нахождения пользователей, сделавших заказы более чем на 500
# SELECT name
# FROM users
# WHERE id IN (SELECT user_id FROM orders WHERE price > 500);
#
# -- Сортировка пользователей по возрасту по убыванию
# SELECT * FROM users ORDER BY age DESC;
#
# -- Ограничение результатов двумя пользователями
# SELECT * FROM users LIMIT 2;
#
# -- Вставка пользователя с NULL значением возраста
# INSERT INTO users (name, age, email)
# VALUES ('Dave', NULL, 'dave@example.com');
#
# -- Выбор пользователей, у которых возраст не задан (NULL)
# SELECT * FROM users WHERE age IS NULL;
#
# -- Начало транзакции для атомарного обновления данных пользователя
# BEGIN TRANSACTION;
#
# -- Вставка нового пользователя
# INSERT INTO users (name, age, email)
# VALUES ('Eve', 29, 'eve@example.com');
#
# -- Обновление возраста Чарли
# UPDATE users
# SET age = 33
# WHERE name = 'Charlie';
#
# -- Завершение транзакции
# COMMIT;
#
# -- Создание индекса по имени в таблице пользователей
# CREATE INDEX IF NOT EXISTS idx_users_name ON users (name);
#
# -- Добавление столбца телефона в таблицу пользователей
# ALTER TABLE users ADD COLUMN phone TEXT;
#
# -- Переименование столбца email
# ALTER TABLE users RENAME COLUMN email TO email_address;
#
# -- Экспорт данных таблицы пользователей в CSV файл
# .headers on
# .mode csv
# .output users.csv
# SELECT * FROM users;
# .output stdout;
#
# -- Удаление таблицы заказов, если она существует
# DROP TABLE IF EXISTS orders;
#
# -- Итоговая проверка данных в таблице пользователей
# SELECT * FROM users;
