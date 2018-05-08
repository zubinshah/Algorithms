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
