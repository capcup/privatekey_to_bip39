from mnemonic import Mnemonic

def is_valid_hex_private_key(hex_key: str) -> bool:
    if len(hex_key) != 64:
        return False
    try:
        int(hex_key, 16)
        return True
    except ValueError:
        return False

def convert_to_mnemonic(hex_key: str) -> str:
    mnemo = Mnemonic("english")
    entropy_bytes = bytes.fromhex(hex_key)
    return mnemo.to_mnemonic(entropy_bytes)

def main():
    hex_key = input("Gib deinen 64-stelligen Private Key als Hex-String ein:\n> ").strip().lower()

    if not is_valid_hex_private_key(hex_key):
        print("❌ Ungültiger Private Key! Muss genau 64 Hex-Zeichen enthalten (256 Bit).")
        return

    mnemonic = convert_to_mnemonic(hex_key)
    print("\n✅ Dein BIP39-Mnemonic (24 Wörter):")
    print(mnemonic)

if __name__ == "__main__":
    main()
