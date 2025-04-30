class TreeNode:
    def __init__(self, value, data = None):
        self.value = value
        self.data= data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
        return self

    def remove_child(self, child_node):
        self.children = [child for child in self.children if child != child_node]
        return self
    
    def print_tree(self, level=0):
        # Print current node with proper indentation
        print('    ' * level + '|-- ' + str(self.value))
        
        # Recursively print all children with increased indentation
        for child in self.children:
            child.print_tree(level + 1)
        
    def build_electronics_shop(self):
        # Build the electronics shop tree
        # Create the root node
        root = TreeNode("Electronics Shop")

        # Create the category nodes
        laptops = TreeNode("Laptops")
        smartphones = TreeNode("Smartphones")
        tablets = TreeNode("Tablets")
        headphones = TreeNode("Headphones")
        speakers = TreeNode("Speakers")
        
        laptop1 = TreeNode("Laptop 1")
        laptop2 = TreeNode("Laptop 2")
        laptop3 = TreeNode("Laptop 3")

        smartphone1 = TreeNode("Smartphone 1")
        smartphone2 = TreeNode("Smartphone 2")

        tablet1 = TreeNode("Tablet 1")
        tablet2 = TreeNode("Tablet 2")

        headphone1 = TreeNode("Headphone 1")
        headphone2 = TreeNode("Headphone 2") 

        speaker1 = TreeNode("Speaker 1")
        speaker2 = TreeNode("Speaker 2")

        # Add children to the root node
        root.add_child(laptops)
        root.add_child(smartphones) 
        root.add_child(tablets)
        root.add_child(headphones)
        root.add_child(speakers)

        # Add children to the laptops node
        laptops.add_child(laptop1)  
        laptops.add_child(laptop2)
        laptops.add_child(laptop3)

        # Add children to the smartphones node
        smartphones.add_child(smartphone1)
        smartphones.add_child(smartphone2)  

        # Add children to the tablets node
        tablets.add_child(tablet1)
        tablets.add_child(tablet2)

        # Add children to the headphones node   
        headphones.add_child(headphone1)
        headphones.add_child(headphone2)

        # Add children to the speakers node
        speakers.add_child(speaker1)
        speakers.add_child(speaker2)    

        return root

if __name__ == "__main__":
    # Create and print the electronics shop tree
    root = TreeNode("Root").build_electronics_shop()
    root.print_tree()
        
        
        