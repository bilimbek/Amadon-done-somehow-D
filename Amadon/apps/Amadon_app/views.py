from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "Amadon_app/index.html", context)

def checkout(request):
    
    if request.method == "POST":
        price_from_form = float(request.POST["price"])
        quantity_from_form = int(request.POST["quantity"])
        total_charge = quantity_from_form * price_from_form
        print("Charging credit card...")
        order = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
        print(order.id)
        request.session['order_id']=order.id
        print(request.session['order_id'])
        return redirect("/checkout")

    if 'order_id' in request.session:

        order = Order.objects.get(id=request.session['order_id'])
        print(order)
        context = {
            "total_charge": order.total_price,
            "quantity": order.quantity_ordered,
        }
        return render(request, "Amadon_app/checkout.html", context)
    else:
        return redirect ( '/')