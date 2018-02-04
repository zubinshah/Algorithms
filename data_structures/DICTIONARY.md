##Dictionary

Dictionary, associative array, map , symbol table : represents an abstract data type which represents or is composed of (key, value) pairs. This data type permits access to data by its content or *key* value . 

#Operations
Dictionary : collection of a key/value pair and each *key* appears unique (at most) once. Following typical operations are required:
     + addition (of a key/value pair)
     + removal (of a key/value pair)
     + retrieval (lookup/search of a key/value pair)
     + modification (of an existing key/value pair)
Certain dictionary implementations efficiently support useful operations like : 
     + Min(D) or Max(D) : Retrieve an item with the smallest (or largest) key from D. This enables dictionary to serve as a priority queue.
     + Predecessor (D, x) or Successor (D, x) : Retrive the item from D whose key is immediately before (or after) x in sorted fashion.

Also referred to as an associative array or map or symbol table.

Some interesting notes on dictionary implementation are listed on this Wikipedia article: https://en.wikipedia.org/wiki/Associative_array#Implementation.
     + Hash Table
     + Search Trees

