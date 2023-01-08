#!/usr/bin/env python
from sbpars.app import parser, export_to_csv


def main():
    print("Hi! I parse sberbank transactions file.\nTrying to parse...")
    data = parser()
    print("Successfully parsed index.html file")
    export_to_csv(data)
    print("Successfully exported to .csv table\nWell done!")


if __name__ == '__main__':
    main()
