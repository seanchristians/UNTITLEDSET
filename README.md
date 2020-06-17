[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4)](./CODE_OF_CONDUCT.md)
[![License](https://img.shields.io/github/license/seanchristians/eponym)](./LICENSE)
![Language](https://img.shields.io/pypi/pyversions/eponym-alloy)
[![Version](https://img.shields.io/pypi/v/eponym-alloy)](https://pypi.org/project/eponym-alloy/)

![Closed Issues](https://img.shields.io/github/issues-closed/seanchristians/eponym)
![Commit Activity](https://img.shields.io/github/commit-activity/y/seanchristians/eponym)
[![Build Status](https://travis-ci.org/seanchristians/eponym.svg?branch=master)](https://travis-ci.org/seanchristians/eponym)

# EPONYM

Useful tool for generating variable names. Uses [wordsapi.com](https://wordsapi.com)

# Getting Started

## Source code

```sh
git clone https://github.com/seanchristians/eponym
pip3 install -r eponym/src/requirements.txt
```

## PyPI

```sh
pip3 install eponym-alloy
```

# Usage

Eponym can be used as part of a project or by itself. Pass a single string sentence to eponym.synonyms to generate an array of synonyms. eponym.rand takes that array as input and returns a word according to some options. Eponym relies on [WordsAPI](https://www.wordsapi.com/) to generate synonyms. To use the service, create an account on [RapidAPI](https://rapidapi.com/) and get a free API key for [WordsAPI](https://rapidapi.com/dpventures/api/wordsapi).

## API Key

The script can interpret an API key from three different sources:
- Any environment variable (defaults to `$APIKEY`)
- A file
- Direct input text
To set your API key, you can define it in the script or run `export APIKEY="[RapidAPI Application Key]"`

## Script functionality

```sh
usage: python3 -m eponym [-h] [-k KEY] [-l] [-w] [-s SEP] [-m MAX] words [words ...]

Variable name generator

positional arguments:
  words              list of input words

optional arguments:
  -h, --help         show this help message and exit
  -k KEY, --key KEY  api key
  -l, --lower        output lowercase
  -w, --words        output word count
  -s SEP, --sep SEP  word separator
  -m MAX, --max MAX  maximum word length for each synonym
```

## Purging the cache

The script will not automatically clear the cache when terms expire after 6 months. Instead, you can write a cron job to do it yourself or do it manually. Run `python3 -c "import eponym; eponym.cache.purge()"` to clear the cache of expired items.

# Caching

Eponym relies on [WordsAPI](https://www.wordsapi.com/). In order to reduce calls to the API and retain bandwidth, all requests go through `cache.get` which builds and maintains a local cache of searched results. `cache.py` refreshes the cache every `cache.timeDelta` which is currently set to 6 months.

# Languages

Currently, the project only supports English. This is due to both sole use of wordsapi.com and a filter which removes non English letters. See [CONTRIBUTING](CONTRIBUTING.md) to help out!

---

© 2020 Sean Christians
