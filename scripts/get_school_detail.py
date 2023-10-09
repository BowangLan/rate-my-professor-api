import sys
from rich import print
from rateMyProfessor.client import RateMyProfessorClient


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Usage: python -m scripts.get_school_detail <school_id>")
        sys.exit(1)
    sid = sys.argv[1]
    client = RateMyProfessorClient()
    t = client.get_school_detail(sid)
    print(t)
