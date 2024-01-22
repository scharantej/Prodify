## Design of Flask Application for a Simple Product-Management Website

### HTML Files

1. **add_product.html**: This HTML file will contain a form that allows the user to add a new product. The form will have fields for the product name, description, price, and an image.
2. **products.html**: This HTML file will display a list of all the products in the database. It will have a table with columns for the product name, description, price, and image.
3. **home.html**: This HTML file will be the home page of the website. It will have links to the add product page (/add-product) and the products page (/products).

### Routes

1. **add_product**: This route will handle the form submission from the add product page. It will validate the form data and add the new product to the database.
2. **products**: This route will retrieve all the products from the database and render the products page.
3. **home**: This route will render the home page of the website.

## Additional Notes

- The HTML files can be customized to match the design of the website.
- The routes can be modified to add additional functionality to the website, such as allowing users to edit or delete products.
- The website can be deployed using a web hosting service, such as Heroku or Google App Engine.