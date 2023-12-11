def compare_lines(line1, lines):
    count = 0
    for line2 in lines:
        for char1, char2 in zip(line1, line2):
            if char1 == char2:
                count += 1
    similarity = count / (len(line1) * len(lines))
    return similarity

def process_file(file_path, output_file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    result = []
    i = 0
    while i < len(lines):
        line1 = lines[i].strip()
        similar_lines = [line1]
        for j in range(i+1, min(i+2, len(lines))):
            line2 = lines[j].strip()
            similarity = compare_lines(line1, [line2])
            if similarity >= 0.38:
                similar_lines.append(line2)
            else:
                break
        
        result.append(' '.join(similar_lines))
        i += len(similar_lines)
    
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write('\n'.join(result))

file_path = input("Enter the path of the input file: ")
output_file_path = input("Enter the path of the output file: ")
process_file(file_path, output_file_path)
