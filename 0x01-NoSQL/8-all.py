#!/usr/bin/env python3
"""
 8. List all documents in Python
"""


def list_all(mongo_collection):
    """lists all documents in a collection"""
    documents = mongo_collection.find()
    return [doc for doc in documents]
