from collections import Counter
import heapq


class HeapNode:
    def __init__(self, data, freq) -> None:
        self.data = data
        self.freq = freq
        self.right: HeapNode | None = None
        self.left: HeapNode | None = None

    def __lt__(self, other) -> bool:
        return self.freq < other.freq


class Huffman:
    def __init__(self, message: str) -> None:
        self.frequencies = Counter(message)
        self.codes = {}

    def generate_codes(self, node: HeapNode, st):
        if node is None:
            return
        if node.data != internal_data:
            self.codes[node.data] = st
        self.generate_codes(node.left, f"{st}0")
        self.generate_codes(node.right, f"{st}1")


internal_data = None
pq: list[HeapNode] = []
msg = Huffman("internet")
for k, v in msg.frequencies.items():
    top = HeapNode(k, v)
    heapq.heappush(pq, top)

while len(pq) > 1:
    left_node = heapq.heappop(pq)
    right_node = heapq.heappop(pq)
    top = HeapNode(internal_data, left_node.freq + right_node.freq)
    if left_node and right_node:
        top.left = left_node
        top.right = right_node
    heapq.heappush(pq, top)
msg.generate_codes(pq[0], "")
print(msg.codes)
