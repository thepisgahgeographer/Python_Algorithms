#!/usr/bin/env python3

import sys
import os
import re

import glob

profile_mappings = \
    {'your_enterprise_profile': "url='https://pythonapi.playground.esri.com/portal', "\
                                "username='arcgis_python', "\
                                "password='amazing_arcgis_123'",
     'your_online_profile': "url='https://arcgis.com/', "\
                            "username='arcgis_python', "\
                            "password='P@ssword123'" }

regex_find_base = r"profile.*=.*(\\\"|').*{profile_str}.*(\\\"|')"

def _replace_profiles(file_contents):
    for key, value in profile_mappings.items():
        regex_find = regex_find_base.format(profile_str=key)
        regex_replace = value
        file_contents = re.sub(regex_find, regex_replace, file_contents)
    return file_contents

def _main():
    root_dir = os.path.abspath(os.path.join(
        os.path.dirname( __file__ ),
        '..',
        '..'))
    guide_dir = os.path.join(root_dir, "guide")
    samples_dir = os.path.join(root_dir, "samples")
    labs_dir = os.path.join(root_dir, "labs")
    nb_file_paths = \
        glob.glob(os.path.join(guide_dir, "**", "*.ipynb"), recursive=True) + \
        glob.glob(os.path.join(samples_dir, "**", "*.ipynb"), recursive=True) + \
        glob.glob(os.path.join(labs_dir, "**", "*.ipynb"), recursive=True)

    for nb_file_path in nb_file_paths:
        print(f"Replacing profiles in {nb_file_path}")
        f = open(nb_file_path, "r")
        file_contents = f.read()
        file_contents = _replace_profiles(file_contents)
        f.close()
        f = open(nb_file_path, "w")
        f.write(file_contents)
        f.close()
        print(f"    Finished!")

if __name__ == "__main__":
    sys.exit(_main())

