import networkx as nx
import sys
sys.path.insert(0, 'code/')
from Utils import *
import pandas as pd

import accessibility
import breadth
import data_amount
import data_qual
import recency


def get_single_data(url, lst, f):
    """
        Tries a url with a certain category, then if it returns the correct data type
        and doesn't errror, then it will add the score from the category into the
        list. Returns the list.
        """
    try:
        temp = f.main(url)
        if type(temp) != int or type(temp) != float:
            return "N"
    except:
        return "N"
    return temp

def main():
    """
        Goes through all of the cities in the all_cities dataset, populates all of the
        cities with an appropriate score or 'N' if the scoring functions don't work.
    """
    all_city_dataset = 'data/all_city_data.csv'
    accessibility_list = []
    breadth_list = []
    quality_list = []
    amount_list = []
    recency_list = []
    category_dict = {accessibility: accessibility_list,
        breadth:breadth_list,
            data_amount: amount_list,
                data_qual: quality_list,
                    recency: recency_list}
    df = read_from_csv(all_city_dataset)
    for url in df['City Open Data URL']:
        for func in category_dict:
            category_dict[func] += get_single_data(url, category_dict[func], func.main)
            print('Checking {} for {}'.format(url, func.name()))
    for mod in category_dict:
        write_to_csv(mod.name(), category_dict[mod], all_city_dataset)
    return category_dict
main()
