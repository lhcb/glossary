#!/usr/bin/env python3

'''
Preprocessing script for LHCb Glossary gitbook.

'''

from pathlib import Path
import re

title_pattern = re.compile(r'''
    ^\#\#            # Starting two #
    \w*              # Optional unlimited whitespace
(?P<name> [^\{]*)    # Non-greedy anything but {
(?: \{\#
  (?P<link> .*)
\}  )?               # Links (Optional)
    \w*$             # End of string and optional whitespace

''', re.VERBOSE)

DIR = Path(__file__).resolve().parent
base = './glossary'
terms = '## Summary of terms'

# Read in old readme
with open('gitbook_readme.md', 'r') as f:
    txt = f.read()

# Make new readme; remove terms if this was run more than once
with open('gitbook_readme.md', 'w') as out:

    intro = txt.split(terms)[0]
    print(intro, file=out)
    print(terms, file=out)

    for fn in sorted((DIR.parent / 'glossary').glob('?.md')):
        letter = fn.stem
        with open(fn) as f:
            for line in f:
                if line.startswith('##'):
                    d = title_pattern.match(line).groupdict()
                    name = d['name'].strip()
                    link = d['link'] if d['link'] is not None else (name.replace(' ', '-')
                                                                        .replace(':', '')
                                                                        .replace('(', '')
                                                                        .replace(')','')
                                                                        .upper())

                    print(f"* [{name}]({base}/{letter}.md#{link})", file=out)
