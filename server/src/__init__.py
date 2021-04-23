from flask import Flask

app = Flask(__name__)

import sys
# insert at 1, 0 is the script path 
sys.path.insert(1, '../search_magician/server')
import src.views
