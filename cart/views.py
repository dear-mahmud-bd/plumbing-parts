from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

# Create your views here.

def cart(req, total=0, quantity=0, cart_items=None):
    try:
        tax = 0
        grand_total = 0
        if req.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=req.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id = _cart_id(req))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2 * total)/100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass 

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax'       : tax,
        'grand_total': grand_total,
    }
    return render(req, 'cart.html', context)


# create session against user
def _cart_id(req):
    cart = req.session.session_key
    if not cart:
        cart = req.session.create()
    return cart


def add_cart_product(req, product_id):
    current_user = req.user
    product = Product.objects.get(id=product_id)
    if current_user.is_authenticated:
        is_cart_item_exists = CartItem.objects.filter(product=product, user=current_user).exists()
        if is_cart_item_exists:
            cart_items = CartItem.objects.filter(product=product, user=current_user)
            print(cart_items)
            item = CartItem.objects.get(product=product, user=current_user)
            item.quantity += 1
            item.save()
        else:
            try:
                cart = Cart.objects.get(cart_id=_cart_id(req)) # get the cart using the cart_id present in the session
            except Cart.DoesNotExist:
                cart = Cart.objects.create(
                    cart_id = _cart_id(req)
                )
            cart.save()
            cart_item = CartItem.objects.create(
                product = product,
                quantity = 1,
                cart = cart,
                user = current_user
            )
            cart_item.save()
        return redirect('cart_page')
    # if user not authenticated...
    else:
        try:
            cart = Cart.objects.get(cart_id = _cart_id(req)) # get the cart using the cart_id present in the session
        except Cart.DoesNotExist:
            cart = Cart.objects.create(
                cart_id = _cart_id(req)
            )
            cart.save()
        
        try:
            cart_item = CartItem.objects.get(product=product, cart=cart)
            cart_item.quantity += 1
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(
                    product = product,
                    quantity = 1,
                    cart = cart,
                )
            cart.save()
            
    return redirect('cart_page')


def remove_cart_product(req, product_id, cart_item_id):
    product = get_object_or_404(Product, id=product_id)
    try:
        if req.user.is_authenticated:
            cart_item = CartItem.objects.get(product=product, user=req.user, id=cart_item_id)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(req))
            cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
            
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except:
        pass
    return redirect('cart_page')


def remove_cart_item(req, product_id, cart_item_id): # delete a whole card 
    product = get_object_or_404(Product, id=product_id)
    if req.user.is_authenticated:
        cart_item = CartItem.objects.get(product=product, user=req.user, id=cart_item_id)
    else:
        cart = Cart.objects.get(cart_id=_cart_id(req))
        cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
    cart_item.delete()
    return redirect('cart_page')


@login_required(login_url='login_page')
def checkout(request, total=0, quantity=0, cart_items=None):
    try:
        tax = 0
        grand_total = 0
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2 * total) / 100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass 
    
    context = {
        'total'      : total,
        'quantity'   : quantity,
        'cart_items' : cart_items,
        'tax'        : tax,
        'grand_total': grand_total,
    }
    return render(request, 'checkout.html', context)

