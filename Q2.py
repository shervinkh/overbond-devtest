import argparse
from bisect import bisect
import csv

from Q1 import read_bonds, sort_and_extract_terms

def parse_arguments(): # pragma: no cover
    description = 'This script calculates the spread to the government bond curve.'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('input_file', help='Path to input file')
    parser.add_argument('output_file', help='Path to output file')
    return parser.parse_args()

def calculate_interpolation(term, bonds, bond_terms):
    '''
    Takes: a term, a list of bonds, and a list containing the term of each bond.
    Returns: the interpolated government yield for the specified term.
    Time Complexity: O(log(n)) - binary search using `bisect`
    '''
    next_higher_term = bisect(bond_terms, term)
    next_lower_term = next_higher_term - 1
    
    # Assume that there is always a lower government term and a higher
    assert (next_higher_term < len(bonds) and next_lower_term >= 0)
    
    term1, term2 = bonds[next_lower_term]['term'], bonds[next_higher_term]['term']
    yield1, yield2 = bonds[next_lower_term]['yield'], bonds[next_higher_term]['yield']
    slope = (yield2 - yield1) / (term2 - term1)
    return yield1 + slope * (term - term1)

def calculate_spread_to_curve(input_file, output_file):
    '''
    Calculate the spread to the government bond curve for all corporate bonds
    Write the result to the output csv file.
    '''
    government_bonds, corporate_bonds = read_bonds(input_file)
    government_bond_terms = sort_and_extract_terms(government_bonds)
    
    with open(output_file, 'w') as output:
        writer = csv.DictWriter(output, fieldnames=['bond', 'spread_to_curve'])
        writer.writeheader()

        # Time Complexity: O(n * log(n))
        for coporate_bond in corporate_bonds:
            government_interpolation = calculate_interpolation(coporate_bond['term'], government_bonds, government_bond_terms)
            spread = coporate_bond['yield'] - government_interpolation
            writer.writerow({'bond': coporate_bond['bond'], 'spread_to_curve': '%.2f%%' % spread})
            
def main(): # pragma: no cover
    args = parse_arguments()
    calculate_spread_to_curve(args.input_file, args.output_file)
    
if __name__ == '__main__': # pragma: no cover
    main()
