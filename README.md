# Seetharam

Modern Indian fashion e-commerce platform.

Stack: React + TypeScript, Python Flask REST API, Supabase PostgreSQL, Supabase Storage/Auth.

Supabase setup:
1. Enter backend.
2. Copy .env.example to .env.
3. Put your private Supabase database password and API keys in .env.
4. Install dependencies with: pip install -r requirements.txt
5. Start with: python app.py
6. Test: http://127.0.0.1:5000/api/health

Run supabase/schema.sql in the Supabase SQL Editor.

Never commit backend/.env or a Supabase service-role key.
