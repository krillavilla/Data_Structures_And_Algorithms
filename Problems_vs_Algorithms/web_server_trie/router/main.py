# The RouteTrieNode will be used to hold the handler for each path and its children
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with handler and an empty dictionary for children
        self.handler = handler
        self.children = {}

# The RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=None):
        # Initialize the trie with a root node and a handler
        self.root = RouteTrieNode(handler)

    def insert(self, path_parts, handler):
        # Insert the handler for the path into the trie
        node = self.root
        for part in path_parts:
            if part not in node.children:
                node.children[part] = RouteTrieNode()
            node = node.children[part]
        node.handler = handler

    def find(self, path_parts):
        # Find and return the handler for a path in the trie
        # Return None if path is not found
        node = self.root
        for part in path_parts:
            if part in node.children:
                node = node.children[part]
            else:
                return None
        return node.handler

# The Router class will wrap the Trie and handle the actual routing
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes and initialize it with a root handler
        # Also hold a handler for handling not found paths
        self.trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # Split the path and pass the parts as a list to the RouteTrie
        path_parts = self.split_path(path)
        self.trie.insert(path_parts, handler)

    def lookup(self, path):
        # Lookup path (by parts) and return the associated handler
        # Return the "not found" handler if path is not found
        path_parts = self.split_path(path)
        handler = self.trie.find(path_parts)
        if handler is None:
            return self.not_found_handler
        else:
            return handler

    def split_path(self, path):
        # Split the path into parts for both the add_handler and lookup methods
        return [part for part in path.split('/') if part]

# Create the router and add a route
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")

# Some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler'
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler'
print(router.lookup("/home/about/me"))  # should print 'not found handler'