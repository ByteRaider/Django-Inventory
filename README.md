<h1>Django Inventory System</h1>
<h3>The Django Inventory System is a dynamic and responsive web application designed to manage and track inventory items. Built with Django 5.0.2, HTML5, and HTMX, this application provides an intuitive user interface for inventory management, including features such as product listing, category organization, stock level indication, and user authentication.</h3>

<h2>Features</h2>
<h3>Product Management:</h3> 
<h4>
  <ul>
    <li><p>Create, update, and delete products with detailed information like name, category, price, and stock levels.</p></li>
    <li><p>Category Organization: Classify products into categories for easier management and retrieval.</p></li>
    <li>
<p>Dynamic Searching and Sorting: Utilize HTMX to search and sort products without page reloads, enhancing user experience.</p></li>
    <li>
<p>User Authentication: Secure signup and login functionality, allowing for personalized inventory management.</p></li>
    <li>
<p>Export Functionality: Export the product list to a CSV file for external use or backup.</p></li>
  </ul>
</h4>
<h3>Getting Started</h3>
Prerequisites
Python 3.8 or higher
Django 5.0.2
HTMX
<h2>Installation</h2>
Clone the repository
<p>git clone https://github.com/ByteRaider/Django-Inventory.git
cd Django-Inventory</p>

<h2>Create and activate a virtual environment</h2>
<p>python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`</p>

<h2>Install required packages</h2>
<p>pip install -r requirements.txt</p>

<h2>Setup:
Apply migrations to create the database schema</h2>
<p>python manage.py migrate</p>

<h2>Run the development server</h2>
<p>python manage.py runserver</p>
<p>Visit http://127.0.0.1:8000/ in your web browser to start using the Django Inventory System.</p>

<h2>Usage</h2>
<ul>
  <li>Navigating the Inventory: The homepage displays a list of products with their details. Use the search bar and sorting options to find and organize products.
</li>
  <li>Adding a Product: Click on "Add Product" and fill out the form with the product's details.</li>
  <li>Editing and Deleting: Each product has options to edit or delete directly from the list view.</li>
  <li>Exporting Products: Use the "Export Products" option to download a CSV file containing the product list.</li>
</ul>

<h2>Contributing
</h2>
<h4>Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs, feature requests, or improvements.</h4>

<h2>License</h2>
<h4>Apache 2.0</h4>
