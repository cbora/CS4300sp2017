# cs4300sp2017
Repo for CS4300 project
## Quickstart


Numpy matrix link: https://s3.amazonaws.com/cs4300/sims_array.npy


(1) Install heroku-cli using this linkk:


       https://devcenter.heroku.com/articles/heroku-cli



(2) Clone Repo


       git clone https://github.com/cbora/cs4300sp2017


(3) install dependencies using


        pip install -r requirements.txt


(4) Make an .env file in root dir of App with these basic settings


        export APP_SETTINGS=config.DevelopmentConfig
        export DATABASE_URL=postgresql://localhost/my_app_db



(5) Run this to setup autoenv


        echo "source `which activate`" >> ~/.?rc
        source ~/.?rc 



(6) Start app from root dir


        python run.py



If you are having trouble running this with conda like I did, just skip steps (5) and (6) and do


      pip install -e . --process-dependency-links

      cs4300 server
    
    


Extended docs here https://github.com/CornellNLP/CS4300_Flask_template
