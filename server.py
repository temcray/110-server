from flask import Flask, request


app = Flask(__name__)

#http://127.0.0.1:500/
@app.route("/", methods=["GET"])
def hello_world():
  return "<P>hello Word, Ch59!</p>"

#http://127.0.0.1:500/cohort59
@app.route("/cohort59")
def hi():
  return "<h1>Hello Cohort#59</h1>"


#http://127.0.0.1:500/home
@app.get("/home")
def home():
  print("Home endpoint accesssed")
  return "Welcome to the home page!"

#http://127.0.0.1:500/api/students
@app.get("/api/students")
def students(): 
  print("Students endpoint accessed")
  student_names = ["Kelly", "beyonce", "michelle", "destinys child"]
  return student_names

#Path Parameter
#http://127.0.0.1:500/greet/<string:name>
@app.get("/greet/<string:name>")
def greet(name):
  return f"Hello {name}"

#http://127.0.0.1:500/contact
@app.get("/contact")
def contact_api():
  print("Contact API endpoint accessed")
  user = {"name": "peter", "age": 35} #dictionary
  return user

#http://127.0.0.1:500/about
@app.get("/about")
def about():
  return "<h1>About Us</h1>"

#Mock product catalog
#http://127.0.0.1:500/api/product
@app.get("/api/product")
def get_products():
  print("products")
  products = [
    {"id": 1,  "name": "Laptop", "price": 1200, "category": "Electronic"},
    {"id": 2,  "name": "Phone", "price": 800, "category": "Electronic"},
    {"id": 3,  "name": "Headphones", "price": 150, "category": "Electronic"}

    ]
  return products

#Count endpoint
#http://127.0.0.1:500/api
@app.get("/api/product/count")
def product():
  print("product, count")
  product = [
    {"id": 1,  "name": "Laptop", "price": 1200, "category": "Electronic"},
    {"id": 2,  "name": "Phone", "price": 800, "category": "Electronic"},
    {"id": 3,  "name": "Headphones", "price": 150, "category": "Electronic"}
  ]
  return {"count": len(product)}
  

#http://127.0.0.1:500/apt/search/title
@app.get("/api/search/title")
def search_title():
  return f"title {search_title}"

#http://127.0.0.1:500//api/save
@app.post("/api/save")
def save():
  return "save"

#http://127.0.0.1:500/api/retrieve
@app.get("/api/retrieve")
def retrieve():
  return "retrieve"

#http://127.0.0.1:500/api/search/coupon/codes
@app.get("/api/search/coupon/codes")
def search_coupon_codes():
  return f"search {search_coupon_codes}"

students = [
  {"id": 1, "name": "Isaac", "age": 37, "email": "isaac84@gmail.com"},
  {"id": 2, "name": "Cory", "age": 34, "email": "cory89@gmail.com"},
]
#http://127.0.0.1:500/students
@app.get("/students")
def get_students():
  return students

@app.post("/students")
def add_student():
  data = request.json
  students.append(data)
  return "Student added"

coupons = [
  {"name": "save10", "discount": 0.10},
  {"name": "save50", "discount": 0.50}
]

@app.get("/Coupon")
def get_coupons():
  return "coupons"

@app.post("/Save")
def Save_Coupon():
  coupon = request.json
  coupons.append(coupon)
  return "OK" #201

@app.get("/coupons/<coupon_name>")
def get_coupon_by_name(coupon_name):
  for coupon in coupons:
    if coupon["name"] == coupon_name:
      return coupon
    
  return "coupon not found", 404 #not found
  

products_list = [
    {"id": 1, "title": "Laptop", "category": "Electronics", "price": 899.99},
    {"id": 2, "title": "Headphones", "category": "Electronics", "price": 199.99},
    {"id": 3, "title": "Coffee Mug", "category": "Kitchen", "price": 12.50},
    {"id": 4, "title": "Notebook", "category": "Stationery", "price": 5.99},
]
@app.get("/products")
def get_all_products():
  return products_list

@app.post("/products")
def save_porduct():
  data = request.json
  products_list.append(data)
  return "New product add",201

#list comprehension
app.run(debug=True)
#app.run(debug=true, )