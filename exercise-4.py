def chunking_by(numbers, chunck):
    if chunck <= 0 or not isinstance(chunck, int):
        return "chunk size need to be a positive integer"
    
    chunks = []
    for i in range(0,len(numbers), chunck):
        # slice the original list to get the wanted chunk
        divide = numbers[i:i + chunck]
        # add the value to the list
        chunks.append(divide)

    return chunks