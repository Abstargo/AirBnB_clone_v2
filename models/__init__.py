#!/usr/bin/python3
"""This module instantiates an object"""

from os import getenv

if getenv("HBNB_TYPE_STORGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
