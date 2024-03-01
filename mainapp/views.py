from django.shortcuts import render, redirect
from django.db import connection

# Create your views here.

def main(request):
    return render(request,"index.html")

def wishlist(request):
    return render(request, 'wishlist.html')

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about-us.html")

def checkout(request):
    return render(request,"checkout.html")

def product(request):
    return render(request,"kannauj perfume.html")

def faq(request):
    return render(request,"faq.html")

def cart(request):
    return render(request,"shopping-cart.html")

def register(request):
    return render(request,"login-register.html")


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('passwd')

        # Use the cursor to execute raw SQL queries
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE email_id = %s AND password = %s"
            cursor.execute(sql, [email, password])
            user = cursor.fetchone()

        if user:
            # Login successful
            return redirect('index')
        else:
            # Incorrect email or password
            return render(request, 'login-register.html', {'error_message': 'Incorrect email or password'})

    return render(request, 'login-register.html')




def register_view(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        passwd = request.POST.get('pass1')
        cpasswd = request.POST.get('cpass')

        # Check if the email already exists
        with connection.cursor() as cursor:
            check_sql = "SELECT * FROM users WHERE email_id = %s"
            cursor.execute(check_sql, [email])
            user_exists = cursor.fetchone()

        if user_exists:
            return render(request, 'register.html', {'error_message': 'Email already exists'})

        # Create a new user
        with connection.cursor() as cursor:
            create_sql = "INSERT INTO users (firstname, lastname, email_id, password) VALUES (%s, %s, %s, %s)"
            cursor.execute(create_sql, [fname, lname, email, cpasswd])

        # Redirect to the login page
        return redirect('login')

    return render(request, 'register.html')







