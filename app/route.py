from flask import Flask, render_template, request
import pymongo
import pymongo.errors
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/product_robot_usage_warning')
def site_join_view():
    return render_template('product/product_robot_usage_warning.html')

@app.route('/product_list_view')
def product_list_view():
    return render_template('product/product_list_view.html')

@app.route('/site_join',  methods=['POST', 'GET'])
def site_join():
    cid = request.form.get('cid', "")
    cname = request.form.get('cname', "")

    context = {
        "success" : "True",
        "cid" : cid,
        "cname" : cname
    }
    if cid == "" or cname == "" :
        context['success'] = "False"
        context['fail-reson'] = "cid or cname is not passed"

    return render_template('site_join_result.json', context = context)

@app.route('/user_list_view',  methods=['POST', 'GET'])
def user_list_view() :

    from datasource.TUserHandler import TUserHandler
    handler = TUserHandler()
    cursor = handler.selectAll()

    context = {}
    return render_template('user_list_view.html', cursor = cursor)

if __name__ == '__main__':
    app.run(debug=True)

