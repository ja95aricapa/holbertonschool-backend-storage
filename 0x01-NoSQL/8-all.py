#!/usr/bin/env python3
""" 8-all.py """


def list_all(mongo_collection):
    """
    Lists all documents in a collection or return
    an empty list if no document in the collection
    """
    if mongo_collection.count_documents({}) == 0:
        return []
    else:
        return [doc for doc in mongo_collection.find()]
