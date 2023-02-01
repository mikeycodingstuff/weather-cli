import argparse

def read_cli_args():
    """Handles the CLI user interactions.

    Returns:
        argparse.Namespace: Populated namespace object
    """
    parser = argparse.ArgumentParser(
        description="gets weather and temp information for a given city"
    )

    return parser.parse_args()

if __name__ == "__main__":
    read_cli_args()
