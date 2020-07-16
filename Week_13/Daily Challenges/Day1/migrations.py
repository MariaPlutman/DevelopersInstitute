from models import db, Contact
from faker import Factory

fake = Factory.create()

# Reload tables
db.drop_all()
db.create_all()
# Make 100 fake contacts
for num in range(100):
    fullname = fake.name().split()
    name = fullname[0]
    surname = ' '.join(fullname[1:])
    email = fake.email()
    phone = fake.phone_number()
    adress = fake.adress()
    # Save in database
    mi_contacto = Contact(name=name, surname=surname,
                          email=email, phone=phone, adress=adress)
    db.session.add(mi_contacto)

db.session.commit()
