"""
Database Export/Import Utility
This script helps you share your database with collaborators.

Usage:
  python export_db.py export    # Creates a backup of your database
  python export_db.py import    # Imports a database backup
"""

import os
import shutil
from datetime import datetime

# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, 'sql_app.db')
EXPORT_DIR = os.path.join(BASE_DIR, 'db_exports')

def export_database():
    """Export the current database to a shareable file"""
    if not os.path.exists(DB_FILE):
        print("[ERROR] Database file not found!")
        print(f"   Looking for: {DB_FILE}")
        return
    
    # Create exports directory if it doesn't exist
    os.makedirs(EXPORT_DIR, exist_ok=True)
    
    # Create timestamped backup
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    export_file = os.path.join(EXPORT_DIR, f'sql_app_backup_{timestamp}.db')
    
    # Copy the database
    shutil.copy2(DB_FILE, export_file)
    
    print("[SUCCESS] Database exported successfully!")
    print(f"Location: {export_file}")
    print("\nShare this file with your collaborator.")
    print("   They should place it in their Backend folder and rename it to 'sql_app.db'")

def import_database():
    """Import a database file"""
    print("[IMPORT] Looking for database files to import...")
    
    if not os.path.exists(EXPORT_DIR):
        print("[ERROR] No exports folder found!")
        print("   Please place the database file you received in: Backend/db_exports/")
        return
    
    # List all .db files in exports directory
    db_files = [f for f in os.listdir(EXPORT_DIR) if f.endswith('.db')]
    
    if not db_files:
        print("[ERROR] No database files found in db_exports folder!")
        print("   Please place the .db file you received there first.")
        return
    
    print("\nAvailable database files:")
    for i, filename in enumerate(db_files, 1):
        print(f"  {i}. {filename}")
    
    # Get user choice
    try:
        choice = int(input("\nEnter the number of the file to import (or 0 to cancel): "))
        if choice == 0:
            print("Import cancelled.")
            return
        if choice < 1 or choice > len(db_files):
            print("[ERROR] Invalid choice!")
            return
        
        selected_file = os.path.join(EXPORT_DIR, db_files[choice - 1])
        
        # Backup existing database if it exists
        if os.path.exists(DB_FILE):
            backup_file = os.path.join(BASE_DIR, f'sql_app_old_{datetime.now().strftime("%Y%m%d_%H%M%S")}.db')
            shutil.copy2(DB_FILE, backup_file)
            print(f"[BACKUP] Backed up existing database to: {backup_file}")
        
        # Import the new database
        shutil.copy2(selected_file, DB_FILE)
        print("[SUCCESS] Database imported successfully!")
        print("   You can now run the backend and login with the imported accounts.")
        
    except ValueError:
        print("[ERROR] Invalid input!")
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python export_db.py export    # Export your database")
        print("  python export_db.py import    # Import a database")
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == "export":
        export_database()
    elif command == "import":
        import_database()
    else:
        print(f"[ERROR] Unknown command: {command}")
        print("Use 'export' or 'import'")
