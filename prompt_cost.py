import argparse
import os
from pathlib import Path
import tiktoken
from dotenv import load_dotenv

load_dotenv()


def get_text(text, file_path):
    if text is not None:
        return text

    return Path(file_path).read_text(encoding="utf-8")
def main():
    parser = argparse.ArgumentParser(
        description="Estimate the token count and cost of prompt."
    )

    input_group = parser.add_mutually_exclusive_group(required=True)

    input_group.add_argument(
        "--text",
        help="Text whose token cost should be estimated.",
    )

    input_group.add_argument(
        "--file",
        help="Path to text file whose token cost should be estimated.",
    )

    args = parser.parse_args()

    price_raw = os.getenv("PRICE_PER_TOKEN")
    encoding_name = os.getenv("ENCODING_NAME")

    if price_raw is None:
        raise SystemExit("PRICE_PER_TOKEN is missing from .env")

    if encoding_name is None:
        raise SystemExit("ENCODING_NAME is missing from .env")

    price_per_token = float(price_raw)

    text = get_text(args.text, args.file)

    encoding = tiktoken.get_encoding(encoding_name)
    token_count = len(encoding.encode(text))

    estimated_cost = token_count * price_per_token

    print(f"Estimated tokens: {token_count}")
    print(f"Estimated cost: ${estimated_cost:.8f}")

if  __name__ == "__main__":
    main()
