### DATA STRUCTURES : IMPLEMENTED IN THIS DIRECTORY
    + Radix Tree (radix trie or compact prefix tree)
    + Patricia Tree (radix=2)
    + r-ary tree
    + Trie
    + Binary tree (i.e. radix 2)
    + patricia tree: PATRICIA trees are radix trees with radix equals 2, 
          which means that each bit of the key is compared individually and each 
          node is a two-way (i.e., left versus right) branch.
    + Suffix Tree
    + LPM

### Trie, Prefix Trie, Radix Tree, Radix Trie, Compact Prefix Tree
    + data structure definition 
    + algorithms: insert/delete/lookup/traverse
    + add a practical example: test with 10K+ nodes or values

### Trie : data structure
    + ordered data structure
    + search tree used to store associative array or a dynamic set
    + unlike a bst, no node stores the key associated with that node, instead
      the its position in the tree defines the key with which it is associated 
    + all the descendants of a node have a common prefix string
    + values are not associated with all the nodes, instead they are associated
      with leaves, and some inner nodes which corresponds to keys of interest
    + Compact Prefix Trie : is a space optimized trie data structure (radix tree)

##  ADVANTAGES: TRIE (over other data structures)
    + TRIE over HASH TABLES
        1. LOOKING up data in trie is faster in worst case, over imperfect hash
           for eg. O(m) where m, is the length of the search string
           an imperfect hash can have hash collisions
        2. No COLLISIONS at all , because of different keys of a trie
        3. Buckets (for collisions) are required if the same key can mean different
           values
        4. NO need to define a HASH FUNCTION
        5. Naturally provides alphabetical ordering of entries by keys

    + DRAWBACKS :
        1. Slower in access compared to hash tables (considering hard-drives 
           and memory accesses)
        2. Scaled version : can occupy more space than a hash table.
    
    + TRIE over BST 
        1. Looking up keys is faster , worst case O(m) for a trie, versus O(log(m))
           for a binary search tree, where n=#of elements, and lookups depend on 
           the depth of the tree.
        2. Tries are more space efficient ,when they have lots of short keys
        3. Balancing a tree is the big concern, which is not there for a trie.

###Radix tree : data structure
    + space optimized trie
    + every node that is the only child is merged with its parent
    + Radix *r* : the number of children of an internal node is the radix r of 
      the radix tree.
    + edges can be labled with a sequence of elements as well as a single element;
      (unlike regular trie where only one element is represented by an edge)
    + radix trees are more efficient for small sets : and for sets of strings 
      that share long prefixes
   
Key at each node is compared with a **chunk-of-bits** , where the quantity of bits
in that chunk at that node is the radix r of the radix tree. For eg. when r is 2, the 
radix trie is a binary tree. (ie. node's 1-bit position corresponds to two values , hence
radix 2).

Binary tree minimizes sparseness at the expense of trie depth (hence is dense), while 
radix tree is very good for sparsely populated data sets.
   
#NOTES : (FROM www.wikipedia.com: this is well said comment.!! )
Unlike regular trees (where whole keys are compared en masse from their beginning up to the point of inequality), the key at each node is compared chunk-of-bits by chunk-of-bits, where the quantity of bits in that chunk at that node is the radix r of the radix trie. When the r is 2, the radix trie is binary (i.e., compare that node's 1-bit portion of the key), which minimizes sparseness at the expense of maximizing trie depth—i.e., maximizing up to conflation of nondiverging bit-strings in the key. When r is an integer power of 2 greater or equal to 4, then the radix trie is an r-ary trie, which lessens the depth of the radix trie at the expense of potential sparseness.

#Applications 
    + associative arrays
    + storing ip addresses (prefixes)
    + inverted indexing

#References and Resources:
https://en.wikipedia.org/wiki/Radix_tree
