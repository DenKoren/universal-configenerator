#!/usr/bin/env python2.7

from mako.template import Template
import socket
import argparse

host_fqdn = socket.getfqdn()
hostname = host_fqdn.split('.')[0]

template_variables = {
    "fqdn": host_fqdn,
    "hostname": hostname,
}


def parse_unknown_arguments(args):
    unknown_arguments = {}

    for argument in args:
        argument = argument.lstrip("\t -")
        try:
            arg_name, arg_value = argument.split("=")
            arg_name = arg_name.lstrip("-")
            unknown_arguments[arg_name] = arg_value
        except ValueError:
            unknown_arguments[argument] = True

    return unknown_arguments


def parse_arguments(args=None):
    
    parser = argparse.ArgumentParser(prog="Webserver config generator",
                                     description="Webserver configuration generator."
                                                 "Parses templates with Jinja2 template engine.")

    parser.add_argument("template_file", action="store", type=str,
                        help="Template file path", )

    known_options, unknown_args = parser.parse_known_args()

    unknown_options = parse_unknown_arguments(unknown_args)

    return known_options, unknown_options


def main(args=None):
    options, additional_variables = parse_arguments(args=args)

    template = Template(filename=options.template_file, strict_undefined=True)
    template_variables.update(additional_variables)
    print template.render(**template_variables)

if __name__ == "__main__":
    main()
