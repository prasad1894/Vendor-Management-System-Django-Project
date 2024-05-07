from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models.product import Product
from .models.category import Category
from django.contrib.auth.hashers import make_password,check_password
from .models.customer import Customer

# Create your views here.
def home(request):
    categories=Category.objects.all()
    categoryID=request.GET.get('category')
    if categoryID:
        products=Product.get_category_id(categoryID)
    else:
        products=Product.objects.all()
    data={'products':products,'categories':categories}
    return render(request,'index.html',data)

def signup(request):
    if request.method=='GET':
        return render(request,'signup.html')
    else:
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        mobile=request.POST['mobile']
        password=request.POST['password']
        password=make_password(password)
        userdata=[fname,lname,email,mobile,password]
        print(userdata)
        uservalues={
            'fname':fname,
            'lname':lname,
            'email':email,
            'mobile':mobile
        }
        
        customerdata=Customer(first_name=fname,last_name=lname,email=email,mobile=mobile,password=password)
        
        
        error_msg=None
        success_msg=None
        if(not fname):
            error_msg="First Name should not be empty"
        elif(not lname):
            error_msg="Last Name should not be empty"
        elif(not email):
            error_msg="Email should not be empty"
        elif(not mobile):
            error_msg="Mobile Number should not be empty"
        elif(not password):
            error_msg="password should not be empty"
        elif(customerdata.isexist()):
            error_msg="Email already Exists"
        if(not error_msg):
            success_msg="Account Created Successfully"
            customerdata.save()
            msg={'success':success_msg}
            return render(request,'signup.html', msg)
        else:
            msg={'error':error_msg,'value':uservalues}
            return render(request,'signup.html', msg)
        
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        email=request.POST['email']
        password=request.POST['password']
        
        users=Customer.getemail(email)
        error_msg=None
        if users:
            check=check_password(password,users.password)
            if check:
                return redirect('/')
            else:
                error_msg="Password is Incorrect"
                msg={'error':error_msg}
                return render(request,'login.html',msg)
        else:
            error_msg="Email is Incorrect"
            msg={'error':error_msg}
            return render(request,'login.html',msg)