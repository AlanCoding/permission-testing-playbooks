#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os

from ansible.module_utils.basic import * # noqa

DOCUMENTATION = '''
---
module: full_env
short_description: Returns info about the place where the playbook run.
description:
    - Return env vars and playbook files in return data.
version_added: "2.7"
options:
requirements: []
author: Alan Rominger
'''

def main():
    module = AnsibleModule(argument_spec=dict(
        dir=dict(required=True, type='str')
    ))
    my_env = dict(os.environ)
    d = module.params['dir']
    file_list = [os.path.join(dp, f) for dp, dn, flns in os.walk(d) for f in flns]
    my_files = {}
    for filename in file_list:
        with open(filename, 'r') as f:
            my_files[filename.replace(d + os.path.sep, '')] = f.read()
    results = dict(full_env=my_env, full_files=my_files)
    module.exit_json(**results)

main()
