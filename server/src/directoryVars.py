import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

def addPath(path):
    return os.path.join(THIS_FOLDER, path)