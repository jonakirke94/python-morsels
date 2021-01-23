import csv
import configparser
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--collapsed', action="store_true")
parser.add_argument('editor_config')
parser.add_argument('output_name')

parsed = parser.parse_args()

config = configparser.ConfigParser()
config.sections()
config.read(parsed.editor_config)
sections = config.sections()

with open(parsed.output_name, 'wt', newline='') as output:
    writer = csv.writer(output, delimiter=",")

    if parsed.collapsed:
        # shouldn' be hardcoded
        writer.writerow(('header', 'indent_style', 'indent_size'))
        for sec in sections:
            arr = [sec]
            for key in config[sec]:
                arr.append(config[sec][key])
            writer.writerow(arr)
    else:
        for sec in sections:
            for key in config[sec]:
                writer.writerow((sec, key, config[sec][key]))
