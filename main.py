
# Import necessary modules
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

# Initialize the app
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120))
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(200))

    def __repr__(self):
        return '<Product %r>' % self.name

# Create the database tables
db.create_all()

# Define the home page route
@app.route('/')
def home():
    """Render the home page."""
    return render_template('home.html')

# Define the add product route
@app.route('/add-product', methods=['GET', 'POST'])
def add_product():
    """Handle the form submission and add a new product to the database."""
    if request.method == 'POST':
        new_product = Product(name=request.form['name'], description=request.form['description'], price=request.form['price'], image=request.form['image'])
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('products'))
    return render_template('add_product.html')

# Define the products list route
@app.route('/products')
def products():
    """Retrieve all products from the database and render the products page."""
    products = Product.query.all()
    return render_template('products.html', products=products)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
