class Passenger:
    def __init__(self, name, ticket_number):
        self.name = name
        self.ticket_number = ticket_number  # Acts as the key for BST

    def __repr__(self):
        return f"<Passenger: {self.name}, Ticket: {self.ticket_number}>"


class BSTNode:
    def __init__(self, passenger):
        self.passenger = passenger
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, passenger):
        if self.root is None:
            self.root = BSTNode(passenger)
        else:
            self._insert_recursive(self.root, passenger)

    def _insert_recursive(self, node, passenger):
        if passenger.ticket_number < node.passenger.ticket_number:
            if node.left is None:
                node.left = BSTNode(passenger)
            else:
                self._insert_recursive(node.left, passenger)
        elif passenger.ticket_number > node.passenger.ticket_number:
            if node.right is None:
                node.right = BSTNode(passenger)
            else:
                self._insert_recursive(node.right, passenger)
        else:
            raise ValueError("Duplicate ticket number not allowed.")

    def search(self, ticket_number):
        return self._search_recursive(self.root, ticket_number)

    def _search_recursive(self, node, ticket_number):
        if node is None:
            return None
        if ticket_number == node.passenger.ticket_number:
            return node.passenger
        elif ticket_number < node.passenger.ticket_number:
            return self._search_recursive(node.left, ticket_number)
        else:
            return self._search_recursive(node.right, ticket_number)

    def delete(self, ticket_number):
        self.root = self._delete_recursive(self.root, ticket_number)

    def _delete_recursive(self, node, ticket_number):
        if node is None:
            return None

        if ticket_number < node.passenger.ticket_number:
            node.left = self._delete_recursive(node.left, ticket_number)
        elif ticket_number > node.passenger.ticket_number:
            node.right = self._delete_recursive(node.right, ticket_number)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            min_larger_node = self._get_min(node.right)
            node.passenger = min_larger_node.passenger
            node.right = self._delete_recursive(node.right, min_larger_node.passenger.ticket_number)
        return node

    def _get_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.passenger)
            self._inorder_recursive(node.right, result)
