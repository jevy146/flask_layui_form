# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : app.py
# Time       ：2021/11/11 15:26
# Author     ：jiewei_yang
# version    ：python 3.7.9
# Description：
"""

from flask import Flask, render_template, jsonify, request
from icecream import ic

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    # return render_template('layui_jquery_button.html') ## 增加了表格数据的异步加载
    return render_template('layui_jquery_form.html')  # form表单的异步加载数据 


# /table/data?page=1&limit=10
@app.route('/table/data', methods=['GET'])
def login():
    page = request.args.get("page")
    limit = request.args.get("limit")
    ic(page, limit)
    data = {"code": 0, "msg": "", "count": 30, "data":
        [{"id": 10000, "username": "user-0", "sex": "女", "city": "城市-0", "sign": "签名-0", "experience": 255,
          "logins": 24, "wealth": 82830700, "classify": "作家", "score": 57},
         {"id": 10001, "username": "user-1", "sex": "男", "city": "城市-1", "sign": "签名-1", "experience": 884,
          "logins": 58, "wealth": 64928690, "classify": "词人", "score": 27},
         {"id": 10002, "username": "user-2", "sex": "女", "city": "城市-2", "sign": "签名-2", "experience": 650,
          "logins": 77, "wealth": 6298078, "classify": "酱油", "score": 31},
         {"id": 10003, "username": "user-3", "sex": "女", "city": "城市-3", "sign": "签名-3", "experience": 362,
          "logins": 157, "wealth": 37117017, "classify": "诗人", "score": 68},
         {"id": 10004, "username": "user-4", "sex": "男", "city": "城市-4", "sign": "签名-4", "experience": 807,
          "logins": 51, "wealth": 76263262, "classify": "作家", "score": 6},
         {"id": 10005, "username": "user-5", "sex": "女", "city": "城市-5", "sign": "签名-5", "experience": 173,
          "logins": 68, "wealth": 60344147, "classify": "作家", "score": 87},
         {"id": 10006, "username": "user-6", "sex": "女", "city": "城市-6", "sign": "签名-6", "experience": 982,
          "logins": 37, "wealth": 57768166, "classify": "作家", "score": 34},
         {"id": 10007, "username": "user-7", "sex": "男", "city": "城市-7", "sign": "签名-7", "experience": 727,
          "logins": 150, "wealth": 82030578, "classify": "作家", "score": 28},
         {"id": 10008, "username": "user-8", "sex": "男", "city": "城市-8", "sign": "签名-8", "experience": 951,
          "logins": 133, "wealth": 16503371, "classify": "词人", "score": 14}, ]}

    return jsonify(data)

import json
@app.route('/table/form', methods=[  'POST'])
def form():
    # 通过 ajax 进行数据的传递
    data = json.loads(request.form.get('data_front'))
    print(data)
    return jsonify({'front_return':'后端返回的数据'})


if __name__ == '__main__':
    app.run(debug=True)
