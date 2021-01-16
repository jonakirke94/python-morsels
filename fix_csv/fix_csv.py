import csv

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('original_cars')
parser.add_argument('fixed_cars')
parser.add_argument('--in-delimiter', dest="delimiter")
parser.add_argument('--in-quote', dest="quotechar")

parsed = parser.parse_args()


with open(parsed.original_cars, 'rt',) as old:
    sample_bytes = 1024
    dialect = csv.Sniffer().sniff(old.read(1024))
    old.seek(0)  # set stream to beginning of file

    delimiter = parsed.delimiter if parsed.delimiter else dialect.delimiter
    quotechar = parsed.quotechar if parsed.quotechar else dialect.quotechar

    reader = csv.reader(old, delimiter=delimiter, quotechar=quotechar)
    with open(parsed.fixed_cars, 'wt', newline='') as new:
        writer = csv.writer(new, delimiter=',')
        for row in reader:
            writer.writerow(row)






