#!/usr/bin/env python3
"""
Main module for updating document attributes in MongoDB using pymongo.
"""
from typing import List


def update_topics(mongo_collection, name: str, topics: List[str]) -> None:
    """
    Change all topics of a school document based on the name
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
