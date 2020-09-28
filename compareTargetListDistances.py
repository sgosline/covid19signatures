'''
This scripts takes two lists of proteins and computes their distance
in the protein-protein interaciton network compared to related distances.
'''

import argparse
import igraph as ig
import pandas as pd


parser = argparse.ArgumentParser("Simple script that compares pairwise\
distances between two sets of lists in interaction network")
parser.add_argument()
parser.add_argument()

def main():
    '''
    Read in arguments and output distances
    '''
    args = parser.parse_args()


if __name__=='__main__':
    main()
