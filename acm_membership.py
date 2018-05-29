#!/usr/bin/python

# A useful little script for generating a CSV of club members using the survey
# output of acmwebsite/mozzarella.
#
# Make sure to install csmdirsearch from pip.
#
# The authtkt cookie can be found by logging into `acm.mines.edu` as an
# admin, and checking the cookie storage for "authtkt".


import requests
import argparse
import csv
import csmdirsearch

parser = argparse.ArgumentParser()
parser.add_argument('auth', type=str, help='authtkt cookie value for an acmwebsite admin')
parser.add_argument('first', type=int, help='the first survey # to use')
parser.add_argument('last', type=int, help='the last survey # to use')
parser.add_argument('output', type=argparse.FileType('w'), help='the output csv file')
args = parser.parse_args()

def get_responses(cookie, ids):
    s = requests.Session()
    cookies = { 'authtkt': cookie }
    for index in ids:
        try:
            r = s.get(f'https://acm.mines.edu/s/{index}/results.json', cookies=cookies)
            if not r.ok:
                print(f'!! could not load survey #{index}')
            for person in r.json()['responses']:
                yield person
        except:
            print(f'!! error while loading survey #{index}')

total = 0
missed = []

names = set()
emails = set()

fieldnames = ['last', 'first', 'email']
output = csv.DictWriter(args.output, fieldnames=fieldnames)

def process(p):
    # Get name
    name = p['name']
    print(f'considering {name}')
    splitname = name.split()
    if len(splitname) < 2:
        return 'name is not full'

    # First and last
    first = splitname[0]
    last = splitname[-1]
    if len(first) == 1 or len(last) == 1:
        return 'name uses intials'
    name = first + ' ' + last

    # Deduplicate
    if name not in names:
        names.add(name)
    else:
        return None

    # Get email
    email = p['email']
    if email is None:
        # CSM directory search
        print(f'  > finding email in csm directory')
        possible = list(csmdirsearch.search_by_name(name))
        if len(possible) > 1:
            return 'several possibilities'
        elif len(possible) == 0:
            return 'failed to find email'
        found = possible[0]
        print(f'  > found {found.name}')
        foundlast = found.name.last
        if foundlast.lower() != last.lower():
            return f'last names don\'t match ({foundlast})'
        email = found.business_email
        print(f'  > email is {email}')

    # Remove mymail shit
    email = email.replace('mymail.', '')

    # Deduplicate
    if email not in emails:
        emails.add(email)
    else:
        return None

    # Write to CSV
    print(f'  + outputting')
    output.writerow({
        'first': first,
        'last': last,
        'email': email,
    })
    return None

for p in get_responses(args.auth, range(args.first, args.last + 1)):
    total += 1
    try:
        err = process(p)
        if err is not None:
            print('  ! ' + err)
            name = p['name']
            missed.append((name, err))
    except Exception as e:
        print(f'!! could not process person: {e}')


print()
print(f'out of {total} records, {len(missed)} could not be processed:')
for (n, e) in set(missed):
    print(f'\t{n} : {e}')
