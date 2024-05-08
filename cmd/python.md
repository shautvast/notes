## New python project with virtual env in ZED

* create $PROJECT
```bash
mkdir project; cd project
python -m venv .venv
activate `source .venv/bin/activate
```

* create pyrightconfig.json
```bash
echo '{  "venvPath": ".",  "venv": ".venv"}' >pyrightconfig.json
```
* `pip install ...`
* `zed .`


* to quit the venv: `deactivate`

* generate requirements.txt
```bash
pip3 freeze > requirements.txt
```
