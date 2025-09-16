# Contoso Foods - Modern Food Store Website

A modern, responsive web application built with Python Flask for Contoso Foods, featuring a product catalog and shopping cart functionality.

## Features

- **Product Catalog**: Browse a wide variety of food products organized by categories
- **Category Filtering**: Filter products by category (Fruits, Dairy, Vegetables, Bakery, etc.)
- **Product Details**: Detailed product pages with descriptions and features
- **Shopping Cart**: Add items to cart, adjust quantities, and view totals
- **Responsive Design**: Modern, mobile-friendly interface using Bootstrap 5
- **Session Management**: Cart persistence using Flask sessions

## Tech Stack

- **Backend**: Python 3.12+ with Flask
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Icons**: Font Awesome 6
- **Fonts**: Google Fonts (Poppins)
- **Package Manager**: uv

## Quick Start

### Prerequisites

- Python 3.12 or higher
- uv package manager

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd contoso-foods
```

2. Create and activate virtual environment using uv:
```bash
uv venv
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate     # On Windows
```
### Running the Application

1. Start the Flask development server:
```bash
uv run app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

The application will be running in development mode with debug enabled.

## Project Structure

```
contoso-foods/
├── app.py                 # Main Flask application
├── templates/             # Jinja2 templates
│   ├── base.html         # Base template with common layout
│   ├── index.html        # Home page with product listing
│   ├── product_detail.html # Individual product detail page
│   └── cart.html         # Shopping cart page
├── static/               # Static assets
│   ├── css/              # Custom CSS files
│   ├── js/               # Custom JavaScript files
│   └── images/           # Product images
├── pyproject.toml        # uv project configuration
├── uv.lock              # Locked dependencies
└── README.md            # Project documentation
```

## Available Routes

- `/` - Home page with product listing and category filtering
- `/product/<id>` - Individual product detail page
- `/cart` - Shopping cart with item management
- `/add_to_cart/<id>` - Add product to cart
- `/remove_from_cart/<id>` - Remove/reduce product quantity in cart
- `/clear_cart` - Clear all items from cart
- `/api/cart/count` - API endpoint for cart item count

## Product Categories

The application includes the following product categories:
- **Fruits**: Fresh organic fruits (bananas, strawberries, lemons, etc.)
- **Dairy**: Milk products (butter, cheese, yogurt, sour cream)
- **Vegetables**: Fresh vegetables (onions, peppers, green onions)
- **Bakery**: Fresh baked goods (bagels)
- **Ready Meals**: Prepared food items (Caesar salad kits)
- **Dips & Spreads**: Hummus and other spreads
- **Snacks**: Chocolate and other snack items
- **Kitchenware**: Dining accessories (plates, utensils)

## Features Included

### Shopping Cart
- Session-based cart persistence
- Add/remove items with quantity management
- Real-time total calculation including tax
- Simulated checkout process

### User Interface
- Modern, clean design with custom CSS variables
- Responsive grid layout for products
- Hover effects and smooth animations
- Category-based filtering
- Breadcrumb navigation
- Loading states for user actions

### Product Management
- Detailed product information
- Category-based organization
- Related products suggestions
- Image fallback handling

## Development

### Adding New Products

Products are defined in the `PRODUCTS` list in `app.py`. Each product should have:
- `id`: Unique integer identifier
- `name`: Product name
- `price`: Price as a float
- `image`: Icon image filename
- `hero_image`: Large image filename for detail page
- `category`: Product category
- `description`: Product description text

### Customizing Styles

The application uses CSS custom properties (variables) defined in `templates/base.html`:
- `--primary-color`: Main brand color
- `--secondary-color`: Accent color
- `--accent-color`: Success/action color
- `--text-dark`: Primary text color
- `--text-light`: Secondary text color

## Production Deployment

For production deployment:

1. Set a secure secret key in `app.py`
2. Set `debug=False` in the Flask app configuration
3. Use a production WSGI server like Gunicorn
4. Configure proper session storage (Redis, database)
5. Set up proper error handling and logging
6. Use environment variables for configuration

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Support

For questions or issues, please contact the development team or create an issue in the repository.
