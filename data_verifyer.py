#!/usr/bin/env python3
"""

"""

import requests

BACKEND_ENDPOINT = "https://archive.kbb1.com/backend/content_units"
CONTENT_UNIT_URL = "https://archive.kbb1.com/en/programs/full/"
PAGE_SIZE = 1000


def get_total():
    r = requests.get(BACKEND_ENDPOINT, params={'page_no': '1', 'page_size': '10', "language": 'en'})
    return r.json()['total']


def fetch_content_unts(page_no=1, page_size=PAGE_SIZE):
    r = requests.get(BACKEND_ENDPOINT, params={'page_no': str(page_no), 'page_size': str(page_size), "language": 'en'})
    return r.json()['content_units']


def fetch_cu_ids(content_units):
    cu_ids = []
    if not content_units:
        raise ValueError("content_units are empty")
    for cu in content_units:
        cu_ids.append(cu['id'])
    return cu_ids


def fetch_content_unit_files_data(cu_id, lang="en"):
    if not cu_id:
        raise ValueError("Emtpy content unit ID")
    r = requests.get(BACKEND_ENDPOINT + "/" + cu_id, params={"language": lang})
    return r.json()['files']


def run_content_units_test():
    total_pages = get_total() // PAGE_SIZE

    for page in range(1, total_pages):
        print("--------------- PAGE: {} -----------------".format(page))
        cu_ids = fetch_cu_ids(fetch_content_unts(page, PAGE_SIZE))
        for cu_id in cu_ids:
            files_data = fetch_content_unit_files_data(cu_id)
            for file in files_data:
                print("File: {}".format(file['name']))


def main():
    run_content_units_test()


if __name__ == "__main__":
    main()
