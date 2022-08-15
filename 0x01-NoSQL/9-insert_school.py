#!/usr/bin/env python3
""" 9-insert_school """


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs
    Returns the new _id
    """
    value_id = mongo_collection.insert_one(kwargs)
    return value_id.inserted_id
