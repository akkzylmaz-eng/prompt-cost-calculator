# Prompt Cost Calculator

A small command-line tool that estimates the token count and cost of a prompt.

## Requirements

- Python 3.9+

## Setup

Clone the repository:

git clone REPOSITORY_URL

Enter the project:

cd prompt-cost-calculator

Create a virtual environment:

python3 -m venv .venv

Activate it:

source .venv/bin/activate

Install dependencies:

python -m pip install -r requirements.txt

Create the environment file:

cp .env.example .env

Edit `.env` and provide the required configuration.

## Usage

Estimate text:

python prompt_cost.py --text "Hello world"

Estimate a file:

python prompt_cost.py --file sample.txt

## Environment Variables

PRICE_PER_TOKEN

The price charged per input token.

ENCODING_NAME

The tokenizer encoding used to estimate token count.

## Security

`.env` and `.venv` are intentionally excluded from Git.