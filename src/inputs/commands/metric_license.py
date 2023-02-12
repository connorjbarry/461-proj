import requests
import json
import sys
import numpy as np
from dotenv import load_dotenv
import os

load_dotenv()

GH_token = os.getenv("GITHUB_TOKEN")


def import_package_github(url, token):
    try:
        # Imports the license dictionary from the URL
        response = requests.get(
            url, headers={'Authorization': f'token {token}'})
        data = response.json()
        license_info = data.get("license", {})
        return license_info
    except:
        ### Invalid URL ###
        return -1


def import_package_npmjs(url):
    try:
        # Imports the license dictionary from the URL
        response = requests.get(url)
        data = response.json()
        license_info = data.get("license", "")
        return license_info
    except:
        ### Invalid URL ###
        return -1


def calc_license_github(data, url):
    # if text contains the list of approved licenses for LGPL 2.1, score is 1
    # if not, the score is 0

    ### Compatible Licenses ###
    # Sources: https://www.gnu.org/licenses/license-list.en.html and https://spdx.org/licenses/
    list_of_licenses = ["LGPL-2.1", "LGPL-2.0", "GPL-2.0", "GPL-2.1", "	Apache-2.0", "	Artistic-2.0",
                        "ClArtistic", "BSD-3-Clause-LBNL", "BSL-1.0", "BSD-3-Clause", "CECILL-2.0",
                        "CECILL-2.1", "BSD-3-Clause-Clear", "eCos-2.0", "ECL-2.0", "EUDatagrid",
                        "FreeBSD-DOC", "FTL", "HPND", "iMatix", "Imlib2", "	IJG", "Intel", "ISC",
                        "MPL-1.1", "MPL-2.0", "OLDAP-2.7", "Python-2.0", "Ruby", "SMLNJ", "Unicode-TOU",
                        "UPL-1.0", "Unlicense", "Vim", "W3C", "WTFPL", "X11", "Zlib", "ZPL-2.0", "MIT"]
    # Compatible Licenses: GPL-2, GPL-2.1, LGPL-2, LGPL-2.1, Apache2.0,
    # ArtisticLicense2.0, ClarifiedArtisticLicense, BerkeleyDB, Boost,
    # ModifiedBSD, CeCILL2, ClearBSD, eCos2.0, ECL2.0,
    # EUDataGrid, Expat, FreeBSD, Freetype, HPND, iMatix, imlib2, IJGL,
    # INTEL, ISC, MPL-2.0, MPL-2.1, NCSA, OpenLDAP-2.7, Python2.0,
    # Ruby, StandardMLofNJ, Unicode, UPL, Unlicense, Vim, W3C, WTFPL2,
    # X11License, ZLib, Zope2.0, MIT

    if data is not None and data.get("spdx_id") in list_of_licenses:
        return 1
    else:
        return 0


def calc_license_npmjs(data, url):
    # if text contains the list of approved licenses for LGPL 2.1, score is 1
    # if not, the score is 0

    ### Compatible Licenses ###
    # Sources: https://www.gnu.org/licenses/license-list.en.html and https://spdx.org/licenses/
    list_of_licenses = ["LGPL-2.1", "LGPL-2.0", "GPL-2.0", "GPL-2.1", "	Apache-2.0", "	Artistic-2.0",
                        "ClArtistic", "BSD-3-Clause-LBNL", "BSL-1.0", "BSD-3-Clause", "CECILL-2.0",
                        "CECILL-2.1", "BSD-3-Clause-Clear", "eCos-2.0", "ECL-2.0", "EUDatagrid",
                        "FreeBSD-DOC", "FTL", "HPND", "iMatix", "Imlib2", "	IJG", "Intel", "ISC",
                        "MPL-1.1", "MPL-2.0", "OLDAP-2.7", "Python-2.0", "Ruby", "SMLNJ", "Unicode-TOU",
                        "UPL-1.0", "Unlicense", "Vim", "W3C", "WTFPL", "X11", "Zlib", "ZPL-2.0", "MIT"]
    # Compatible Licenses: GPL-2, GPL-2.1, LGPL-2, LGPL-2.1, Apache2.0,
    # ArtisticLicense2.0, ClarifiedArtisticLicense, BerkeleyDB, Boost,
    # ModifiedBSD, CeCILL2, ClearBSD, eCos2.0, ECL2.0,
    # EUDataGrid, Expat, FreeBSD, Freetype, HPND, iMatix, imlib2, IJGL,
    # INTEL, ISC, MPL-2.0, MPL-2.1, NCSA, OpenLDAP-2.7, Python2.0,
    # Ruby, StandardMLofNJ, Unicode, UPL, Unlicense, Vim, W3C, WTFPL2,
    # X11License, ZLib, Zope2.0

    if isinstance(data, dict):
        license_id = data.get("type")
    elif isinstance(data, str):
        license_id = data
    else:
        license_id = None

    if license_id in list_of_licenses:
        return 1
    else:
        return 0


def score(url, url_for_json):
    license_score = 0
    # scores the URLs for license compatibility
    url = url
    if "github" in url:
        package_data = import_package_github(url, GH_token)
        # will run if data is imported correctly
        if package_data != -1:
            license_score = calc_license_github(package_data, url)

    elif "npmjs" in url:
        package_data = import_package_npmjs(url)
        # will run if data is imported correctly
        if package_data != -1:
            license_score = calc_license_npmjs(package_data, url)

    # write data to output file
    try:
        with open("src/inputs/commands/metrics.json", "r") as f:
            data = json.load(f)
    except:
        data = {}
    if url_for_json in data:
        data[url_for_json]["License"] = license_score
    else:
        data[url_for_json] = {"License": license_score}

    # Write the updated JSON data back to the file
    with open("src/inputs/commands/metrics.json", "w") as f:
        json.dump(data, f, indent=4)
    print(license_score)
    return


if __name__ == "__main__":
    print(sys.argv[1], sys.argv[2])
    score(sys.argv[1], sys.argv[2])
