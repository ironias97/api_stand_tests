import configuration
import requests
import data

d = data
conf = configuration
req = requests


def get_docs():
    return req.get(conf.URL_SERVICE + conf.DOC_PATH)


def get_logs():
    return req.get(conf.URL_SERVICE + conf.LOG_MAIN_PATH, params={"count": 20})


def get_users_table():
    return req.get(conf.URL_SERVICE + conf.USER_TABLE_PATH)


def post_new_user(body):
    return requests.post(conf.URL_SERVICE + conf.CREATE_USER_PATH,
                         json=body,
                         headers=d.headers)


def post_product_kits(products_id):
    return req.post(conf.URL_SERVICE + conf.PRODUCT_KITS_PATH,
                    json=products_id,
                    headers=d.headers)
