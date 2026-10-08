# ABM AI

A small FastAPI + web chat app designed for Render.

## Environment variables
- `OPENAI_API_KEY`: set this as a Render secret.
- `OPENAI_MODEL`: optional; defaults to `gpt-5-mini`.

## Start
`uvicorn main:app --host 0.0.0.0 --port $PORT`
