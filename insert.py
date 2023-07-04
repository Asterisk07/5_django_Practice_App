
# import os

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

# # Create a new person
# new_person = Person(name='John', password='pass')

# # Save the new person to the database
# new_person.save()

import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

# Configure Django settings
django.setup()
try:
    from login.models import Person
except:
    raise ZeroDivisionError
# Add the necessary imports for your model
# from myproject.models import Person

# Your insert code here
# Create and save a new Person instance
person = Person(name='adm', password='pass')
person.save()
# Query the Person model and print the data
persons = Person.objects.all()
for person in persons:
    print(person.name, person.password)