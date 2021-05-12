#!/usr/bin/env python3
import csv
with open("csv_users.txt", "r") as data:
    counter= 0
    # generate unique number
    # give all files unique names
    for row in csv.reader(data):
        counter += 1
        filename= f"admin.rc{counter}"
        with open(filename, "w") as rcfile:
            print("export OS_AUTH_URL=" + row[0], file=rcfile)
            print("export OS_IDENTITY_API_VERSION=3", file=rcfile)
            print("export OS_PROJECT_NAME=" + row[1], file=rcfile)
            print("export OS_PROJECT_DOMAIN_NAME=" + row[2], file=rcfile)
            print("export OS_USERNAME=" + row[3], file=rcfile)
            print("export OS_USER_DOMAIN_NAME=" + row[4], file=rcfile)
            print("export OS_PASSWORD=" + row[5], file=rcfile)

