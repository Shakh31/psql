import psycopg2
from tabulate import tabulate


def connect_to_database():
    return psycopg2.connect(
        database='Pharm_db',
        user='postgres',
        password='1234',
        host='localhost',
        port=5432
    )


def calculate_income_expenditure():
    income = 0
    expenditure = 0

    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        cursor.execute("select amount, transaction_type from transactions")
        transactions = cursor.fetchall()

        for amount, transaction_type in transactions:
            if transaction_type == 'income':
                income += amount
            elif transaction_type == 'expenditure':
                expenditure += amount
    finally:
        cursor.close()
        conn.close()

    return income, expenditure


def calculate_quantity():
    total_bought = 0
    total_sold = 0

    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        cursor.execute("select quantity, transaction_type from transactions")
        transactions = cursor.fetchall()

        for quantity, transaction_type in transactions:
            if transaction_type == 'income':
                total_bought += quantity
            elif transaction_type == 'expenditure':
                total_sold += quantity
    finally:
        cursor.close()
        conn.close()

    return total_bought, total_sold


def main():
    income, expenditure = calculate_income_expenditure()
    bought, sold = calculate_quantity()

    data = [
        ["Total Income", income],
        ["Total Expenditure", expenditure],
        ["Total Quantity Bought", bought],
        ["Total Quantity Sold", sold]
    ]

    print(tabulate(data, tablefmt="grid"))


main()


