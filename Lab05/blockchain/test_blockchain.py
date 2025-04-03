from blockchain import Blockchain

# Khởi tạo blockchain
my_blockchain = Blockchain()

# Thêm giao dịch
my_blockchain.add_transaction('Alice', 'Bob', 10)

# Lấy block trước đó
previous_block = my_blockchain.get_previous_block()
previous_proof = previous_block.proof

# Tìm proof mới
new_proof = my_blockchain.proof_of_work(previous_proof)

# Tạo block mới
previous_hash = previous_block.hash
new_block = my_blockchain.create_block(new_proof, previous_hash)

print("Block mới đã được thêm vào blockchain:")
print(new_block.__dict__)

my_blockchain.add_transaction('Bob', 'Charlie',5)
my_blockchain.add_transaction("Charlie", 'Alice',3)

for block in my_blockchain.chain:
    print(f"Block #{block.index}")
    print("Timestamp:", block.timestamp)
    print("Transactions:", block.transactions)
    print("Proof:", block.proof)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)
    print("-------------")

print("Is Blockchain Valid:", my_blockchain.is_chain_valid(my_blockchain.chain))