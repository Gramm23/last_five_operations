from utils import operations

for operation in operations:
    if 'from' in operation:
        print(f"""{operation['date']} {operation['description']}
{operation['from']} -> {operation['to']}
{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}""")
        print()
    else:
        print(f"""{operation['date']} {operation['description']}
 -> {operation['to']}
{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}""")
        print()
