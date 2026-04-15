from collections import Counter
import heapq

INTERNAL_CHAR = chr(0)


class HeapNode:
    def __init__(self, char, freq) -> None:
        self.data = char
        self.freq = freq
        self.right = None
        self.left = None

    def __lt__(self, other: HeapNode):
        return self.freq < other.freq


class Huffman:
    def __init__(self, msg) -> None:
        self.codes = dict()
        self.msg = msg
        # get freqs
        self.freqHash = Counter(msg)
        self.minHeap = []
        # create the minHeap(priorty queue)
        for k, v in self.freqHash.items():
            node = HeapNode(k, v)
            heapq.heappush(self.minHeap, node)
        # create the heap(binary tree for huffman codes)
        while len(self.minHeap) > 1:
            left_node = heapq.heappop(self.minHeap)
            right_node = heapq.heappop(self.minHeap)
            top = HeapNode(INTERNAL_CHAR, left_node.freq + right_node.freq)
            top.left = left_node
            top.right = right_node
            heapq.heappush(self.minHeap, top)
        # generate codes of the message
        self.generate_codes(self.minHeap[0], "")

    def generate_codes(self, node: HeapNode, code):
        if node is None:
            return
        if node.data != INTERNAL_CHAR:
            self.codes[node.data] = code
        self.generate_codes(node.left, code + "0")
        self.generate_codes(node.right, code + "1")


msg = "internet"
huff = Huffman(msg)
print(huff.codes)
