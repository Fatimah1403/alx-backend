#!/usr/bin/env python3
"""
get_page that takes two integer arguments page withdefault
value 1 and page_size with default value 10.
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        return a tuple of size two containing a start index
        and an end index corresponding to the range of indexes
    """
    start_index = 0
    end_index = 0

    for i in range(page):
        start_index = end_index
        end_index += page_size
    return (start_index, end_index)


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
        assert(isinstance(page, int) and isinstance(page_size, int))
        assert(page > 0 and page_size > 0)

        dataset = self.dataset()
        start_end = index_range(page, page_size)
        if start_end:
            return dataset[start_end[0]:start_end[1]]
        return []


def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
    """
    Returns a dict of:
    page_size: the length of the returned dataset page
    page: the current page number
    data: the dataset page (equivalent to return from previous task)
    next_page: number of the next page, None if no next page
    prev_page: number of the previous page, None if no previous page
    total_pages: the total number of pages in the dataset as an integer
    """
    total_pages = len(self.dataset())
    dataset_rec = self.get_page(page, page_size)

    data_info = {
        "page": page,
        "page_size": len(dataset_rec),
        "data": dataset_rec,
        "next_page": page + 1 if (page + 1) <= total_pages else None,
        "prev_page": page - 1 if (page - 1) > 1 else None,
        "total_pages": total_pages
    }
    return data_info
