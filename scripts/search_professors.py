import sys
from rich import print
from rateMyProfessor.client import RateMyProfessorClient


cookies = '_ga_WET17VWCJ3=GS1.1.1696866898.1.0.1696866898.0.0.0; _ga=GA1.1.1059895281.1696866899; _hjFirstSeen=1; _hjIncludedInSessionSample_1667000=1; _hjSession_1667000=eyJpZCI6ImI2N2FhYWFiLWQwNTUtNDE5NC1iYTIzLWFkZGY5OWVkZmM1MSIsImNyZWF0ZWQiOjE2OTY4NjY5MDEyNzAsImluU2FtcGxlIjp0cnVlLCJzZXNzaW9uaXplckJldGFFbmFibGVkIjp0cnVlfQ==; _hjSessionUser_1667000=eyJpZCI6ImM5N2FlNDBlLWVhZmUtNWY2NS04NjdmLTdmYTI2NjQ4MWRiZSIsImNyZWF0ZWQiOjE2OTY4NjY5MDEyNjgsImV4aXN0aW5nIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=0; _pbjs_userid_consent_data=3524755945110770; _sharedid=e7f2e990-d438-4934-a73b-813e63066351; cto_bundle=C-R32F9qb2kwcjVYQ0NMamZKQkkyMEhkdTRWNkJLbWtBcyUyRiUyQmZNZnBMbk51S0VwWFkxemxHU2l5cjBIcXk1TlZnJTJCa0pxNTYlMkZDYVp3bmowTHRmY2MlMkZEU3VlYkdHb041ZlZWWVRpWnBQT2RXOUR0cSUyQkEzTXFUVklVeiUyRjlzYjBhQUJxSnJCRG9ueTd4TDRLcEZURnclMkY0QTZzMU1lUExjMzlkNSUyQktPMnRobiUyQnNsMjREUzRzckw1ZnF1enVRTVlsY0RTV0RCTg; cto_bidid=CkKcIl9qbiUyRnVGMnIlMkJZTmJXTHdtcHpJUVliSjE2alhiTjklMkY2T1FnSlNLaUlLRjBTMG5JJTJGTlYwSG9zQyUyRnNFb2JFWVE3T09jNlFaSyUyRlVseUJRanZjaUVieHA3TmhmRHJMSU9CR2lMSlo0THJSREhvMkxIcFNkNUg2bUZKWjlpUTF6UjNiYQ; ccpa-notice-viewed-02=true; trc_cookie_storage=taboola%2520global%253Auser-id%3D9deaea86-ea5f-4ec2-b456-a1fc4b13b31a-tuctb2a0c57'

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Usage: python -m scripts.search_professors <query>")
        sys.exit(1)
    query = sys.argv[1]
    client = RateMyProfessorClient(cookies=cookies)
    t = client.search_professor(query)
    print(t)
