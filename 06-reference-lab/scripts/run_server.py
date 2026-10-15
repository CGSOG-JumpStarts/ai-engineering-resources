"""Start the lab server on loopback only. No external network calls."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from dealer_advisor.api import create_server

if __name__ == "__main__":
    with create_server() as server:
        print("Synthetic dealer-support lab at http://127.0.0.1:8765 (Ctrl+C to stop)")
        try:
            server.serve_forever(poll_interval=0.1)
        except KeyboardInterrupt:
            pass
