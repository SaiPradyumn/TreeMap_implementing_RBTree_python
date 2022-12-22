from TreeMap.RB_Tree import rb_tree


class TreeMap:
    # It accepts empty constructor, key, value pairs and dicitonary
    def __init__(self, key=None, value=None, dictionary=None) -> None:
        self.__tree = rb_tree()
        # If only one value is passed in the constructor, we assume it to be a dictionary
        if(type(key) is dict and value is None and dictionary is None):
            for k,v in key.items():
                self.__tree.insert(k,v)
            return
        # If two values are passed, we assume it to be a key value pair
        elif(key is not None and value is not None and dictionary is None):
            self.__tree.insert(key, value)
            return
        # If a dictionary is passed, we add all keys and values
        elif (dictionary is not None and key is None and value is None):
            for k,v in dictionary.items():
                self.__tree.insert(k,v)
            return
        elif (key is None and value is None and dictionary is None):
            return
        else:
            raise TypeError('Invalid arguments')
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
    
    def __repr__(self):
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
        if self.__tree.root is not None:
            return self.__tree.search_tree(self.__tree.root, key).val
        return None
    
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
        if self.__tree.root is not None:
            self.__tree.delete(key)
        return None
    # Clear the entire tree
    def clear(self):
        self.__tree.clear_tree()
    
    # get size of map
    def size(self):
        return len(self.__tree.tree_traversal())
    
    # Checks if key is present
    def contains_key(self, key):
        if self.__tree.root is not None:
            n = self.__tree.search_tree(self.__tree.root, key)
            if n is None or n.key is None:
                return False
            else:
                return True
        return False

    # Checks if value is present
    def contains_value(self, value):
        if self.__tree.root is not None:
            order = self.__tree.tree_traversal()
            for i in order:
                if i.val == value:
                    return True
            return False
        return False

    # Lowest Key
    def first_key(self):
        if self.__tree.root is not None:
            return self.__tree.first_ele().key
        return None
    
    # Lowest key but returns key and value
    def first_entry(self):
        if self.__tree.root is not None:
            ele =  self.__tree.first_ele()
            return {ele.key: ele.val}
        return None
    
    # Get the element with lowest key and delete it
    def poll_first_entry(self):
        if self.__tree.root is not None:
            self.__tree.poll_first()
        return None

    # Get the largest key
    def last_key(self):
        if self.__tree.root is not None:
            return self.__tree.last_ele().key
        return None
    
    # Get the largest key value pair
    def last_entry(self):
        if self.__tree.root is not None:
            ele =  self.__tree.last_ele()
            return {ele.key: ele.val}
        return None
    
    # Get the elment with the largest key and delete it
    def poll_last_entry(self):
        if self.__tree.root is not None:
            self.__tree.poll_last()
        return None

    def visaulize_tree(self):
        self.__tree.display_graph()
    

