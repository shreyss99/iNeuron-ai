def get_encoded_str(root, data):

    ''' Return encoded string of original data '''
    
    codes = get_codes(root)
    compressed_data = []
    for d in data:
        compressed_data.append(codes[d])
    return ''.join(compressed_data)
    
    
def pad_encoded_str(encoded_str):

    ''' Return encoded string with padding zero
    for storing in file in bytes '''
    
    extra_zero = 8 - len(encoded_str) % 8
    padded_encoded_str = '0' * extra_zero + encoded_str
    extra_zero_info = '{0:08b}'.format(extra_zero)
    padded_encoded_str = extra_zero_info + padded_encoded_str
    return padded_encoded_str