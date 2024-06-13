from database import sesija,Employee,Product,Sale


def insert_empoyee(sesija,full_name,email,age,position,salary,years_in_company):
    emp1 = Employee(full_name = full_name,
                    email = email,
                    age = age,
                    position = position,
                    salary = salary,
                    years_in_company = years_in_company)

    sesija.add(emp1)
    sesija.commit()
    print(f"Vraboteniot {full_name} e vnesen")
    return emp1
def insert_product(sesija,name,price):
    prod1 = Product(name=name,price=price)
    sesija.add(prod1)
    sesija.commit()
    print(f"Produktot {name} e dodaden")
    return prod1

def insert_sale(sesija,employee_id, product_id):
    sale1 = Sale(employee_id=employee_id,product_id=product_id)
    sesija.add(sale1)
    sesija.commit()
    print("Prodazbata e zabelezana")
    return sale1
#e = insert_empoyee(sesija,"Jakov Noveski","mail@example.com",28,"Developer",60000,2)
#p = insert_product(sesija,"banani","100")
#s = insert_sale(sesija,2,3)

"""emp = sesija.query(Employee).all()
for employee in emp:
    print(f"{employee.id}.{employee.full_name} = {employee.position}")"""

#empoyees = sesija.query(Employee).filter_by(position = 'Sales').all()
#empoyees = sesija.query(Employee).filter_by(position = 'Sales').first()
#empoyees = sesija.query(Employee).filter_by(position = 'Developer').limit(3).all()
#print(empoyees)

print("Novi promeni vo nov branchj")
ime = input("Vnesete go vasheto ime: ")
print(f"Zdravo {ime}")

