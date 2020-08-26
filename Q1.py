import argparse
from bisect import bisect
import csv

def parse_arguments(): # pragma: no cover
    description = 'This script calculates the yield spread (return) between a corporate bond and its government bond benchmark.'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('input_file', help='Path to input file')
    parser.add_argument('output_file', help='Path to output file')
    return parser.parse_args() 

def read_bonds(filename):
    '''
    Processes the input csv and return a pair of lists:
        government_bonds, corporate_bonds
    
    Each list is formatted like this:
        [{'bond': 'G1', 'type': 'government', 'term': 9.4, 'yield': 3.7}, ...]
    '''
    def parse_numbers(bond_item):
        bond_item['term'] = float(bond_item['term'].split(' ')[0])
        bond_item['yield'] = float(bond_item['yield'][:-1])
        return bond_item
        
    def filter_type(bond_type):
        return lambda bond: bond['type'] == bond_type
        
    bonds = {}
    with open(filename) as csv_file:
        all_bonds = list(map(parse_numbers, csv.DictReader(csv_file)))
    government_bonds = list(filter(filter_type('government'), all_bonds))
    corporate_bonds = list(filter(filter_type('corporate'), all_bonds))

    return government_bonds, corporate_bonds

def sort_and_extract_terms(bonds):
    '''
    Sorts a list of bonds based on their term and returns the list of terms for the bonds
    '''
    bonds.sort(key=lambda bond: bond['term'])
    return list(map(lambda bond: bond['term'], bonds))

def find_government_benchmark(term, bonds, bond_terms):
    '''
    Takes: a term, a list of bonds, and a list containing the term of each bond.
    Returns: the bond in the list with the closest term to the specified term.
    Time Complexity: O(log(n)) - binary search using `bisect`
    '''
    next_higher_term = bisect(bond_terms, term)
    next_lower_term = next_higher_term - 1
    if next_higher_term == len(bonds):
        return bonds[next_lower_term]
    elif next_lower_term == -1:
        return bonds[next_higher_term]
    elif abs(bond_terms[next_higher_term] - term) < abs(bond_terms[next_lower_term] - term):
        return bonds[next_higher_term]
    else:
        return bonds[next_lower_term]

def calculate_benchmarks(input_file, output_file):
    '''
    Calculate the spread for all corporate bonds and their government bond benchmark
    Write the result to the output csv file.
    '''
    government_bonds, corporate_bonds = read_bonds(input_file)
    government_bond_terms = sort_and_extract_terms(government_bonds)
    
    with open(output_file, 'w') as output:
        writer = csv.DictWriter(output, fieldnames=['bond', 'benchmark', 'spread_to_benchmark'])
        writer.writeheader()

        # Time Complexity: O(n * log(n))
        for coporate_bond in corporate_bonds:
            benchmark = find_government_benchmark(coporate_bond['term'], government_bonds, government_bond_terms)
            spread = coporate_bond['yield'] - benchmark['yield']
            writer.writerow({'bond': coporate_bond['bond'], 'benchmark': benchmark['bond'], 'spread_to_benchmark': '%.2f%%' % spread})
            
def main(): # pragma: no cover
    args = parse_arguments()
    calculate_benchmarks(args.input_file, args.output_file)
    
if __name__ == '__main__': # pragma: no cover
    main()
