# setup

`for linux`


- set up venv
  ( make sure that you have the venv activated when you run the app or install any new modules)

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- install the requirements

  ```bash
  [1]install requirements
  cd scrapper
  pip3 install -r requirements.txt
  [2]install firefox web geckodriver
  cd venv/bin
  wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
  tar -xvzf geckodriver*
  ```

- run the script
  ```bash
  python bfs.py
  ```
