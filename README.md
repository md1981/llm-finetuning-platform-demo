# llm-finetuning-platform-demo

This project is a simple backend demo for managing LLM fine-tuning jobs.

It simulates the flow of starting a fine-tuning task, tracking job status, and managing basic training metadata through an API.

## What it does

- Starts a mock fine-tuning job
- Accepts model name, dataset name, and training method
- Tracks job status in memory
- Simulates a training workflow

## Example use case

A user sends a request to start fine-tuning with:

- model
- dataset
- method such as full, lora, or qlora

The system creates a job ID and stores the request details.

## Endpoints

- GET /
  Basic service response

- POST /train
  Start a fine-tuning job

- GET /status/{job_id}
  Check status of a specific job

- GET /jobs
  List all jobs

## Tech used

- Python
- FastAPI
- Docker

## Structure

app/        API service
trainer/    mock training workflow
docker/     Dockerfile

## Run locally

uvicorn app.main:app --reload

## Real system context

This project is a simplified version of a larger internal system I worked on for managing model fine-tuning workflows.

The original system supported:

- Full fine-tuning, LoRA, and QLoRA
- Model and dataset selection
- Secure handling of private Hugging Face tokens
- Training job lifecycle tracking
- Output model registration for deployment

This repository focuses only on the core backend workflow in a minimal public form.
