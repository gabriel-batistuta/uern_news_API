import os

def generate_tree_markdown(directory, prefix="", ignore_list=None):
    if ignore_list is None:
        ignore_list = []
    markdown_content = ""
    items = sorted(os.listdir(directory))
    items = [item for item in items if item not in ignore_list]
    for index, item in enumerate(items):
        path = os.path.join(directory, item)
        connector = "├── " if index < len(items) - 1 else "└── "
        markdown_content += f"{prefix}{connector}{item}\n"
        if os.path.isdir(path):
            extension = "│   " if index < len(items) - 1 else "    "
            markdown_content += generate_tree_markdown(path, prefix + extension, ignore_list)
    return markdown_content

# Diretório que você deseja listar
directory = 'public'

# Lista de arquivos e pastas a serem ignorados
ignore_list = ['LICENSE', 'README.md', 'sub-script', '__pycache__', 'venv']

# Gera o conteúdo markdown
markdown_content = f"""# UERN NEWS DOCS

Essa parte do repositório serve pra implementação do código do site com a documentação da API
\n\n# Estrutura de Arquivos em {directory}\n\n"""
markdown_content += "```\n"
markdown_content += generate_tree_markdown(directory, ignore_list=ignore_list)
markdown_content += "```\n"

# Escreve o conteúdo no arquivo markdown
with open('./public/README.md', 'w') as f:
    f.write(markdown_content)

print("README.md generated sucessfully")
