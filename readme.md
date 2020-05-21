# ticker_terms

Source files for ticker_terms and all development related to it. pypi package to generate all possible names combinations for public company executives. Used in the backend of [Newscatcher](https://newscatcherapi.com/).

## Installation

```bash
pip install ticker_terms
```

## Usage


```python
from ticker_terms import Company

corp = Company('AAPL')
corp.terms[0] #first executive
corp.terms[0][1] #official name for first executive
corp.terms[0][1:] #remaining possible nicknames
corp.terms[1] #second executive
corp.terms[1][1] #official name for second executive
corp.terms[1][1:] #remaining possible nicknames

```