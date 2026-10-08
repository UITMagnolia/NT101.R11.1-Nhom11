from dependencies import install_dependencies
install_dependencies(["pycryptodome"])

from Crypto.Cipher import DES


def des_ecb_encrypt(key: str, plaintext: str) -> str:
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(plaintext)

def text_to_bytes(text: str) -> bytes:
    return text.encode("utf-8")

def avalanche_test(block1: bytes, block2: bytes) -> int:
    if len(block1) != len(block2):
        raise ValueError("Blocks must have the same length")

    num1 = int.from_bytes(block1, "big")
    num2 = int.from_bytes(block2, "big")

    return (num1 ^ num2).bit_count()

def main(key: str = None):
    if not key:
        print("No key provided, using default key: 24521922")
        key = text_to_bytes("24521922")
    else:
        key = text_to_bytes(key)

    p1 = text_to_bytes("STAYHOME")
    p2 = text_to_bytes("STAYHOMA")

    c1 = des_ecb_encrypt(key, p1)
    c2 = des_ecb_encrypt(key, p2)

    distance = avalanche_test(c1, c2)
    percentage = distance / (len(c1) * 8) * 100

    print("========== Task 2.3: Avalanche Effect ==========\n")
    print("Key:", key.decode())
    print("Plaintext 1:", p1.decode())
    print("Plaintext 2:", p2.decode())

    print("Ciphertext 1 (Hex):", c1.hex())
    print("Ciphertext 2 (Hex):", c2.hex())

    print("Ciphertext 1 (Binary):", format(int.from_bytes(c1, "big"), "064b"))
    print("Ciphertext 2 (Binary):", format(int.from_bytes(c2, "big"), "064b"))

    print("Hamming Distance (number of different bits):", distance)
    print(f"Percentage: {percentage:.2f}%\n")


if __name__ == "__main__":
    key = input("Enter a key (24521922 / 24521923): ")
    main(key)