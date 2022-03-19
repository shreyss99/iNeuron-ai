def get_encoded_str(root, data):

    ''' Return encoded string of original data '''
    
    codes = get_codes(root)
    compressed_data = []
    for d in data:
        compressed_data.append(codes[d])
    return ''.join(compressed_data)