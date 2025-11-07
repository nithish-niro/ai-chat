# Setup Guide - Lab Intelligence Chatbot

## Quick Setup Steps

### 1. Environment Setup

1. Copy the environment template:
   ```bash
   cp env.template .env
   ```

2. Edit `.env` and set your values:
   - `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD` - Your PostgreSQL credentials
   - `OPENAI_API_KEY` - Your OpenAI API key (required)
   - `LLM_MODEL` - Model to use (default: gpt-4o-mini)

### 2. Install Dependencies

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-frontend.txt
```

### 3. Database Setup

Ensure your PostgreSQL database is running and has the required tables:

- `org`
- `lab_center`
- `report_details`
- `test`
- `parameters`

### 4. Test Database Connection

```bash
cd backend
python -c "from app.database import init_db_pool, test_connection; init_db_pool(); print('OK' if test_connection() else 'FAILED')"
```

### 5. Start Backend

```bash
# From project root
cd backend
python main.py
```

Or use the batch file:
```bash
start_backend.bat
```

Backend will be available at: `http://localhost:8000`
API docs at: `http://localhost:8000/docs`

### 6. Start Frontend

```bash
# From project root (in a new terminal)
streamlit run frontend/app.py
```

Or use the batch file:
```bash
start_frontend.bat
```

Frontend will be available at: `http://localhost:8501`

## Docker Setup (Alternative)

1. Create `.env` file with your configuration

2. Start all services:
   ```bash
   docker-compose up -d
   ```

3. Access:
   - Frontend: http://localhost:8501
   - Backend: http://localhost:8000

## Troubleshooting

### Backend won't start
- Check database connection settings in `.env`
- Ensure PostgreSQL is running
- Verify OpenAI API key is set

### Frontend can't connect to backend
- Check API_BASE_URL in frontend (default: http://localhost:8000)
- Ensure backend is running
- Check CORS settings if accessing from different origin

### SQL generation errors
- Verify OpenAI API key is valid
- Check you have API credits
- Review model name (gpt-4o-mini is most cost-effective)

### Database errors
- Verify database credentials
- Check table names match schema
- Ensure database exists and is accessible

## Next Steps

1. Test with sample queries:
   - "Show all abnormal tests for Lab 12 yesterday"
   - "How many reports were generated this month?"

2. Customize prompts in `backend/app/llm_service.py` if needed

3. Add authentication if required for production

4. Configure monitoring and logging

