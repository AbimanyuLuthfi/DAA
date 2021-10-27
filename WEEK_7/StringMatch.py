def string_match(string, sub_str):
    # Brute force string matching
    for i in range(len(string)-len(sub_str)+1):
        index = i # index Point to the 1 Three characters to be compared
        for j in range(len(sub_str)):
            if string[index] == sub_str[j]:
                index += 1
            else:
                break
            if index-i == len(sub_str):
                return i
    return -1
    
if __name__ == "__main__":
    print(string_match("adbcbdc", "bdc"))
