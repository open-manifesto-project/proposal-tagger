PROPOSAL TAGGER
================

Module that retrieves and labels manifesto proposals with [TiPi Ciudadano](tipiciudadano.es) or [Parlamento2030](parlamento2030.es) topics.

## Requirements

* Python 3.6
* Virtualenv (created and activated)


## Setup

```
git clone git@github.com:open-manifesto-project/proposal-tagger.git
cd proposal-tagger
pip install -r requirements.txt
cp proposal-tagger/settings.py.example proposal-tagger/settings.py
```

Finally, configure the module editing *proposal-tagger/settings.py* file.


## Run

```
python run.py
```


## Additional notes

If you want to transform JSON to CSV, just use **[json2scv](https://www.npmjs.com/package/json2csv)** command line tool.
