from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from flask_session import Session
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Sample products based on the image list provided
PRODUCTS = [
    {
        'id': 1,
        'name': 'Fresh Bagel',
        'price': 2.50,
        'image': 'bagel-icon.png',
        'hero_image': 'bagel-hero.png',
        'category': 'Bakery',
        'description': 'Freshly baked artisanal bagel, perfect for breakfast'
    },
    {
        'id': 2,
        'name': 'Organic Banana',
        'price': 0.75,
        'image': 'banana-icon.png',
        'hero_image': 'banana-hero.png',
        'category': 'Fruits',
        'description': 'Sweet, ripe organic bananas packed with potassium'
    },
    {
        'id': 3,
        'name': 'Premium Butter',
        'price': 4.99,
        'image': 'butter-icon.png',
        'hero_image': 'butter-hero.png',
        'category': 'Dairy',
        'description': 'Creamy, rich butter made from farm-fresh cream'
    },
    {
        'id': 4,
        'name': 'Caesar Salad Kit',
        'price': 6.99,
        'image': 'caesar-icon.png',
        'hero_image': 'caesar-hero.png',
        'category': 'Ready Meals',
        'description': 'Complete Caesar salad kit with dressing and croutons'
    },
    {
        'id': 5,
        'name': 'Artisan Cheese',
        'price': 8.99,
        'image': 'cheese-icon.png',
        'hero_image': 'cheese-hero.png',
        'category': 'Dairy',
        'description': 'Aged artisan cheese with complex flavors'
    },
    {
        'id': 6,
        'name': 'Ruby Grapefruit',
        'price': 1.25,
        'image': 'grapefruit-icon.png',
        'hero_image': 'grapefruit-hero.png',
        'category': 'Fruits',
        'description': 'Juicy ruby red grapefruit, rich in vitamin C'
    },
    {
        'id': 7,
        'name': 'Greek Yogurt',
        'price': 3.99,
        'image': 'greek-yogurt-icon.png',
        'hero_image': 'greek-yogurt-hero.png',
        'category': 'Dairy',
        'description': 'Thick, creamy Greek yogurt with live cultures'
    },
    {
        'id': 8,
        'name': 'Green Onions',
        'price': 1.50,
        'image': 'green-onion-icon.png',
        'hero_image': 'green-onion-hero.png',
        'category': 'Vegetables',
        'description': 'Fresh green onions, perfect for garnishing'
    },
    {
        'id': 9,
        'name': 'Classic Hummus',
        'price': 4.49,
        'image': 'hummus-icon.png',
        'hero_image': 'hummus-hero.png',
        'category': 'Dips & Spreads',
        'description': 'Smooth, creamy hummus made with chickpeas and tahini'
    },
    {
        'id': 10,
        'name': 'KitKat Chocolate',
        'price': 1.99,
        'image': 'kitkat-icon.png',
        'hero_image': 'kitkat-hero.png',
        'category': 'Snacks',
        'description': 'Crispy wafer bars covered in milk chocolate'
    },
    {
        'id': 11,
        'name': 'Fresh Lemon',
        'price': 0.50,
        'image': 'lemon-icon.png',
        'hero_image': 'lemon-hero.png',
        'category': 'Fruits',
        'description': 'Bright, zesty lemons perfect for cooking and drinks'
    },
    {
        'id': 12,
        'name': 'Sweet Mandarin',
        'price': 0.85,
        'image': 'mandarin-icon.png',
        'hero_image': 'mandarin-hero.png',
        'category': 'Fruits',
        'description': 'Sweet, easy-to-peel mandarin oranges'
    },
    {
        'id': 13,
        'name': 'Yellow Onion',
        'price': 1.25,
        'image': 'onion-icon.png',
        'hero_image': 'onion-hero.png',
        'category': 'Vegetables',
        'description': 'Fresh yellow onions, a kitchen essential'
    },
    {
        'id': 14,
        'name': 'Dinner Plates Set',
        'price': 24.99,
        'image': 'plates-icon.png',
        'hero_image': 'plates-hero.png',
        'category': 'Kitchenware',
        'description': 'Elegant ceramic dinner plates, set of 4'
    },
    {
        'id': 15,
        'name': 'Red Bell Pepper',
        'price': 2.25,
        'image': 'red-pepper-icon.png',
        'hero_image': 'red-pepper-hero.png',
        'category': 'Vegetables',
        'description': 'Crisp, sweet red bell peppers'
    },
    {
        'id': 16,
        'name': 'Sour Cream',
        'price': 3.49,
        'image': 'sour-cream-icon.png',
        'hero_image': 'sour-cream-hero.png',
        'category': 'Dairy',
        'description': 'Rich, tangy sour cream for cooking and dipping'
    },
    {
        'id': 17,
        'name': 'Fresh Strawberries',
        'price': 4.99,
        'image': 'strawberry-icon.png',
        'hero_image': 'strawberry-hero.png',
        'category': 'Fruits',
        'description': 'Sweet, juicy strawberries perfect for desserts'
    }
]

def get_cart_items():
    """Get cart items from session"""
    if 'cart' not in session:
        session['cart'] = {}
    return session['cart']

def get_cart_total():
    """Calculate total price of items in cart"""
    cart = get_cart_items()
    total = 0
    for product_id, quantity in cart.items():
        product = next((p for p in PRODUCTS if p['id'] == int(product_id)), None)
        if product:
            total += product['price'] * quantity
    return round(total, 2)

def get_cart_count():
    """Get total number of items in cart"""
    cart = get_cart_items()
    return sum(cart.values())

@app.route('/')
def index():
    """Home page with product listing"""
    categories = list(set(product['category'] for product in PRODUCTS))
    selected_category = request.args.get('category')
    
    if selected_category:
        filtered_products = [p for p in PRODUCTS if p['category'] == selected_category]
    else:
        filtered_products = PRODUCTS
    
    return render_template('index.html', 
                         products=filtered_products,
                         categories=categories,
                         selected_category=selected_category,
                         cart_count=get_cart_count())

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    """Product detail page"""
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if not product:
        return redirect(url_for('index'))
    
    return render_template('product_detail.html', 
                         product=product,
                         products=PRODUCTS,
                         cart_count=get_cart_count())

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    """Add product to cart"""
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if not product:
        return redirect(url_for('index'))
    
    cart = get_cart_items()
    product_id_str = str(product_id)
    
    if product_id_str in cart:
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1
    
    session['cart'] = cart
    return redirect(request.referrer or url_for('index'))

@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    """Remove product from cart"""
    cart = get_cart_items()
    product_id_str = str(product_id)
    
    if product_id_str in cart:
        if cart[product_id_str] > 1:
            cart[product_id_str] -= 1
        else:
            del cart[product_id_str]
    
    session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    """Shopping cart page"""
    cart = get_cart_items()
    cart_items = []
    
    for product_id, quantity in cart.items():
        product = next((p for p in PRODUCTS if p['id'] == int(product_id)), None)
        if product:
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'subtotal': round(product['price'] * quantity, 2)
            })
    
    total = get_cart_total()
    
    return render_template('cart.html',
                         cart_items=cart_items,
                         total=total,
                         cart_count=get_cart_count(),
                         products=PRODUCTS)

@app.route('/clear_cart')
def clear_cart():
    """Clear all items from cart"""
    session['cart'] = {}
    return redirect(url_for('cart'))

@app.route('/api/cart/count')
def api_cart_count():
    """API endpoint to get cart count"""
    return jsonify({'count': get_cart_count()})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 