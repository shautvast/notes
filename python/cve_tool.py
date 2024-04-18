#!/usr/bin/env python3

# read and parse whitelist.yaml file
# lookup all CVE's mentioned
# generate a list of fix versions
##
# requirements.txt
##
# certifi==2024.2.2
# charset-normalizer==3.3.2
# idna==3.7
# jq==1.7.0
# PyYAML==6.0.1
# requests==2.31.0
# urllib3==2.2.1
###
import yaml
import sys
import requests
import time
import jq

def print_err(txt):
    print(f"\033[91mError: {txt}\033[00m")

def print_info(txt):
    print(f"\033[92m{txt}\033[00m")


def print_help_and_exit():
    print_err("Not enough arguments")
    print_err("Usage:")
    print_err("cve_tool [whitelist.yaml]")
    exit(-1)


if len(sys.argv) <2:
    print_help_and_exit()

whitelist_file = sys.argv[1]

with open(whitelist_file) as stream:
    try:
        whitelist = yaml.safe_load(stream)
    except yaml.YAMLError as exception:
        print_err(exception)
        exit(-1)

def flatten(matrix):
     flat_list = []
     for row in matrix:
         flat_list.extend(row)
     return flat_list

for (cve, vulns) in whitelist["vulnerabilities"].items():

    libs = flatten(map((lambda vuln: list(vuln.keys())), vulns))
    if cve.startswith("CVE"):
        cve_info = requests.get(f"https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={cve}",
        ).json()
        print_info(f"{cve} {libs}")
        print_info(list(jq.compile("..|objects|.versionEndExcluding//empty").input_value(cve_info)))

        time.sleep(2) # this is for preventing api rate limits

