from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
  return "<P>hello Word, Ch59!</p>"

@app.route("/cohort59")
def hi():
  return "<h1>Hello Cohort#59</h1>"



@app.get("/home")
def home():
  print("Home endpoint accesssed")
  return "Welcome to the home page!"

@app.get("/api/students")
def students(): 
  print("Students endpoint accessed")
  student_names = ["Kelly", "beyonce", "michelle", "destinys child"]
  return student_names

#Path Parameter
@app.get("/greet/<string:name>")
def greet(name):
  return f"Hello {name}"

@app.get("/contact")
def contact_api():
  print("Contact API endpoint accessed")
  user = {"name": "peter", "age": 35} #dictionary
  return user


@app.get("/about")
def about():
  return "<h1>About Us</h1>"

#Mock product catalog
@app.get("/api/product")
def get_products():
  print("products")
  products = [
    {"id": 1,  "name": "Laptop", "price": 1200},
    {"id": 2,  "name": "Phone", "price": 800},
    {"id": 3,  "name": "Headphones", "price": 150}

    ]
  return products

#Count endpoint
@app.get("/api/product/count")
def get_product_count():
  count = len(products)
  print("product, count:", count)
  return jsonify({"count": count})
  


app.run(debug=True)