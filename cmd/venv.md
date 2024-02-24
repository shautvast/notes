## New python project with virtual env in ZED

* create $PROJECT `mkdir project; cd project`
* create `python -m venv .venv`
* activate `source .venv/bin/activate` 
* `deactivate`
* create pyrightconfig.json
```json
{
  "venvPath": ".",
  "venv": ".venv"
}
```
* `pip install ...`
* `zed .`


