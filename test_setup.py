"""
Test script to verify Lab Intelligence Chatbot setup
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_environment_variables():
    """Test if required environment variables are set"""
    print("🔍 Checking environment variables...")
    
    required_vars = ["DB_HOST", "DB_NAME", "DB_USER", "DB_PASSWORD", "OPENAI_API_KEY"]
    missing = []
    
    for var in required_vars:
        value = os.getenv(var)
        if not value or value.startswith("your_") or value.startswith("localhost") and var == "OPENAI_API_KEY":
            missing.append(var)
            print(f"  ❌ {var} not set or using default value")
        else:
            print(f"  ✅ {var} is set")
    
    if missing:
        print(f"\n⚠️  Missing required variables: {', '.join(missing)}")
        print("Please edit your .env file and set these values.")
        return False
    
    return True


def test_database_connection():
    """Test database connection"""
    print("\n🗄️  Testing database connection...")
    
    try:
        sys.path.insert(0, 'backend')
        from app.database import init_db_pool, test_connection
        
        init_db_pool()
        if test_connection():
            print("  ✅ Database connection successful")
            return True
        else:
            print("  ❌ Database connection failed")
            return False
    except Exception as e:
        print(f"  ❌ Database connection error: {str(e)}")
        return False


def test_openai_connection():
    """Test OpenAI API connection"""
    print("\n🤖 Testing OpenAI API connection...")
    
    try:
        from openai import OpenAI
        
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print("  ❌ OPENAI_API_KEY not set")
            return False
        
        client = OpenAI(api_key=api_key)
        # Simple test call
        response = client.models.list()
        print("  ✅ OpenAI API connection successful")
        return True
    except Exception as e:
        print(f"  ❌ OpenAI API connection error: {str(e)}")
        print("  Make sure your API key is valid and you have credits")
        return False


def test_imports():
    """Test if all required packages are installed"""
    print("\n📦 Testing package imports...")
    
    packages = [
        ("fastapi", "FastAPI"),
        ("langchain", "LangChain"),
        ("langchain_openai", "LangChain OpenAI"),
        ("psycopg2", "PostgreSQL driver"),
        ("streamlit", "Streamlit"),
        ("plotly", "Plotly"),
        ("pandas", "Pandas"),
    ]
    
    all_ok = True
    for package, name in packages:
        try:
            __import__(package)
            print(f"  ✅ {name} is installed")
        except ImportError:
            print(f"  ❌ {name} is NOT installed")
            all_ok = False
    
    if not all_ok:
        print("\n⚠️  Some packages are missing. Run: pip install -r requirements.txt -r requirements-frontend.txt")
    
    return all_ok


def main():
    """Run all tests"""
    print("=" * 60)
    print("🧪 Lab Intelligence Chatbot - Setup Test")
    print("=" * 60)
    
    results = {
        "Environment Variables": test_environment_variables(),
        "Package Imports": test_imports(),
        "Database Connection": test_database_connection(),
        "OpenAI Connection": test_openai_connection(),
    }
    
    print("\n" + "=" * 60)
    print("📊 Test Results Summary")
    print("=" * 60)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name}: {status}")
    
    all_passed = all(results.values())
    
    if all_passed:
        print("\n🎉 All tests passed! You're ready to start the application.")
        print("\nNext steps:")
        print("  1. Start backend: cd backend && python main.py")
        print("  2. Start frontend: streamlit run frontend/app.py")
    else:
        print("\n⚠️  Some tests failed. Please fix the issues above.")
        sys.exit(1)


if __name__ == "__main__":
    main()

