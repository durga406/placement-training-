import heapq
import os
import pickle
class HuffmanNode:
    def __init__(self, byte, freq):
        self.byte = byte
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq
def build_frequency_table(data: bytes) -> dict:
    freq_table = {}
    for byte in data:
        freq_table[byte] = freq_table.get(byte, 0) + 1
    return freq_table
def build_huffman_tree(freq_table: dict) -> HuffmanNode:
    heap = [HuffmanNode(byte, freq) for byte, freq in freq_table.items()]
    heapq.heapify(heap)
    if len(heap) == 1:
        node = heapq.heappop(heap)
        root = HuffmanNode(None, node.freq)
        root.left = node
        return root
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)
    return heap[0]
def generate_codes(root: HuffmanNode, current_code: str, codes: dict):
    if root is None:
        return
    if root.byte is not None:
        codes[root.byte] = current_code
        return
    generate_codes(root.left, current_code + "0", codes)
    generate_codes(root.right, current_code + "1", codes)
def pad_encoded_text(encoded_text: str) -> bytes:
    extra_padding = 8 - (len(encoded_text) % 8)
    for _ in range(extra_padding):
        encoded_text += "0"
    padding_info = f"{extra_padding:08b}"
    encoded_text = padding_info + encoded_text
    byte_array = bytearray()
    for i in range(0, len(encoded_text), 8):
        byte = encoded_text[i:i+8]
        byte_array.append(int(byte, 2))
    return bytes(byte_array)
def remove_padding(padded_encoded_text: bytes) -> str:
    bit_string = ""
    for byte in padded_encoded_text:
        bit_string += f"{byte:08b}"
    padding_info = bit_string[:8]
    extra_padding = int(padding_info, 2)
    bit_string = bit_string[8:]
    encoded_text = bit_string[:-extra_padding] if extra_padding > 0 else bit_string
    return encoded_text
def compress_file(input_path: str, output_path: str):
    if not os.path.exists(input_path):
        print(f"Error: File '{input_path}' not found.")
        return
    with open(input_path, 'rb') as f:
        data = f.read()
    if len(data) == 0:
        print("Warning: Input file is empty.")
        with open(output_path, 'wb') as f:
            pickle.dump(({}, bytes()), f)
        return
    freq_table = build_frequency_table(data)
    root = build_huffman_tree(freq_table)
    codes = {}
    generate_codes(root, "", codes)
    encoded_bits = "".join(codes[byte] for byte in data)
    compressed_data = pad_encoded_text(encoded_bits)
    with open(output_path, 'wb') as f:
        pickle.dump((freq_table, compressed_data), f)
    print(f"Successfully compressed '{input_path}' to '{output_path}'")
    print(f"Original Size: {len(data)} bytes | Compressed Size: {os.path.getsize(output_path)} bytes")
def decompress_file(input_path: str, output_path: str):
    if not os.path.exists(input_path):
        print(f"Error: File '{input_path}' not found.")
        return
    with open(input_path, 'rb') as f:
        freq_table, compressed_data = pickle.load(f)
    if not freq_table:
        with open(output_path, 'wb') as f:
            f.write(b"")
        print(f"Successfully decompressed empty file to '{output_path}'")
        return
    root = build_huffman_tree(freq_table)
    encoded_bits = remove_padding(compressed_data)
    decompressed_bytes = bytearray()
    current_node = root
    for bit in encoded_bits:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.byte is not None:
            decompressed_bytes.append(current_node.byte)
            current_node = root  
    with open(output_path, 'wb') as f:
        f.write(decompressed_bytes)
    print(f"Successfully decompressed '{input_path}' to '{output_path}'")
if __name__ == '__main__':
    sample_text = "huffman coding algorithm is an elegant tool for lossless file compression" * 100
    with open("example.txt", "w") as f:
        f.write(sample_text)
    compress_file("example.txt", "example.huff")
  decompress_file("example.huff", "restored_example.txt")
