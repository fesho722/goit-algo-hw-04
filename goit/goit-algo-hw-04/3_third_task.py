import sys
import os
from colorama import init, Fore, Style

init(autoreset=True)

def visualize_directory_structure(directory):

    if not os.path.isdir(directory):
        print(Fore.RED + "Директорія не знайдена.")
        return
    
    print(Fore.GREEN + f"Структура директорії: {directory}")
    print(Fore.BLUE + "-" * 40)
    for root, dirs, files in os.walk(directory):
        level = root.replace(directory, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(Fore.YELLOW + f"{indent}{os.path.basename(root)}/")
        sub_indent = ' ' * 4 * (level + 1)
        for file in files:
            print(Fore.WHITE + f"{sub_indent}{file}")
        print(Fore.BLUE + "-" * 40)


    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print(Fore.RED + "Використання: python script.py <шлях до директорії>")
        else:
            directory_path = sys.argv[1]
            visualize_directory_structure(directory_path)