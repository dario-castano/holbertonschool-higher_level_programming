#!/bin/bash
# Causes the server to respond with a message containing You got me!, in the body of the response.
curl -L -d "user_id=98" -H "Origin: HolbertonSchool" -X PUT 0.0.0.0:5000/catch_me
