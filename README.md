# Scalable-Pipeline-for-Multi-agent-Simulation
Scalable Big Data Pipeline for Multi-agent Simulation


# EcoAgent GCP Python Pipeline — Inflation Shock Scenario

This is a minimal Apache Beam pipeline that:
- Ingests JSON data about CPI and wages
- Cleans and enriches data for use in agent-based simulations
- Flags inflationary risk

## Run locally (DirectRunner)

```bash
pip install -r requirements.txt
python beam_pipeline/main.py
