# setup

`for linux`

- clone the repo ( make sure that SSH key is set or use github app )

  ```bash
  git clone git@github.com:ben7bk-y-Andrew/search_magician.git
  ```

- set up venv
  ( make sure that you have the venv activated when you run the app or install any new modules)

  ```bash
  python3 -m venv .env
  source .env/bin/activate
  ```

- install the requirements

  ```bash
  pip3 install -r requirements.text
  ```

- run the server
  ```bash
  cd ./server
  FLASK_APP=src FLASK_ENV=development flask run
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
- Please retrain the model from main then selecting 1 (As the model size is larger than 100 MB)