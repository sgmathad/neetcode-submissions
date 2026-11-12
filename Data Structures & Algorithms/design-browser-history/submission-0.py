class Node:
    def __init__(self, val: str):
        self.val = val
        self.next = None
        self.prev = None
    
class BrowserHistory:

    def __init__(self, homepage: str):
        self.first =  Node(homepage)

    def visit(self, url: str) -> None:
        node = Node(url)
        self.first.next = node
        node.prev = self.first
        self.first = node

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if not self.first.prev:
                break
            self.first = self.first.prev
        return self.first.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if not self.first.next:
                break
            self.first = self.first.next
        return self.first.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)