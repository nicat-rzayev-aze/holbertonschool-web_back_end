#!/usr/bin/env python3
"""
Main module for filtering MongoDB documents by a specific topic using pymongo.
"""
from typing import List, Dict, Any


def schools_by_topic(mongo_collection, topic: str) -> List[Dict[str, Any]]:
    """
    Return a list of schools having a specific topic.
    """
    return list(mongo_collection.find({"topics": topic}))
