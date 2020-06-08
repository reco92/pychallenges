
class Node(object):
    def __init__(self, data):
        self.data = data
        self.leafs = list()
    
    def insert_blank_leaf(self):
        self.leafs.append(Node(''))

    def check_match(self, previus, to_check):
        word = previus + self.data
        if self.data == '':
            return False

        if word in to_check or to_check in word:
            return True

        return False

    def insert(self, data, previous):

        if self.data == '':
            self.data = data
            self.leafs.append(Node(''))
            return True

        word = previous + self.data
        if word == data:
            return True
        if word in data:
            for leaf in self.leafs:
                if leaf.check_match(word, data):
                    return leaf.insert(data, word)
            #add diference
            diff = data[len(word):]
            new_node = Node(diff)
            new_node.insert_blank_leaf()
            self.leafs.append(new_node)

            return True
        elif data in word:
            diff = word[len(data):]
            preserve_node = Node(diff)
            preserve_node.leafs = self.leafs.copy()
            self.data = word[len(previous):len(data)]
            self.leafs = list()
            self.insert_blank_leaf()
            self.leafs.append(preserve_node)

            return True

        return False

    def print(self, previous=''):
        if self.data == '':
            print (previous + self.data)

        for leaf in self.leafs:
            leaf.print(previous+self.data)
                    
class Patricia(object):

    def __init__(self):
        self.root = Node('')

    def insert(self, word):
        if not self.root.insert(word,''):
            #check characters
            root_data = self.root.data
            idx = 0
            while root_data[idx] == word[idx]:
                idx += 1
            root_val = word[:idx]
            old_diff = root_data[idx:]
            new_diff = word[idx:]
            new_root = Node(root_val)
            node_diff = Node(old_diff)
            new_node = Node(new_diff)

            node_diff.leafs = self.root.leafs.copy()
            new_node.insert_blank_leaf()
            new_root.leafs.append(node_diff)
            new_root.leafs.append(new_node)
            self.root = new_root

    
    def print_words(self):
        self.root.print()


def main():
    pato = Patricia()
    pato.insert('roma')
    pato.insert('romano')
    pato.insert('roman')
    pato.insert('rosman')
    pato.insert('amigo')

    pato.print_words()

if __name__ == "__main__":
    main()