from TreeMap.RB_Tree import rb_tree


class TreeMap:
    # It accepts empty constructor, key, value pairs and dicitonary
    def __init__(self, key=None, value=None, dict=None) -> None:
        self.__tree = rb_tree()
        if(key is not None and value is not None):
            self.__tree.insert(key, value)
        elif(dict is not None):
            for k,v in dict.items():
                self.__tree.insert(k,v)
        
    # Print Map
    def __str__(self):
        s="{"
        order = self.__tree.tree_traversal()
        if len(order)>0:
            for i in order:
                s += "{}: {}, ".format(i.key,i.val)
            s = s[:-2]
        s +="}"
        return s

    # Insert
    def put(self, key, value):
        self.__tree.insert(key, value)
    
    # Insert dictionary
    def put_all(self, dict):
        for k,v in dict.items():
            self.__tree.insert(k,v)
    
    # Get a value from key
    def get(self, key):
        return self.__tree.search_tree(self.__tree.root, key).val
    
    # Returns list of keys
    def get_keys(self):
        order = self.__tree.tree_traversal()
        return [i.key for i in order]

    # Returns list of values
    def get_values(self):
        order = self.__tree.tree_traversal()
        return [i.val for i in order]

    # Remove an element
    def remove(self, key):
        self.__tree.delete(key)
    
    # Clear the entire tree
    def clear(self):
        self.__tree.clear_tree()
    
    # get size of map
    def size(self):
        return len(self.__tree.tree_traversal())
    
    # Checks if key is present
    def contains_key(self, key):
        n = self.__tree.search_tree(self.__tree.root, key)
        if n is None or n.key is None:
            return False
        else:
            return True

    # Checks if value is present
    def contains_value(self, value):
        order = self.__tree.tree_traversal()
        for i in order:
            if i.val == value:
                return True
        return False

    # Lowest Key
    def first_key(self):
        return self.__tree.first_ele().key
    
    # Lowest key but returns key and value
    def first_entry(self):
        ele =  self.__tree.first_ele().key
        return ele.key, ele.val
    
    # Get the element with lowest key and delete it
    def poll_first_entry(self):
        self.__tree.poll_first()

    # Get the largest key
    def last_key(self):
        return self.__tree.last_ele().key
    
    # Get the largest key value pair
    def last_entry(self):
        ele =  self.__tree.last_ele().key
        return ele.key, ele.val
    
    # Get the elment with the largest key and delete it
    def poll_last_entry(self):
        self.__tree.poll_last()
    

    def visaulize_tree(self):
        self.__tree.display_graph()
    

