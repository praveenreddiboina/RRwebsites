

from django.shortcuts import render , redirect , HttpResponseRedirect
from .models import Products
from .models import Category
from django.views import View
from django.core.mail import send_mail
from django.conf import settings

#Create your views here.
class Index(View):
    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('homepage')

    def get(self , request):
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    # else:
    #     products = Products.get_all_products()

    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request, 'index.html',data)

def about(request):
    return render(request,"about.html")


def products(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    else:
        products = Products.get_all_products()

    data = {}
    data['products'] = products
    data['categories'] = categories

    return render(request, "products.html", data)

def contact(request):
    if request.method =='POST':
        frommail = request.POST['frommail']
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail(subject,message,frommail,['praveen14.marolix@gmail.com',frommail])

    return render(request, 'contact.html')
# def contact(request):
# 	if request.method == 'POST':
#         eww    
# 		message = request.POST['message']
# 		send_mail('Contact Form',
# 		 message, 
# 		 settings.EMAIL_HOST_USER,
# 		 ['praveen14.marolix@gmail.com'])
# 	return render(request, 'contact.html')