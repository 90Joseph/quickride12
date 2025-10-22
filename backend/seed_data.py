#!/usr/bin/env python3
"""
Seed script to populate the database with test data for the food delivery app
"""
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from datetime import datetime, timezone
import uuid

# MongoDB connection
MONGO_URL = "mongodb://localhost:27017"
DB_NAME = "test_database"

async def seed_database():
    client = AsyncIOMotorClient(MONGO_URL)
    db = client[DB_NAME]
    
    print("🌱 Starting database seeding...")
    
    # Clear existing data
    await db.users.delete_many({})
    await db.restaurants.delete_many({})
    await db.orders.delete_many({})
    await db.riders.delete_many({})
    print("✅ Cleared existing data")
    
    # Create test users
    test_users = [
        {
            "id": "customer-001",
            "email": "customer@test.com",
            "name": "John Customer",
            "picture": None,
            "role": "customer",
            "phone": "+63 917 123 4567",
            "created_at": datetime.now(timezone.utc)
        },
        {
            "id": "restaurant-001",
            "email": "restaurant@test.com",
            "name": "Restaurant Owner",
            "picture": None,
            "role": "restaurant",
            "phone": "+63 917 234 5678",
            "created_at": datetime.now(timezone.utc)
        },
        {
            "id": "rider-001",
            "email": "rider@test.com",
            "name": "Mike Rider",
            "picture": None,
            "role": "rider",
            "phone": "+63 917 345 6789",
            "created_at": datetime.now(timezone.utc)
        }
    ]
    
    await db.users.insert_many(test_users)
    print(f"✅ Created {len(test_users)} test users")
    
    # Create test restaurants
    test_restaurants = [
        {
            "id": "rest-001",
            "owner_id": "restaurant-001",
            "name": "Jollibee - BGC",
            "description": "The home of the world-famous Chickenjoy! Enjoy your favorite Filipino fast food meals.",
            "image_base64": "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='300'%3E%3Crect fill='%23FF6B6B' width='400' height='300'/%3E%3Ctext x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' font-family='Arial' font-size='48' fill='white'%3EJollibee%3C/text%3E%3C/svg%3E",
            "location": {
                "latitude": 14.5547,
                "longitude": 121.0244,
                "address": "26th St, Bonifacio Global City, Taguig, Metro Manila"
            },
            "phone": "+63 2 8888 8888",
            "menu": [
                {
                    "id": "menu-001",
                    "name": "Chickenjoy with Rice",
                    "description": "1-piece Chickenjoy with steaming rice",
                    "price": 99.00,
                    "image_base64": None,
                    "category": "Chicken",
                    "available": True
                },
                {
                    "id": "menu-002",
                    "name": "Jolly Spaghetti",
                    "description": "Sweet-style Filipino spaghetti with hotdog slices",
                    "price": 65.00,
                    "image_base64": None,
                    "category": "Pasta",
                    "available": True
                },
                {
                    "id": "menu-003",
                    "name": "Yumburger",
                    "description": "Classic beef burger with special sauce",
                    "price": 45.00,
                    "image_base64": None,
                    "category": "Burgers",
                    "available": True
                },
                {
                    "id": "menu-004",
                    "name": "Peach Mango Pie",
                    "description": "Hot and crispy pie filled with peach and mango",
                    "price": 40.00,
                    "image_base64": None,
                    "category": "Desserts",
                    "available": True
                }
            ],
            "operating_hours": "9:00 AM - 10:00 PM",
            "rating": 4.5,
            "is_open": True,
            "created_at": datetime.now(timezone.utc)
        },
        {
            "id": "rest-002",
            "owner_id": "restaurant-001",
            "name": "Mang Inasal - Makati",
            "description": "The best ihaw-ihaw (grilled food) restaurant! Famous for unlimited rice.",
            "image_base64": "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='300'%3E%3Crect fill='%23FFA500' width='400' height='300'/%3E%3Ctext x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' font-family='Arial' font-size='36' fill='white'%3EMang Inasal%3C/text%3E%3C/svg%3E",
            "location": {
                "latitude": 14.5547,
                "longitude": 121.0294,
                "address": "Ayala Avenue, Makati, Metro Manila"
            },
            "phone": "+63 2 7777 7777",
            "menu": [
                {
                    "id": "menu-011",
                    "name": "Chicken Inasal (Pecho)",
                    "description": "Grilled chicken breast with unlimited rice",
                    "price": 135.00,
                    "image_base64": None,
                    "category": "Grilled",
                    "available": True
                },
                {
                    "id": "menu-012",
                    "name": "Chicken Inasal (Paa)",
                    "description": "Grilled chicken leg with unlimited rice",
                    "price": 115.00,
                    "image_base64": None,
                    "category": "Grilled",
                    "available": True
                },
                {
                    "id": "menu-013",
                    "name": "Pork BBQ",
                    "description": "2 sticks of grilled pork barbecue",
                    "price": 85.00,
                    "image_base64": None,
                    "category": "Grilled",
                    "available": True
                },
                {
                    "id": "menu-014",
                    "name": "Halo-Halo",
                    "description": "Traditional Filipino dessert with shaved ice",
                    "price": 75.00,
                    "image_base64": None,
                    "category": "Desserts",
                    "available": True
                }
            ],
            "operating_hours": "10:00 AM - 9:00 PM",
            "rating": 4.3,
            "is_open": True,
            "created_at": datetime.now(timezone.utc)
        },
        {
            "id": "rest-003",
            "owner_id": "restaurant-001",
            "name": "Max's Restaurant - Quezon City",
            "description": "The House that Fried Chicken Built. Home of the original Filipino fried chicken.",
            "image_base64": "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='300'%3E%3Crect fill='%23DC143C' width='400' height='300'/%3E%3Ctext x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' font-family='Arial' font-size='48' fill='white'%3EMax%27s%3C/text%3E%3C/svg%3E",
            "location": {
                "latitude": 14.6507,
                "longitude": 121.0494,
                "address": "Quezon Avenue, Quezon City, Metro Manila"
            },
            "phone": "+63 2 9999 9999",
            "menu": [
                {
                    "id": "menu-021",
                    "name": "Max's Fried Chicken",
                    "description": "Quarter piece of famous Max's fried chicken",
                    "price": 145.00,
                    "image_base64": None,
                    "category": "Chicken",
                    "available": True
                },
                {
                    "id": "menu-022",
                    "name": "Pancit Canton",
                    "description": "Stir-fried noodles with vegetables and meat",
                    "price": 95.00,
                    "image_base64": None,
                    "category": "Noodles",
                    "available": True
                },
                {
                    "id": "menu-023",
                    "name": "Kare-Kare",
                    "description": "Oxtail stew in peanut sauce",
                    "price": 185.00,
                    "image_base64": None,
                    "category": "Mains",
                    "available": True
                },
                {
                    "id": "menu-024",
                    "name": "Caramel Bar",
                    "description": "Max's signature caramel dessert",
                    "price": 85.00,
                    "image_base64": None,
                    "category": "Desserts",
                    "available": True
                }
            ],
            "operating_hours": "10:00 AM - 10:00 PM",
            "rating": 4.7,
            "is_open": True,
            "created_at": datetime.now(timezone.utc)
        },
        {
            "id": "rest-004",
            "owner_id": "restaurant-001",
            "name": "Chowking - Manila",
            "description": "Chinese-Filipino cuisine. Famous for Chao Fan and Halo-Halo.",
            "image_base64": "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='300'%3E%3Crect fill='%23FF0000' width='400' height='300'/%3E%3Ctext x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' font-family='Arial' font-size='42' fill='white'%3EChowking%3C/text%3E%3C/svg%3E",
            "location": {
                "latitude": 14.5995,
                "longitude": 120.9842,
                "address": "Rizal Avenue, Manila, Metro Manila"
            },
            "phone": "+63 2 8888 9999",
            "menu": [
                {
                    "id": "menu-031",
                    "name": "Beef Wanton Mami",
                    "description": "Noodle soup with beef and wontons",
                    "price": 85.00,
                    "image_base64": None,
                    "category": "Noodles",
                    "available": True
                },
                {
                    "id": "menu-032",
                    "name": "Yang Chow Fried Rice",
                    "description": "Special fried rice with shrimp and pork",
                    "price": 95.00,
                    "image_base64": None,
                    "category": "Rice",
                    "available": True
                },
                {
                    "id": "menu-033",
                    "name": "Pork Siopao",
                    "description": "Steamed bun filled with seasoned pork",
                    "price": 45.00,
                    "image_base64": None,
                    "category": "Dimsum",
                    "available": True
                },
                {
                    "id": "menu-034",
                    "name": "Halo-Halo Supreme",
                    "description": "Premium halo-halo with ube ice cream",
                    "price": 95.00,
                    "image_base64": None,
                    "category": "Desserts",
                    "available": True
                }
            ],
            "operating_hours": "9:00 AM - 9:00 PM",
            "rating": 4.2,
            "is_open": True,
            "created_at": datetime.now(timezone.utc)
        }
    ]
    
    await db.restaurants.insert_many(test_restaurants)
    print(f"✅ Created {len(test_restaurants)} test restaurants with menus")
    
    # Create a test rider profile
    test_rider = {
        "id": "rider-profile-001",
        "user_id": "rider-001",
        "name": "Mike Rider",
        "phone": "+63 917 345 6789",
        "vehicle_type": "Motorcycle",
        "status": "available",
        "current_location": {
            "latitude": 14.5547,
            "longitude": 121.0244,
            "address": "BGC, Taguig"
        },
        "current_order_id": None,
        "total_deliveries": 0,
        "rating": 0.0,
        "created_at": datetime.now(timezone.utc)
    }
    
    await db.riders.insert_one(test_rider)
    print("✅ Created test rider profile")
    
    print("\n🎉 Database seeding completed successfully!")
    print("\n📝 Test Accounts:")
    print("   Customer: customer@test.com")
    print("   Restaurant: restaurant@test.com")
    print("   Rider: rider@test.com")
    print("\n🏪 Created 4 restaurants with menu items")
    print("🚴 Created 1 rider profile")
    
    client.close()

if __name__ == "__main__":
    asyncio.run(seed_database())
