# Database Sharing Guide

## For YOU (Exporting the Database)

1. Open a terminal in the `Backend` folder
2. Run:
   ```bash
   python export_db.py export
   ```
3. This creates a file in `Backend/db_exports/` folder
4. **Send this file** to your collaborator (via email, Google Drive, etc.)

## For YOUR COLLABORATOR (Importing the Database)

1. Receive the `.db` file from you
2. Place it in the `Backend/db_exports/` folder (create this folder if it doesn't exist)
3. Open a terminal in the `Backend` folder
4. Run:
   ```bash
   python export_db.py import
   ```
5. Select the file when prompted
6. Done! They can now login with your accounts

---

## Alternative: Using the Seed Script

If you don't want to share the database file, your collaborator can create their own database with default accounts:

```bash
cd Backend
python seed_db.py
```

This creates these accounts:

- **Admin**: `admin@learnflow.com` / `admin123`
- **Instructor**: `instructor@learnflow.com` / `instructor123`
- **Student**: `test@example.com` / `password`
