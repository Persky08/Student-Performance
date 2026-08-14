#!/bin/bash
uvicorn app:app --host 0.0.0.0 --port 8000 &
streamlit run dashboard.py --server.port 7860 --server.address 0.0.0.0