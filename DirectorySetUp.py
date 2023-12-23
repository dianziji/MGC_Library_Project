import os

# Define the directory structure
project_structure = {
    "backend/app": ["__init__.py", "main.py", "models.py", "schemas.py", "crud.py", "dependencies.py"],
    "backend/app/routers": ["__init__.py", "books.py", "users.py", "borrowing_records.py"],
    "backend/tests": ["test_api.py"],
    "backend": ["requirements.txt"]
}

def create_project_structure(base_path, structure):
    """ Create directories and files based on the provided structure. """
    for path, files in structure.items():
        # Create directory
        dir_path = os.path.join(base_path, path)
        os.makedirs(dir_path, exist_ok=True)

        # Create files in the directory
        for file in files:
            file_path = os.path.join(dir_path, file)
            with open(file_path, 'w') as f:
                f.write('') # Creates an empty file

# Set the base path to your desired location on Windows
base_path = 'D:\\CS\\MGC_Library_Project'

# Create the project structure
create_project_structure(base_path, project_structure)

print(f"Project structure created successfully at {base_path}")
