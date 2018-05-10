### HOW to use this directory 

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

### Graph
A graph represents an abstract data type.

## Representation of graphs
A graph [G] primarily consists of vertices [V] and edges [E].

Both V and E represent an auxiliary information that is used to represent a problem and 
using known graph techniques can provide assistance to that problem.

A graph datastructure consists of (1) a finite set of vertices and (2) a finite 
set of ordered edges (u, v). The pair represents an order/direction for the edge 
representing an edge from u to v. The edges may contain weight/value/cost.

## Data structures to represent graphs
There are two primary ways to store graphs in computer systems :
    1. Adjacency Lists : better for sparse graphs due to memory overheads
    2. Adjacency Matrix : better for dense graph

List structures include the incidence list, an array of pairs of vertices, and the adjacency list, which separately lists the neighbors of each vertex: Much like the incidence list, each vertex has a list of which vertices it is adjacent to. (Ref. Wikipedia).

Matrix structures include the incidence matrix, a matrix of 0's and 1's whose rows represent vertices and whose columns represent edges, and the adjacency matrix, in which both the rows and columns are indexed by vertices. In both cases a 1 indicates two adjacent objects and a 0 indicates two non-adjacent objects. The Laplacian matrix is a modified form of the adjacency matrix that incorporates information about the degrees of the vertices, and is useful in some calculations such as Kirchhoff's theorem on the number of spanning trees of a graph. The distance matrix, like the adjacency matrix, has both its rows and columns indexed by vertices, but rather than containing a 0 or a 1 in each cell it contains the length of a shortest path between two vertices. (Ref. Wikipedia)

## Applications : 
    + Model various relations : physical, physiological, biological, social, informational systems, etc...
    + Social Networks : connections between individuals or entities
    + Networks : paths in a city, between locations, telephone networks, circuit networks, etc.
    + Networks : for communications, flow of informations, data organizations
    + Networks : where attributes are assigned to nodes and edges
    + Link structures of a website : represented by a di-graph, where V=>webpages ,and Edges=>links-between webpages
    + Social media : travel, biology, chip design, etc.
    + *Graph rewrite systems (transformation of graphs)*
    + *Graph databases* (complimentary to graph rewrite systems, which focuses on rule-based in-memory manipulation of graphs and graph databases: meant to be transaction safe, pesistent storage and querying of data
    + Linguistics and natural language processing, computational linguistics, semantic networks
    + Chemistry and physics
    + Social network analysis
    + Statistical physics
    + Computational Neuroscience
    + and many others ..

##References:
(1) https://web.stanford.edu/class/cs97si/06-basic-graph-algorithms.pdf
(2) The Algorithm Design Manual, Second Edition, Steven S. Skiena
(3) http://www.geeksforgeeks.org/graph-data-structure-and-algorithms/
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
