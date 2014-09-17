#!/usr/bin/env python2.7

from mako.template import Template
import socket
import argparse
import re
import logging

host_fqdn = socket.getfqdn()
hostname = host_fqdn.split('.')[0]

template_variables = {
    "fqdn": host_fqdn,
    "hostname": hostname,
}


def parse_unknown_arguments(args):
    unknown_arguments = {}

    for argument in args:
        logging.debug("Parsing unknown argument '{0}'".format(argument))

        argument = argument.lstrip("\t -")
        try:
            arg_name, arg_value = argument.split("=")
            arg_name = arg_name.lstrip("-")
            arg_name = re.sub(r'[-/\\]', '_', arg_name)
            logging.debug("Parsed argument: arg_name='{0}', arg_value='{1}'".format(arg_name, arg_value))

            unknown_arguments[arg_name] = arg_value
        except ValueError:
            unknown_arguments[argument] = True

    return unknown_arguments


def parse_arguments(args=None):

    parser = argparse.ArgumentParser(prog="universal-configenerator",
                                     description="Universal config generator."
                                                 " Simple CLI interface to Mako template engine with default"
                                                 " configuration. Allows you to define variables from CLI"
                                                 " passing variable as option for command.",
                                     epilog="Example: %(prog)s --anyopt=anyval /tmpl/file > parsed_file")

    parser.add_argument("--debug", "-d", action="store_true",
                        help="Enable debug log messages")

    parser.add_argument("template_file", action="store", type=str,
                        help="Template file path")

    known_options, unknown_args = parser.parse_known_args()

    if known_options.debug:
        logging.root.setLevel("DEBUG")

    logging.debug("Known options: {0}".format(known_options))
    logging.debug("Unknown arguments: {0}".format(unknown_args))

    unknown_options = parse_unknown_arguments(unknown_args)

    return known_options, unknown_options


def main(args=None):
    options, additional_variables = parse_arguments(args=args)

    template = Template(filename=options.template_file, strict_undefined=True)
    template_variables.update(additional_variables)
    print template.render(**template_variables)

if __name__ == "__main__":
    main()
