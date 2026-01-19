"""
Backend Diagnostic Script
Run this script to check if all dependencies and configurations are correct.
"""

import sys
import importlib

def check_python_version():
    """Check if Python version is compatible"""
    print("=" * 50)
    print("PYTHON VERSION CHECK")
    print("=" * 50)
    version = sys.version_info
    print(f"Python Version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("[X] ERROR: Python 3.8 or higher is required!")
        return False
    else:
        print("[OK] Python version is compatible")
        return True

def check_dependencies():
    """Check if all required packages are installed"""
    print("\n" + "=" * 50)
    print("DEPENDENCY CHECK")
    print("=" * 50)
    
    required_packages = {
        'fastapi': 'FastAPI',
        'uvicorn': 'Uvicorn',
        'sqlalchemy': 'SQLAlchemy',
        'passlib': 'Passlib',
        'jose': 'Python-JOSE',
        'pydantic': 'Pydantic',
        'email_validator': 'Email Validator'
    }
    
    all_installed = True
    
    for package, name in required_packages.items():
        try:
            importlib.import_module(package)
            print(f"[OK] {name} is installed")
        except ImportError:
            print(f"[X] {name} is NOT installed")
            all_installed = False
    
    return all_installed

def check_files():
    """Check if all required files exist"""
    print("\n" + "=" * 50)
    print("FILE CHECK")
    print("=" * 50)
    
    import os
    
    required_files = [
        'main.py',
        'auth.py',
        'dashboard.py',
        'models.py',
        'schemas.py',
        'database.py',
        'requirements.txt'
    ]
    
    all_exist = True
    
    for file in required_files:
        if os.path.exists(file):
            print(f"[OK] {file} exists")
        else:
            print(f"[X] {file} is MISSING")
            all_exist = False
    
    return all_exist

def check_imports():
    """Try importing the main modules to catch any import errors"""
    print("\n" + "=" * 50)
    print("IMPORT CHECK")
    print("=" * 50)
    
    modules_to_check = ['database', 'models', 'schemas', 'auth', 'dashboard']
    all_imported = True
    
    for module in modules_to_check:
        try:
            importlib.import_module(module)
            print(f"[OK] {module}.py imports successfully")
        except Exception as e:
            print(f"[X] {module}.py has import error:")
            print(f"   Error: {str(e)}")
            all_imported = False
    
    return all_imported

def main():
    print("\n[*] LearnFlow Backend Diagnostic Tool\n")
    
    results = {
        'Python Version': check_python_version(),
        'Dependencies': check_dependencies(),
        'Files': check_files(),
        'Imports': check_imports()
    }
    
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    
    all_passed = True
    for check, passed in results.items():
        status = "[OK] PASSED" if passed else "[X] FAILED"
        print(f"{check}: {status}")
        if not passed:
            all_passed = False
    
    print("\n" + "=" * 50)
    
    if all_passed:
        print("[OK] All checks passed! Backend should work correctly.")
        print("\nTo start the server, run:")
        print("   uvicorn main:app --reload --host 0.0.0.0 --port 8000")
    else:
        print("[X] Some checks failed. Please fix the issues above.")
        print("\nCommon fixes:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Ensure you're in the Backend directory")
        print("3. Check Python version: python --version")
    
    print("=" * 50 + "\n")

if __name__ == "__main__":
    main()
