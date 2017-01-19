import re

TESSERACT_MAJOR_VERSION = ""
TESSERACT_MINOR_VERSION = ""
# dig out the version from Tesseract sources
VERSION_FILE_PATH = "tesseract/CMakeLists.txt"

with open(VERSION_FILE_PATH, 'r') as f:
    major_version_regex = re.compile("set\(VERSION_MAJOR (.+)\)")
    minor_version_regex = re.compile("set\(VERSION_MINOR (.+)\)")
    for line in f:
        major = major_version_regex.match(line)
        if major:
            TESSERACT_MAJOR_VERSION = major.group(1)

        minor = minor_version_regex.match(line)
        if minor:
            TESSERACT_MINOR_VERSION = minor.group(1)

        if TESSERACT_MAJOR_VERSION and TESSERACT_MINOR_VERSION:
            break

print("Version: {}{}".format(TESSERACT_MAJOR_VERSION, TESSERACT_MINOR_VERSION))

with open('ts_version.py', 'w') as f:
    f.write('tesseract_version = "{}{}"'.format(TESSERACT_MAJOR_VERSION, TESSERACT_MINOR_VERSION))
