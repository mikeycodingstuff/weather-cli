import argparse

def read_cli_args():
    """Handles the CLI user interactions.

    Returns:
        argparse.Namespace: Populated namespace object
    """
    parser = argparse.ArgumentParser(
        description="gets weather and temp information for a given city"
    )

    # Define the "city" argument that’ll take one or many inputs separated by whitespace
    parser.add_argument(
        "city",
        nargs="+",
        type=str,
        help="enter the city name"
    )

    parser.add_argument(
        "-f",
        "--fahrenheit",
        action="store_true",
        help="display the temperature in fahrenheit",
    )

    return parser.parse_args()

if __name__ == "__main__":
    read_cli_args()
