# DD2480-CI
## Summary

A small continuous integration CI server. This CI server only contains the core features of continuous integration. The CI server keeps the history of the past builds. Each builds information is accessible through our API. 

## How to use

### Set up config for new repository

1. In `ci.ini`, add a personal access token with permissions for the public repository as well as the name of the MongoDB database and its API url.

2. Use Ngrok to set up a routing URL to localhost port 8017 for the webhook using `ngrok http 8017` and add the Ngrok URL as a webhook to the repo. 

### Running the code

Make sure to have python3 installed and run `pip3 install -r requirements.txt` to install the dependencies. 

From the root of the repo, run `python3 src/app.py` to start the application. That's it. 

To run static check and unittests locally, run `sh src/scripts.sh`. 

To generate documentation in the form of a html file, run the `generate_docs.sh` script using `sh generate_docs.sh`. The html file will be in the documentation folder.

## Statement of Contributions

The program was written by the group members together, often in meetings involving all or most of the members. Several parts of the startup, such as the code and git structure, was done collectively by most of the group. The rest of the work was divided among the members, see below.

Ali: Implemented core CI feature #1 an #2 with Klara, wrote README, wrote documentations, created test branches and tests for CI server.

Axel: Set up Ngrok hosting, set up Flask application and create request handlers, connect to MongoDB, fix Rest API to set commit status, incorporate HTML into application. 

Klara: Creating initial issues, implementing core CI feature #1 and #2 together with Ali, some documentation, writing Essence document.

Linus: Created notification file with Axel, wrote README, wrote documentations, wrote Essence document.

Maegan: Created the frontend for the webpages, helped with the setting up of MongoDB, and some documentation.

## Contributors

Ali Asbai

Axel Lervik

Klara Alpsten

Linus Below Blomkvist

Maegan Chen Peralta
