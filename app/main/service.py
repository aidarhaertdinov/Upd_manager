import pandas as pd
from app.model import ProductLine, db


def parsing_upd(excel_path: str) -> list[ProductLine]:
    excel = pd.read_excel(excel_path, sheet_name='Лист1')
    product_lines = []
    for value in excel.values:
        product_name = value[0]
        unit_of_measurement = value[1]
        quantity = value[2]
        price = value[3]
        cost_without_tax = value[4]
        tax_rate = value[5]
        tax_amount = value[6]
        cost_with_tax = value[7]
        product_lines.append(ProductLine(product_name, unit_of_measurement, quantity, price, cost_without_tax, tax_rate, tax_amount, cost_with_tax))
    return product_lines






