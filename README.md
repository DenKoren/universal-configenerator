Universal coniguration generator
========================

Universal configuration (and not only configuration) generator.
Simply it is CLI to Jinja2 (http://jinja.pocoo.org/) template engine with some common variables predefind like hostname, and fqdn.

It passes any variable from CLI to template engine to use them inside the template.

For example:
```bash
universal-configenerator --custom-option=custom_value template.jinja2 > parsed_template.conf
```

and use custom variable inside the template:

```
template sample.

this is template sample, which uses variable 'custom-option' initialized from CLI with value ${custom_option}
```

# IMPORTANT:
Python extension library argparse <= 1.1 has a bug makes it to take unknown optional arguments with spaces in values as a known positional ones. So, the code
```bash
universal-configenerator --custom-option="custom value" template.jinja2 > parsed_template.conf
```
will not work with argparse version <= 1.1 resulting an IOError exception with message "IOError: [Errno 2] No such file or directory: '--custom-option=custom value'".
