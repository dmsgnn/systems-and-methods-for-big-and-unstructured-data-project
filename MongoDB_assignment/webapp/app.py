from datetime import datetime
import os
from pymongo.collection import Collection
from flask import Flask, json, render_template, request, abort, session
from flask_pymongo import PyMongo
from bson import json_util



app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
# app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["MONGO_URI"] = "mongodb+srv://andreac99:tmJXfW55Skt75z@cluster0.7px16.mongodb.net/test?authSource=admin" \
                          "&replicaSet=atlas-i8fr10-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true"
app.secret_key = '12345'                        
pymongo = PyMongo(app, tls=True, tlsAllowInvalidCertificates=True)
db = pymongo.cx.SMBUD
certificates: Collection = db.certificates


def parse_json(data):
    return json.loads(json_util.dumps(data))

@app.route('/')
@app.route('/login/')
def login():
    if request.method == 'GET':
        return render_template('login.html')

@app.route('/personal_area/', methods = ['POST', 'GET'])
def personal_area():
    if request.method != 'POST':
        return abort(404)
    else:
        session['tax_code'] = request.form['tax_code']
        person = certificates.find_one_or_404({"tax_code": session["tax_code"]}, {"name": 1, "surname": 1, "_id": 0})
        return render_template('personal_area.html', value=person["name"] + " " + person["surname"])


@app.route('/certificates/<string:uci>', methods=["GET"])
def get_certificate(uci):  # put application's code here
    certificate = certificates.find_one_or_404({"uci": uci})
    return parse_json(certificate)



@app.route("/certificates/")
def list_certificates():

    # For pagination, it's necessary to sort by name,
    # then skip the number of docs that earlier templates would have displayed,
    # and then to limit to the fixed page size, ``per_page``.
    certificates_result = certificates.find().sort("uci")

    certificates_count = certificates.count_documents({})

    return {
        "certificates": [parse_json(certificates_result)]
    }


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
