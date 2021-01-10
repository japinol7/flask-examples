from flask import Flask

app = Flask(__name__)

from . import views
from . import pokemon
from . import anime_list
from . import nasa_asteroid
from . import dog_breeds
