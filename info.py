#!/usr/bin/env python

import pkg_resources
from pprint import pprint

pprint([x for x in pkg_resources.working_set])

