import json
from discountcoupon import ShopifyDiscountManager
from flask import Flask, render_template,request
app = Flask(__name__)
app._static_folder = '/Users/harshloomba/Documents/Bizzy/'

@app.route('/')
def index():
  return app.send_static_file('index.html')

@app.route('/discountmanager', methods=['POST'])
def my_link():
	print "here"
	uid=request.form['id']
	pwd=request.form['pwd']
	uniqueid=request.form['userID']
	print uniqueid
	codevalue=request.form['code']
	print codevalue
	discountv=request.form['discountvalue']
	limit=request.form['usagelimit']
	print limit
	startdate=request.form['startdate']
	enddate=request.form['enddate']
	
	
	# Initialize a manager for your store: shopify_shop_name.myshopify.com
	discount_manager = ShopifyDiscountManager('hersheychoc',uid, 
		pwd,uniqueid,codevalue,limit,startdate,enddate)

	# Create a discount for 10% off all order items
	response=discount_manager.create_discount_code(**{'code': codevalue, 'discount_type': 'percentage', 'value':discountv})
	content = json.loads(response.content)
	
	return app.response_class(response.content, content_type='application/json')
if __name__ == '__main__':
  app.run(debug=True)

