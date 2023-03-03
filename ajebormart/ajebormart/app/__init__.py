from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app.routes import user_routes, product_routes, cart_routes, order_routes, payment_routes