from django.shortcuts import render, redirect
from .models import Person

def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        # Check if person exists in the database
        # filter is comparable to "SELECT * FROM tablename WHERE name='searchname';"
        person = Person.objects.filter(name=name).first()

        if not person:
            # Person not found, render login form with an error message
            error_message = 'User not found'
            return render(request, 'login.html', {'error_message': error_message})

        elif person.password != password:
            # Password doesn't match, render login form with an error message
            error_message = 'Incorrect password'
            return render(request, 'login.html', {'error_message': error_message})

        # Successful login, redirect to a success page or perform other actions
        # return render(request,'success.html',{'name1':person.name})
        return success(request,name1=person.name)
        # return redirect('success', name1=person.name)
        # return redirect(reverse('success') + f'?name1={person.name}')


        
    return render(request, 'login.html')

def success(request,name1):
    # Logic for rendering the success page
    return render(request,'success.html',{'name1':name1})
