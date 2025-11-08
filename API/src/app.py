import flask
import sys 
import os 

from waitress import serve

# Add the parent directory to sys.path to enable imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from Webscrapper.src import main as webscrapper_interface

app = flask.Flask(__name__)

html_page = "<html><body><h2>Currency Man</h2><form action=\"/currency\" method=\"POST\"><input type=\"text\" name=\"currency_from\" placeholder=\"Enter Currency From\" required><input type=\"text\" name=\"currency_to\" placeholder=\"Enter Currency To\" required><button type=\"submit\">Submit</button></form></body></html>"

# Route to serve the HTML form
@app.route('/', methods=['GET'])
def home():
    return html_page

# Route to handle form submission and return JSON
@app.route('/currency', methods=['POST'])
def convert_currency():
    
    currency_from = flask.request.form.get('currency_from', '').strip().upper()
    currency_to = flask.request.form.get('currency_to', '').strip().upper()
    
    # Validate currency codes
    if not currency_from or not currency_to:
        return flask.jsonify({"error": "Both currency_from and currency_to are required"}), 400
    
    if len(currency_from) != 3 or len(currency_to) != 3:
        return flask.jsonify({"error": "Currency codes must be 3 characters..."}), 400
    
    try:
        data = webscrapper_interface.current_usd_to_egp_exchange_rate(currency_from, currency_to)
        return flask.jsonify({"exchange-rate": data})
    
    except Exception as e:
        return flask.jsonify({"error": f"Invalid currency codes or conversion failed: {str(e)}"}), 400

if __name__ == "__main__":
    serve(app, host='localhost', port=5000)
    
    # Dev Server
    # app.run(debug=True, host='localhost', port=5000)