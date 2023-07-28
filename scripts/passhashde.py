import hashlib
from dotenv import load_dotenv

load_dotenv()
# The password you've extracted
hashed_password = os.getenv(hashed_password)

# The original password you suspect
original_password = "password"

# Create a new md5 hash object
md5_hash = hashlib.md5()

# Hash the original password
md5_hash.update(original_password.encode('utf-8'))

# Get the hexadecimal representation of the hash
hashed_output = md5_hash.hexdigest()
print(hashed_output)
# Check if the hashed output matches the extracted password
if hashed_output == hashed_password:
    print("The passwords match!")
else:
    print("The passwords do not match.")
