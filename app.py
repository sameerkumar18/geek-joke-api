# -*- coding: utf-8 -*-
from flask import Flask
import sys

application = Flask(__name__)

reload(sys)
sys.setdefaultencoding('utf-8')


if __name__ == '__main__':
    application.run(debug=True)
