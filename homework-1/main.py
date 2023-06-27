"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2

with psycopg2.connect(
        host="localhost",
        database="north",
        user="postgres",
        password="Layne8841"
) as conn:
    with conn.cursor() as cur:
        with open('north_data/customers_data.csv', newline='') as file:
            customers = csv.DictReader(file)
            for row in customers:
                ins = "INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s)"
                val = (row['customer_id'], row['company_name'], row['contact_name'])
                # cur.execute(ins, val)

        with open('north_data/employees_data.csv', newline='') as file:
            employees = csv.DictReader(file)
            for row in employees:
                ins = "INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes) VALUES (" \
                      "%s, " \
                      "%s, %s, %s, %s, %s)"
                val = (
                row['employee_id'], row['first_name'], row['last_name'], row['title'], row['birth_date'], row['notes'])
                # cur.execute(ins, val)

        with open('north_data/orders_data.csv', newline='') as file:
            orders = csv.DictReader(file)
            for row in orders:
                ins = "INSERT INTO orders (order_id,customer_id,employee_id,order_date,ship_city) VALUES (%s, " \
                      "%s, %s, %s, %s)"
                val = (row['order_id'], row['customer_id'], row['employee_id'], row['order_date'], row['ship_city'])
                # cur.execute(ins, val)
        cur.execute("SELECT * FROM customers")
        rows = cur.fetchall()
        print(rows)
conn.close()
