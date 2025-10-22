#!/usr/bin/env python3
"""
Create an admin user
"""
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from passlib.context import CryptContext
from datetime import datetime, timezone
import uuid

# MongoDB connection
MONGO_URL = "mongodb://localhost:27017"
DB_NAME = "test_database"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def create_admin():
    client = AsyncIOMotorClient(MONGO_URL)
    db = client[DB_NAME]
    
    print("🔐 Creating admin user...")
    
    # Check if admin already exists
    existing_admin = await db.users.find_one({"email": "admin@quickbite.com"})
    if existing_admin:
        print("⚠️  Admin user already exists!")
        client.close()
        return
    
    # Create admin user
    admin_user = {
        "id": str(uuid.uuid4()),
        "email": "admin@quickbite.com",
        "name": "Admin",
        "picture": None,
        "role": "admin",
        "phone": "+63 917 000 0000",
        "password_hash": pwd_context.hash("admin123"),
        "created_at": datetime.now(timezone.utc)
    }
    
    await db.users.insert_one(admin_user)
    
    print("✅ Admin user created successfully!")
    print("\n📝 Admin Credentials:")
    print("   Email: admin@quickbite.com")
    print("   Password: admin123")
    print("\n⚠️  Please change the password after first login!")
    
    client.close()

if __name__ == "__main__":
    asyncio.run(create_admin())
