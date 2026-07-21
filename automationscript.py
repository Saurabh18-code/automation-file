import csv
import shutil
import os
import logging
from datetime import datetime

# Logging setup
if not os.path.exists("logs"):
    os.makedirs("logs")

log_file = f"logs/log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def setup_demo(base_dir):
    """Creates directory and sample files"""
    try:
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
            print(f"Created directory: {base_dir}")
            logging.info(f"Created directory: {base_dir}")

        input_file = os.path.join(base_dir, 'sample.txt')
        csv_file = os.path.join(base_dir, 'data.csv')

        # Write text file
        with open(input_file, 'w') as f:
            f.write("Hello, this is a sample text file for automation demo.")
            logging.info("Created sample.txt")

        # Write CSV file
        with open(csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Name', 'Status'])
            writer.writerow([1, 'Task_A', 'Completed'])
            writer.writerow([2, 'Task_B', 'Pending'])
            logging.info("Created data.csv")

        print("✅ Sample files created")

    except Exception as e:
        logging.error(f"Setup error: {e}")
        print(f"Error during setup: {e}")


def automate_files(base_dir):
    """File automation operations"""
    try:
        input_file = os.path.join(base_dir, 'sample.txt')
        csv_file = os.path.join(base_dir, 'data.csv')
        moved_file = os.path.join(base_dir, 'archived_sample.txt')

        # Read text file
        print("\n--- Reading File ---")
        with open(input_file, 'r') as f:
            content = f.read()
            print(content)
            logging.info("Read sample.txt")

        # Move + Rename
        print("\n--- Moving File ---")
        if os.path.exists(input_file):
            shutil.move(input_file, moved_file)
            print("File moved successfully")
            logging.info("Moved sample.txt to archived_sample.txt")

        # Read CSV
        print("\n--- Reading CSV ---")
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(f"{row['Name']} - {row['Status']}")
                logging.info(f"Processed {row['Name']}")

    except FileNotFoundError:
        logging.error("File not found")
        print("❌ File not found")

    except PermissionError:
        logging.error("Permission denied")
        print("❌ Permission denied")

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"Error: {e}")

    finally:
        print("\n✅ Operation completed")

def main():
    print("📁 FILE AUTOMATION DEMO")

    base_dir = input("Enter directory name (default: file_demo): ").strip()
    if not base_dir:
        base_dir = "file_demo"

    while True:
        print("\nMenu:")
        print("1. Setup demo files")
        print("2. Run automation")
        print("3. Show files")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            setup_demo(base_dir)

        elif choice == "2":
            automate_files(base_dir)

        elif choice == "3":
            if os.path.exists(base_dir):
                print(os.listdir(base_dir))
            else:
                print("Directory not found")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main(); input("Press Enter to exit...")
                                                                                                  