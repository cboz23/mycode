#!/usr/bin/python3
import requests
from datetime import datetime

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# This function grabs our credentials
# It is easily recycled from our previous script
def returncreds():
    # First, I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    # Remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# This is our main function
def main():
    # First, grab credentials
    nasacreds = returncreds()

    # Get start date from user
    startdate = input("Enter start date in YYYY-MM-DD format: ")
    
    # Validate the date format
    try:
        datetime.strptime(startdate, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    # Optionally get end date from user
    enddate = input("Enter end date (optional, press Enter to skip): ")

    if enddate:
        # Validate the date format
        try:
            datetime.strptime(enddate, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return
        enddate = "&end_date=" + enddate
    else:
        enddate = ""

    # Make a request with the request library
    neowrequest = requests.get(NEOURL + "start_date=" + startdate + enddate + "&" + nasacreds)

    # Strip off json attachment from our response
    neodata = neowrequest.json()

    ## Display NASA's NEOW data
    print(neodata)

if __name__ == "__main__":
    main()

