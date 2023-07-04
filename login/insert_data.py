from myapp.models import Person

# Create a new person
new_person = Person(name='John', password='pass')

# Save the new person to the database
new_person.save()
