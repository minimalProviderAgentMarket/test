# Fixes #17
chars = 'Hello' * 200000  # This will create 1 million characters (5 chars * 200000)
print(chars)
print(f"\nTotal characters printed: {len(chars)}")