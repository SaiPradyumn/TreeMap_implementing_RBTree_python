# Implementing TreeMap in Python along the principle of Red-Black Tree

Problem Description:

Storing a key-value pair in maps (Java / C++) and dictionaries (Python) does not guarantee the
sorted order of the input. Hence we additionally need to sort the data to get the desired output which
results in the average case time complexity (if the underlying implementation is Quick Sort) of O(n log n).
We aim to implement an algorithm to store the key-value pairs in sorted order (TreeMap) and achieve
the complexity of O (log n) while performing the operations on the data.

Implementation:

The implementation of the project is based on the principles of Red-Black Self-Balancing Trees.
Red-Black trees store the data in a sorted manner and maintain the balance. This ensures that
operations such as insert, delete and search can be done in O(log n). Which will be a faster alternative to
storing the data in a hashmap and then sorting it.
We will be developing an interface to store key-value pairs in the Red-Black tree and perform all
the required operations on the data. The interfacing library will work as a TreeMap.

Technical Approach:

1. Implement underlying algorithms for the self-balancing tree.
2. Develop an interface to access the functionality of the algorithm.
3. Testing the algorithm.
4. Complexity analysis for time and space with respect to the input size.
