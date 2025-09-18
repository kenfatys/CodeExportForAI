# File extensions to ignore
BLACKLIST_EXTENSIONS = {
    'txt', 'md', 'markdown', 'log', 'pdf', 'doc', 'docx', 'xls', 'xlsx',
    'png', 'jpg', 'jpeg', 'gif', 'bmp', 'ico', 'svg', 'webp',
    'mp3', 'mp4', 'avi', 'mov', 'wav',
    'zip', 'rar', '7z', 'tar', 'gz',
    'exe', 'dll', 'so', 'bin', 'o', 'obj',
    'pyc', 'pyo', 'pyd', 'class',
    'db', 'sqlite', 'mdb',
    'ini', 'cfg', 'conf', 'config', 'env'
}

# Directories to ignore
BLACKLIST_DIRS = {
    '__pycache__', '.git', '.vscode', '.vs', '.idea', 'node_modules', 
    'obj', 'bin', 'venv', 'env', 'virtualenv', 'dist', 'build', 'target', 'packages'
}

# Output format
OUTPUT_FORMAT = 'txt'  # or 'md'
OUTPUT_FILENAME = "output.txt"

# Default settings
MAX_FILE_SIZE_MB = 1

# Output behavior
CREATE_FILE = True          # Write output file
COPY_TO_CLIPBOARD = True   # Copy result to clipboard
# If both are False, a file will be created by default

# Filenames to ignore
BLACKLIST_FILENAMES = {
    '__init__.py', 'setup.py', 'requirements.txt'
}

# Filename filter mode: 'exact' = exact match, 'contains' = substring match
FILENAME_FILTER_MODE = 'exact'  # or 'contains'

INCLUDE_EMPTY_FILES = False
SHOW_PROGRESS = True