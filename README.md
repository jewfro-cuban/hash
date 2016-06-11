# HashTable
Simple Hash table implementation in pyhton with fixed size.

In (key, value) pair `key` can only be integer

## Installation

### Using `pip`
```
sudo pip install HashTable
```

### From git-repo

```
git clone https://github.com/munendrasn/hash.git
cd hash
sudo python setup.py install
```
## Usage

```
>>>from hash import HashTable
>>>h = HashTable()

>>>h[20] = 'use' # only int as key
>>>h[123] = 43
>>>h             # Display hash table 
{ 20:use, 123:43 }
>>>h.pop(12)
'use'
>>>h.set(65, 'check')
>>>h
{ 20:use, 123:43, 65:check }

```

## Contact
For any queries, feel free to reach me at  *sn.munendra52 [at] gmail [dot] com*