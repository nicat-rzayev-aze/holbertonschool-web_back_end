#!/usr/bin/env python3
"""Module for pagination helper function."""


def index_range(page: int, page_size: int) -> tuple:
    """Calculate the start and end indexes for a given page and page size"""
    
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
