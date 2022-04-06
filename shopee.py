from ast import keyword
from itertools import product
import requests
import pandas as pd


def product_search(keyword):
    url = ('https://shopee.co.id/api/v4/search/search_items?by=relevancy&keyword=pakaian%20anak%20laki%20laki&limit=60&newest=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2').format(keyword)
    resp = requests.get(url).json()
    return resp


def product_detail(itemid, shopid):
    url = ("https://shopee.co.id/api/v4/product/get_shop_info?shopid=340258562").format(itemid, shopid)
    resp = requests.get(url).json()
    return resp


if __name__ == "__main__":
    products = product_search(
        "setelan baju anak laki-laki dan perempuan")
    item_id = products['items'][0]['itemid']
    shop_id = products['items'][0]['shopid']
    item = product_detail(item_id, shop_id)

df = pd.DataFrame(item)
df.to_csv('shopee.csv')
