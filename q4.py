employees={'Antony':55000,'Susan':45000,'Kiran':60000}
result={name: 'high' if salary>50000 else 'low' for name,salary in employees.items()}
print(result)