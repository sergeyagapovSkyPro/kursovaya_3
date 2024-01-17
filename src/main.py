from src.utils import *

values = get_operations_date(load_json_file())
operations = sort_operations_date(values)
date = change_data(operations)
card_number = mask_card_number(operations)
amount_number = mask_amount_number(operations)

for operation in range(len(operations)):
    print(f"{date[operation]} {operations[operation]['description']}\n"
          f"{card_number[operation]} => Счет {amount_number[operation]}\n"
          f"{operations[operation] ['operationAmount'] ['amount']} {operations[operation] ['operationAmount']['currency']['name']}\n")