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


# def add_data_in_db(excel_path):
#     product_lines = parsing_upd(excel_path)
#     for product_line in product_lines:
#         db.session.add(ProductLine(product_name=product_line.product_name,
#                                    unit_of_measurement=product_line.unit_of_measurement,
#                                    quantity=product_line.quantity, price=product_line.price,
#                                    cost_without_tax=product_line.cost_without_tax,
#                                    tax_rate=product_line.tax_rate, tax_amount=product_line.tax_amount,
#                                    cost_with_tax=product_line.cost_with_tax))
#         db.session.commit()





