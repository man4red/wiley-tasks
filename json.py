#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Egor Egorenkov"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Egor Egorenkov"
__email__ = "it.manfred@gmail.com"
__status__ = "Development"

import json

jsonstr = """
[
  {
    "_id": "5bc44d3edf2b8798ce3c95bd",
    "tags": [
      "proident",
      "aute",
      "in",
      "laborum"
    ],
    "friends": [
      {
        "id": 0,
        "name": "Alyce Wall"
      },
      {
        "name": "Eloise Cervantes"
      },
      {
        "id": 2,
        "name": "Turner Morton"
      }
    ],
    "greeting": "Hello, stranger! You have 8 unread messages.",
    "favoriteFruit": "strawberry"
  },
  {
    "id": 1,
    "_id": "f4ee69a5-55a9-4cfd-ac4e-5eb525ec6d5a",
    "tags": [
      "radn1",
      "auto2",
      "out",
      "exploit"
    ],
    "friends": [
      {
        "id": 0,
        "name": "Mu Xaong"
      },
      {
        "id": 1,
        "name": "Irgem Stiv"
      },
      {
        "id": 2,
        "name": "In Kirisk"
      }
    ],
    "greeting": "I'm back.",
    "favoriteFruit": "apple"
  }
]"""

result = json.loads(jsonstr)

#print('dump:', json.dumps(result, indent=4))


def main():
    """ fetch the user’s friend’s name those “id” equals “2”, and has ‘laborum’ tag
  """
    for row in result:
        try:
            if 'laborum' in row['tags']:
                for friend in row['friends']:
                    if friend.get('id') == 2:
                        print(friend.get('name'))
                        continue
        except KeyError:
            pass


if __name__ == "__main__":
    main()
