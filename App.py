import os

def create_from_tree_file(tree_file_path):
    with open(tree_file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    path_stack = []
    last_indent = 0

    for line in lines:
        # Remove newline and trailing spaces
        clean_line = line.rstrip('\n')
        if not clean_line.strip():
            continue

        # Count indent depth using number of '│   ' or '    '
        stripped = clean_line.lstrip('│└├─ ')
        indent = (len(clean_line) - len(stripped)) // 4

        # Get name (file or folder)
        name = stripped.strip()
        is_dir = name.endswith('/')

        # Adjust the stack based on current indent
        path_stack = path_stack[:indent]
        path_stack.append(name.rstrip('/'))

        # Create the path
        current_path = os.path.join(*path_stack)
        if is_dir:
            os.makedirs(current_path, exist_ok=True)
        else:
            os.makedirs(os.path.dirname(current_path), exist_ok=True)
            open(current_path, 'w').close()

# Example usage:
create_from_tree_file("tree_input.txt")
