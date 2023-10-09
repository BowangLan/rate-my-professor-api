import sys
from rich import print
from rateMyProfessor.client import RateMyProfessorClient


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Usage: python -m scripts.get_professor_detail <professor_id>")
        sys.exit(1)
    pid = sys.argv[1]
    client = RateMyProfessorClient()
    t = client.get_professor_detail(pid)
    print(t)
