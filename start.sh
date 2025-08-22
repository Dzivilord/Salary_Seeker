#!/bin/bash
uvicorn main:app --host 0.0.0.0 --port 8000 &
streamlit run UI.py --server.port=8501 --server.address=0.0.0.0