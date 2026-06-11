#!/usr/bin/env python3
"""
Main module for MongoDB collection operations using pymongo
"""
from typing import List, Dict, Any


def list_all(mongo_collection) -> List[Dict[str, Any]]:
    """
    List all documents in a python pymongo collection object.
    """
    if mongo_collection is None:
        return []
        
    return list(mongo_collection.find())
