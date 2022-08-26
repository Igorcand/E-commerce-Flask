# E-commerce 
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/Igorcand/E-commerce-Flask/blob/master/LICENSE) 

# About the Project
E-commerce Flask is a complete application developed using a framework Flask with the back Server side, that is, the front-end is rendered at python code. The idea of Project is a website that can add products to a buying cart, see information about all products, and filter the products by brands, categories, and name. During the development was added a required login always that tried to do some buy, protect passwords with cryptography, and upload and save images, using respectively, Flask-Login, Flask-Bcrypt, Flask-Reupload, and other Flask extensions. At the created application there also exists an admin tab to can add products and information about these products, very similar that the Page created while using Flask-Admin, in this region exist routes to see products, brands and categories and also add thems.
The project was developed following the video on the youtube channel Jamal Bugti.

## Layout 
When the code is ruined, this is a home page showing all products that are registered on database
![Mobile 1](https://github.com/Igorcand/E-commerce-Flask/blob/master/assets/homepage.png) 

## Navbar 
At the browsing tab, we have routes to filtring the products registred, being able to see the brands or categories, or even search at the product name. And also do login and registering.
![Mobile 1](https://github.com/Igorcand/E-commerce-Flask/blob/master/assets/navbar.png) 

### Filtring 
![Mobile 1](https://github.com/Igorcand/E-commerce-Flask/blob/master/assets/filtring.png)
### Login 
![Mobile 1](https://github.com/Igorcand/E-commerce-Flask/blob/master/assets/login_customer.png) 
### Register
![Mobile 1](https://github.com/Igorcand/E-commerce-Flask/blob/master/assets/registring.png) 

## Single Page 
In each product that exists on the website exists a detail button, to see and do a better analyzing the products description, see all available colors   and add at the cart buying of course with quantity and necessary colors.
![Mobile 1](https://github.com/Igorcand/E-commerce-Flask/blob/master/assets/single_page.png) 

## Cart
After adding all products that you need at the cart buying, you can analyze, edit and delete the added items by accessing the icon "cart(...)" on the navbar.
![Mobile 1](https://github.com/Igorcand/E-commerce-Flask/blob/master/assets/carts.png) 

## Orders
After verifying the products that are added ate the cart, you can create a order of the products and confirm your request clicking at button "order now" and will simulate a request to buy and show a screen with the products choosed and the value about each item. If you want use this website model to some real application, you need integrete with some paymeent API, like Stripe, to go to others steps relational at paymeent.
![Mobile 1](https://github.com/Igorcand/E-commerce-Flask/blob/master/assets/orders.png) 




## Admin Login 
To register some product on database, you can login on Admin Page and acess this page clicking at the button "Admin" in navbar.
To login you need necessary that is registered in the database, if you didn't you can click on the button "register".

## Home page Admin
This is an admin homepage, the place where you can see all products registered, delete and update them.
![Mobile 1](https://github.com/Igorcand/E-commerce-Flask/blob/master/assets/admin_homepage.png) 

## Brands Admin
This is an admin homepage, the place where you can see all brands registered, delete and update them.
![Mobile 1](https://github.com/Igorcand/E-commerce-Flask/blob/master/assets/admin_brands.png) 

## Categories Admin
This is an admin homepage, the place where you can see all categories registered, delete and update them.
![Mobile 1](https://github.com/Igorcand/E-commerce-Flask/blob/master/assets/admin_categories.png) 

## Navbar Admin  
To add some product in the database, product, brand, or category, you have access to browse tab inside the admin page.
![Mobile 1](https://github.com/Igorcand/E-commerce-Flask/blob/master/assets/admin_navbar.png) 

### Add Produt 
![Mobile 1](https://github.com/Igorcand/E-commerce-Flask/blob/master/assets/add_prod.png) 
### Add Brand  
![Mobile 1](https://github.com/Igorcand/E-commerce-Flask/blob/master/assets/add_brand.png) 
### Add Category 
![Mobile 1](https://github.com/Igorcand/E-commerce-Flask/blob/master/assets/add_cat.png) 




# Technology used

## Front end
- HTML  
- CSS 
- Bootstrap 4

## Back end
- Python
- Flask

## Data Base
- SQLite


# How run this project

```bash
# clone this repository
git clone https://github.com/Igorcand/E-commerce-Flask

# Enter the folder 
E-commerce-Flask

# Install modules
pip install -r requirements.txt

# Execute the file 
python run.py
```


# Author

Igor Cândido Rodrigues

https://www.linkedin.com/in/igorc%C3%A2ndido/
