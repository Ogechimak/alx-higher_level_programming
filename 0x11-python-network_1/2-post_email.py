#!/usr/bin/python3
"""Sends a POST request with email as a parameter"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    # Get URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email parameter
    data = urllib.parse.urlencode({'email': email}).encode()

    # Create a request object
    request = urllib.request.Request(url, data=data, method='POST')

    # Send the request and handle the response
    with urllib.request.urlopen(request) as response:
        # Read and decode the response body
        body = response.read().decode('utf-8')

        # Display the decoded response body
        print(body)
