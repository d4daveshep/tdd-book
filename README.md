## Some setup instructions for building and running the code and tests ##
1. Download latest geckodriver and install to `/usr/local/bin`

1. Install github CLI `gh` following instructions from Github.org

1. Set up virtualenv  
`aptitude install python3-venv`  
`cd tdd-book`  
`python3 -m venv virtualenv`  

1. Activate the virtualenv with  
`source virtualenv/bin/activate`  

1. Python requirements.txt file needs django & selenium  
Inside virtualenv...  
`pip3 install -r requirements.txt`  




