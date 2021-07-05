# Linux Setup

`for linux`

## flask server

- clone the repo

```bash
git clone https://github.com/search-magician/search_magician.git
```

- set up venv
( make sure that you have the venv activated when you run the app or install any new modules)

```bash
cd ./server
python3 -m venv .env
source .env/bin/activate
```

- install the requirements

```bash
pip3 install -r requirements.txt
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_trf
```

- install elasticsearch
```bash
curl -fsSL https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -

echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list

sudo apt update

sudo apt install elasticsearch
```
- config max memory 
``` bash
sudo nano /etc/elasticsearch/jvm.options
```

``` vim 
# Xms represents the initial size of total heap space
# Xmx represents the maximum size of total heap space

-Xms1g ##uncomment and edit here "Xms<memory size>g" 3 to 4 should be fine 
-Xmx1g ##uncomment and edit here "Xms<memory size>g" 3 to 4 should be fine
```


- setup the elastic mapping
``` bash
python3 elasticSetup.py

# add testing data ( you should run the flask server first )
curl --location --request POST 'http://localhost:5000/playlists/PL96C35uN7xGLafls3cRlsSGGjjXiiqHTU' \
--data-raw ''

# test the search 
curl --location --request GET 'http://localhost:5000/search?q=games'    
```

- run elasticsearch service

``` bash 
sudo service elasticsearch start
```

- run the server
```bash
FLASK_APP=src FLASK_ENV=development YOUTUBE_API_KEY = "AIzaSyDtrJTNrq_Czfa261UXZIoqkLeo5sizg-I" flask run
```
- before you commit stage your changes and run pre-commit to ensure everything is OK :)
```bash
git add very_cool_file_name.py
pre-commit
```
- bonus (add this to your ~/.bashrc automatically activate virtualenvs when cd )
```bash
function cd() {
  if [[ -d ./.env ]] ; then
    deactivate
  fi

  builtin cd $1

  if [[ -d ./.env ]] ; then
    . ./.env/bin/activate
  fi
}
```


# Windows Setup

`for windows`

## flask server

- clone the repo

```bash
git clone https://github.com/search-magician/search_magician.git
```

- set up venv
( make sure that you have the venv activated when you run the app or install any new modules)

```bash
cd ./server
python3 -m venv .env
source .env/bin/activate
```

- install the requirements

```Terminal
pip3 install -r requirements.txt
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_trf
```

- Install the elasticsearch package with pip inside the virtual environment
```Terminal
python -m pip install elasticsearch
python -m pip install elasticsearch[async]
```
- Install the elasticsearch service with msi 
1- Download the .msi package for Elasticsearch v7.13.2 from https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.13.2.msi
2- Double-click the downloaded .msi package to launch a GUI wizard that will guide you through the installation process. You can view help on any step by clicking the ? button, which reveals an aside panel with additional information for each input.
3- Within the first screen, select the directory for the installation. In addition, select directories for where data, use the default locations.
4- Then select to install as a service 
5- Set the max memory to 4 GB
6- Select trial license 
7- Click install


- setup the elastic mapping
``` Terminal
python3 elasticSetup.py

# add testing data ( you should run the flask server first )
curl --location --request POST 'http://localhost:5000/playlists/PL96C35uN7xGLafls3cRlsSGGjjXiiqHTU' \
--data-raw ''

# test the search 
curl --location --request GET 'http://localhost:5000/search?q=games'    
```

- run elasticsearch service

``` CMD 
sc.exe start Elasticsearch
```

- Run the server
```bash
FLASK_APP=src FLASK_ENV=development YOUTUBE_API_KEY = "AIzaSyDtrJTNrq_Czfa261UXZIoqkLeo5sizg-I" flask run
```
