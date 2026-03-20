#!/usr/bin/env python3

from eval import calculate
import log
import writer


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-D', '--debug', default=False, action='store_true', help="enable debug logging")
    parser.add_argument('-H', '--home', default=False, action='store_true', help="generate home page")
    parser.add_argument('-O', '--overview', default=False, action='store_true', help="generate overview page")
    parser.add_argument('-C', '--contact', default=False, action='store_true', help="generate contact page")
    parser.add_argument('-R', '--recommendations', default=False, action='store_true', help="generate recommendations page")
    parser.add_argument('-M', '--methodology', default=False, action='store_true', help="generate methodology page")
    parser.add_argument('-E', '--evaluations', default=False, action='store_true', help="generate methodology page")
    parser.add_argument('-A', '--all', default=False, action='store_true', help="generate all pages")
    args = parser.parse_args()

    if args.debug:
        log.setDebug()
        log.DEBUG('Logging set to DEBUG')

    if args.all:
        args.home = args.overview = args.contact = args.recommendations = args.methodology = args.evaluations = True

    if any((args.home, args.overview, args.evaluations)):
        data = calculate()
        # log.DEBUG(data.keys())

    if args.home:
        writer.index(data)
    if args.overview:
        writer.detailed_overview(data)
    if args.contact:
        writer.about()
    if args.methodology:
        writer.methodology()
    if args.recommendations:
        writer.recommendations()
    if args.evaluations:
        for summary in data:
            writer.evaluation(data[summary])


if __name__ == "__main__":
    main()
    