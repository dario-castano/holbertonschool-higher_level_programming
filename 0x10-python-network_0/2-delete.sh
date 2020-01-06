#!/bin/bash
# sends a DELETE request to URL passed as arg, displays the body of the response
curl -sX "DELETE" "$1"
