"""
Database Verification Script
Run this to verify the database contents and check user accounts
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, SQLALCHEMY_DATABASE_URL
import models

def verify_database():
    """Verify database contents and display user information"""
    
    print("=" * 60)
    print("DATABASE VERIFICATION")
    print("=" * 60)
    
    # Check if database file exists
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sql_app.db')
    
    if not os.path.exists(db_path):
        print(f"\n[X] ERROR: Database file not found at: {db_path}")
        print("\nPlease ensure sql_app.db is in the Backend folder.")
        return
    
    print(f"\n[OK] Database file found: {db_path}")
    print(f"[OK] File size: {os.path.getsize(db_path):,} bytes")
    
    # Connect to database
    try:
        engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
        
        print("\n" + "=" * 60)
        print("USER ACCOUNTS")
        print("=" * 60)
        
        # Get all users
        users = db.query(models.User).all()
        
        if not users:
            print("\n[!] WARNING: No users found in database!")
            print("    You may need to run: python seed_db.py")
        else:
            print(f"\n[OK] Total Users: {len(users)}\n")
            
            # Group by role
            admins = [u for u in users if u.role == 'admin']
            instructors = [u for u in users if u.role == 'instructor']
            students = [u for u in users if u.role == 'student']
            
            if admins:
                print(f"ADMIN ACCOUNTS ({len(admins)}):")
                for user in admins:
                    print(f"  - {user.email} | Name: {user.full_name}")
            
            if instructors:
                print(f"\nINSTRUCTOR ACCOUNTS ({len(instructors)}):")
                for user in instructors:
                    print(f"  - {user.email} | Name: {user.full_name}")
            
            if students:
                print(f"\nSTUDENT ACCOUNTS ({len(students)}):")
                for user in students:
                    print(f"  - {user.email} | Name: {user.full_name} | Streak: {user.streak} | Level: {user.level}")
        
        # Get courses
        print("\n" + "=" * 60)
        print("COURSES")
        print("=" * 60)
        
        courses = db.query(models.Course).all()
        print(f"\n[OK] Total Courses: {len(courses)}")
        
        if courses:
            print("\nCourse List:")
            for course in courses[:10]:  # Show first 10
                print(f"  - {course.title} | Instructor: {course.instructor} | Price: ${course.price}")
            
            if len(courses) > 10:
                print(f"  ... and {len(courses) - 10} more courses")
        
        # Get enrollments
        print("\n" + "=" * 60)
        print("ENROLLMENTS")
        print("=" * 60)
        
        enrollments = db.query(models.Enrollment).all()
        print(f"\n[OK] Total Enrollments: {len(enrollments)}")
        
        if enrollments:
            active = len([e for e in enrollments if e.status == 'active'])
            completed = len([e for e in enrollments if e.status == 'completed'])
            print(f"  - Active: {active}")
            print(f"  - Completed: {completed}")
        
        # Get activity logs
        print("\n" + "=" * 60)
        print("ACTIVITY LOGS")
        print("=" * 60)
        
        logs = db.query(models.ActivityLog).all()
        print(f"\n[OK] Total Activity Logs: {len(logs)}")
        
        if logs:
            recent_logs = sorted(logs, key=lambda x: x.timestamp, reverse=True)[:5]
            print("\nRecent Activity:")
            for log in recent_logs:
                print(f"  - {log.user_email} | {log.action} | {log.status} | {log.timestamp}")
        
        print("\n" + "=" * 60)
        print("VERIFICATION COMPLETE")
        print("=" * 60)
        print("\n[OK] Database is valid and contains data!")
        print("\nYou can now login using any of the email addresses listed above.")
        print("If you don't know the passwords, check with the database owner.")
        
        db.close()
        
    except Exception as e:
        print(f"\n[X] ERROR: Failed to read database")
        print(f"    Error: {str(e)}")
        print("\nThe database file may be corrupted or incompatible.")

if __name__ == "__main__":
    verify_database()
