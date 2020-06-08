[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4)](./CODE_OF_CONDUCT.md)
[![License](https://img.shields.io/github/license/seanchristians/eponym)](./LICENSE)
![Language](https://img.shields.io/github/languages/top/seanchristians/eponym)

![Closed Issues](https://img.shields.io/github/issues-closed/seanchristians/eponym)
![Commit Activity](https://img.shields.io/github/commit-activity/y/seanchristians/eponym)
[![Build Status](https://travis-ci.org/seanchristians/eponym.svg?branch=master)](https://travis-ci.org/seanchristians/eponym)

# EPONYM

Useful tool for generating variable names. Uses thesaurus.com

# Getting Started

Download the project. Make sure to move it to a directory included in your `$PYTHONPATH`
```sh
git clone https://github.com/seanchristians/eponym
```
(Coming to PyPi soon)

# Usage

Eponym can be used as part of a project or by itself. Pass a single string sentence to eponym.synonyms to generate an array of synonyms. eponym.rand takes that array as input and returns a word according to some options.

```sh
usage: p3 -m eponym [-h] [-l] [-w] [-s SEP] [-m MAX] words [words ...]

Variable name generator

positional arguments:
  words              list of input words

optional arguments:
  -h, --help         show this help message and exit
  -l, --lower        output uppercase
  -w, --words        output word count
  -s SEP, --sep SEP  word separator
  -m MAX, --max MAX  maximum word length for each synonym
```

# Caching

Eponym relies on thesaurus.com. This site has been chosen for it's reliability and popularity. Thesaurus.com does not have an accessible API. Therefore, each word must be individually queried on the main page. Large volumes of searches would be bad for this site. As such, it's important to cache results not only for faster execution speed, but also to save their bandwidth. Hopefully they get an API soon. If you know of a site with an API to access synonyms, please see [CONTRIBUTING](./CONTRIBUTING.md). **TL/DR**: don't delete `.cache`.

I am looking into implementing [bradleyfowler123/thesaurus-api](https://github.com/bradleyfowler123/thesaurus-api). Please see [CONTRIBUTING](./CONTRIBUTING.md) to help out with caching issues.

# Languages

Currently, the project only supports English. This is due to both sole use of thesaurus.com and a filter which removes non English letters. See [CONTRIBUTING](./CONTRIBUTING.md) to help out!

# Disclaimer

Although this is stated in the Limitation of Liability in the [license](./LICENSE), I feel the need to restate this here: This project and the maintainers of this project do not assume responsibility for the actions of individuals using the project. We do not support or condone malicious action against [thesaurus.com](https://www.thesaurus.com) such as Denial of Service attacks and breach of their [Terms of Service](https://www.dictionary.com/e/terms/) arising from use of this project.

---

© 2020 Sean Christians