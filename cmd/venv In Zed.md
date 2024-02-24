## New python project with virtual env in ZED

* create $PROJECT `mkdir project; cd project`
* create `python -m venv .venv`
* activate `source .venv/bin/activate` 

* create pyrightconfig.json
```json
{
  "venvPath": ".",
  "venv": ".venv"
}
```
* `pip install ...`
* `zed .`


* to quit the venv: `deactivate`
