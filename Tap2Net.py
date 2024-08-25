import random
import time
import psutil
import os


# Define ANSI color codes
class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def generate_random_key(length):
    """Generate a random encryption key."""
    key = ''.join(random.choices('0123456789ABCDEF', k=length))
    return key


def encrypt_data(data, key):
    """Encrypt data using a provided key."""
    encrypted_data = ''
    total_data = len(data)
    processed_data = 0
    for char in data:
        # Introduz variação aleatória na velocidade de processamento
        time.sleep(random.uniform(0.05, 0.2))
        encrypted_char = hex(ord(char) ^ int(key, 16))[2:].zfill(2).upper()
        encrypted_data += encrypted_char
        processed_data += 1
        # Print progress during encryption
        print_progress(processed_data, total_data)
    return encrypted_data


def print_progress(processed, total, iteration, format):
    """Print progress bar."""
    bar_length = 30
    progress = processed / total
    num_blocks = int(bar_length * progress)
    bar = colors.GREEN + '[' + colors.END + colors.BLUE + '█' * num_blocks + ' ' * (
            bar_length - num_blocks) + colors.END + colors.GREEN + ']' + colors.END
    print(f"\rEncrypting data ({format}) - Iteration {iteration}: {bar} {processed}/{total} bytes processed", end="",
          flush=True)


def get_system_info():
    """Get random system information."""
    cpu_usage = psutil.cpu_percent()
    mem_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    return f"CPU: {cpu_usage}% | Memory: {mem_usage}% | Disk: {disk_usage}%"


def get_random_message():
    """Generate a random message."""
    messages = [
        "Processing your data...",
        "Please wait while we secure your information...",
        "Encrypting your data for safe transmission...",
        "Data security protocols initiated...",
        "Securing your information with military-grade encryption..."
    ]
    return random.choice(messages)


def print_cpu_usage():
    """Print CPU usage."""
    cpu_usage = psutil.cpu_percent()
    print(f"CPU Usage: {cpu_usage}%")


def print_memory_usage():
    """Print memory usage."""
    mem_usage = psutil.virtual_memory().percent
    print(f"Memory Usage: {mem_usage}%")


def print_disk_usage():
    """Print disk usage."""
    disk_usage = psutil.disk_usage('/').percent
    print(f"Disk Usage: {disk_usage}%")


def clear_terminal():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    for i in range(5):
        clear_terminal()
        print(colors.BOLD + colors.YELLOW + "Tap2Net Data Encryption" + colors.END)
        print(colors.BOLD + colors.GREEN + "------------------------------------" + colors.END)

        # Prompt the user for the title of the data
        data_title = input("Enter a title for the data: ")

        # Prompt the user to input the data to process
        data = input("Enter data to process: ")

        # Prompt the user to input the data to process
        data = input("Enter data: ")

        # Generate a random 16-character encryption key
        encryption_key = generate_random_key(16)

        for a in range(3):
            # Simulate data processing
            print("Processing data... ", end="", flush=True)
            for _ in range(20):
                print(colors.BLUE + "█" + colors.END, end="", flush=True)
                time.sleep(0.2)
            print("\n")

        # Simulate system information display
        print(colors.YELLOW + "System Information: " + get_system_info() + colors.END)
        print()
        print_cpu_usage()
        print_memory_usage()
        print_disk_usage()
        print()

        for a in range(3):
            # Simulate random messages during processing
            print(colors.YELLOW + "Random Message: " + get_random_message() + colors.END)
            print()

        # Prompt the user to input the data to process
        data = input("Enter data: ")

        for a in range(5):
            # Simulate CPU and memory usage during encryption
            print(colors.GREEN + "Encrypting data..." + colors.END)
            for j in range(1, 11):
                print_progress(j+a, 5+a, i + 1+a, f"Format {j+a}")
                time.sleep(0.5)
            print("\n" + colors.GREEN + "Data encryption complete." + colors.END)

        # Display encrypted data
        print("Encrypted Data:", colors.BOLD + colors.RED + "Encrypted data here" + colors.END)

        # Simulate countdown before completion
        print("\n" + colors.YELLOW + "Finalizing process..." + colors.END)
        for k in range(5, 0, -1):
            print(f"{k}...", end="", flush=True)
            time.sleep(1)
        print("\n" + colors.BOLD + colors.GREEN + "Process completed successfully!" + colors.END)
        print(colors.BOLD + colors.GREEN + "------------------------------------" + colors.END)
        print(colors.BOLD + colors.YELLOW + "Tap2Net" + colors.END)
        time.sleep(2)


if __name__ == "__main__":
    main()


