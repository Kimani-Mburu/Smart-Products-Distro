from django.contrib.auth.models import User
from django.db.models.fields import DecimalField
from django.shortcuts import get_object_or_404, redirect, render
from UserInformation.models import Customer

from orders.models import Order, Order_item
from supply.order import Cart
from .forms import DeliverAddress

# Create your views here.
app_name = 'orders'

def checkout(request):
    cart = Cart(request)
    
    user  = get_object_or_404(User, id=request.user.id)
    customer = get_object_or_404(Customer, user=user)
    
    
    if len(cart):
        order = Order.objects.create(user=user, vendor_id=customer, delivery_address = 'Mayview, Khali')
        order.save()
        
        for item in cart:
            order_item = Order_item.objects.create(
                order_id = order,
                product_id = item['product'],
                quantity = item['quantity'],
                total_cost = (int(item['unit_price']) * item['quantity'])
            )
            order_item.save()
        # cart.clear()
        
        ref_no = order.reference_no
        
        order_items = Order_item.objects.filter(order_id__reference_no = ref_no)
        
        context = {
            "reference_no": ref_no,
            'order_items': order_items,
            'delivery_address': order.delivery_address,
            'order_date': order.date,
        }
        print(context['order_items'][0].product_id.name)
        return render(request,'supply/checkout.html', context )
    else:
        return redirect('supply:cart_detail')
    
