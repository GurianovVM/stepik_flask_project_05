from flask import jsonify

from app import app, db, jwt
from model import User, Card, Purchas, Store
from schem import StoreSchema


@app.route('/')
def main_view():
    return '<h1>WORK</h1>'


@app.route('/stores/', methods=['GET'])
#@jwt_required
def get_stores():
    stores = db.session.query(Store).all()
    if stores:
        store_schema = StoreSchema(many=True)
        return jsonify(store_schema.dump(stores))
    else:
        return jsonify(), 404
