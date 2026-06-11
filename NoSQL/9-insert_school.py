#!/usr/bin/env python3
"""
Main module for inserting documents into MongoDB collections using pymongo
"""
from typing import Any


def insert_school(mongo_collection, **kwargs) -> Any:
    """
    Insert a new document into a collection based on provided kwargs
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
