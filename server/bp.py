from flask import Blueprint
import os,sys

if getattr(sys, 'frozen', False):
    # The application is frozen
    datadir = os.path.dirname(sys.executable)
else:
    # The application is not frozen
    datadir = os.path.dirname(__file__)
    datadir=os.path.dirname(datadir)

template_folder=os.path.join(datadir,'client/html')
static_folder=os.path.join(datadir,'client')
bp = Blueprint('bp', __name__,
               template_folder=template_folder,
               static_folder=static_folder,
               static_url_path='assets')
