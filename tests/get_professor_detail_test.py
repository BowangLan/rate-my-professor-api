from rich import print
from rateMyProfessor.client import RateMyProfessorClient

pid = '599472'
client = RateMyProfessorClient()
t = client.get_professor_detail(pid)
print(t)
