#!/usr/bin/env python3
"""
get_page that takes two integer arguments page withdefault
value 1 and page_size with default value 10.
"""
import csv
import math
from typing import List, Tuple
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """_summary_

        Args:
            page (int, optional): _description_. Defaults to 1.
            page_size (int, optional): _description_. Defaults to 10.

        Returns:
            List[List]: _description_
            You have to use this CSV file (same as the one presented
            at the top of the project)Use assert to verify
            that both arguments are integers greater than 0.
            Use index_range to find the correct indexes to paginate
            the dataset correctly and return the appropriate page
            of the dataset (i.e. the correct list of rows).
            If the input arguments are out of range for the dataset,
            an empty list should be returned.
        """
        assert (isinstance(page, int) and isinstance(page_size, int))
        assert (page > 0 and page_size > 0)

        dataset = self.dataset()
        start_end = index_range(page, page_size)
        if start_end:
            return dataset[start_end[0]:start_end[1]]
        return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Returns a page of the dataset.
        Args:
            page (int): The page number.
            page_size (int): The page size.
        Returns:
            List[List]: The page of the dataset.
        """
        total_pages = len(self.dataset()) // page_size + 1
        data = self.get_page(page, page_size)
        info = {
            "page": page,
            "page_size": page_size if page_size <= len(data) else len(data),
            "total_pages": total_pages,
            "data": data,
            "prev_page": page - 1 if page > 1 else None,
            "next_page": page + 1 if page + 1 <= total_pages else None
        }
        return info
