import hashlib
import os

# Define the files to be used
FILE_TO_CHECK = 'important.txt'
HASH_FILE = 'original_hash.txt'

def get_file_hash(filepath):
    """
    Generates a SHA256 hash for a given file.
    """
    # Create a SHA256 hash object
    sha256_hash = hashlib.sha256()
    
    # Read the file in binary mode
    with open(filepath, "rb") as f:
        # Read the file in chunks to handle large files efficiently (4KB at a time)
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
            
    return sha256_hash.hexdigest()

def main():
    # 1. Check if the important file exists
    if not os.path.exists(FILE_TO_CHECK):
        raise Exception(f"CRITICAL ERROR: '{FILE_TO_CHECK}' not found!")

    # 2. Generate the SHA256 hash for the current state of the file
    current_hash = get_file_hash(FILE_TO_CHECK)

    # 3. Check if we have an original hash to compare against
    if not os.path.exists(HASH_FILE):
        # We DO NOT auto-generate the trusted hash. It must be created manually.
        raise Exception(f"CRITICAL ERROR: Trusted hash file '{HASH_FILE}' is missing! Cannot verify integrity.")

    # 4. Read the original hash from the file
    with open(HASH_FILE, 'r') as f:
        original_hash = f.read().strip()

    # 5. Compare the current hash with the original hash
    if current_hash == original_hash:
        print("Integrity maintained")
    else:
        # Raise an exception to fail the CI/CD pipeline permanently
        raise Exception("WARNING: Integrity mismatch detected. The file has been modified!")

if __name__ == "__main__":
    main()
