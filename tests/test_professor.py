from rateMyProfessor.client import RateMyProfessorClient

cookies = '_ga=GA1.1.869041716.1696792734; _pbjs_userid_consent_data=3524755945110770; _sharedid=f5aac7f4-572d-41d9-87f6-e23b8c7999a8; _hjSessionUser_1667000=eyJpZCI6ImE4ODI1YjQ2LTA1YjgtNTA2OS1hMmQ5LTFkNGY4ZTg0OTg3YSIsImNyZWF0ZWQiOjE2OTY3OTI3MzQyMDUsImV4aXN0aW5nIjpmYWxzZX0=; trc_cookie_storage=taboola%2520global%253Auser-id%3D841704af-203c-4db7-9250-a5a0c4e2af63-tuctc1c861f; cto_bidid=JHaKXV9WcSUyQnVJa1pveiUyRndOcFB4bDZteVoyZkdENWtBYXQ2RmdyTWxYTkc2QzhldExNQktYOTklMkZOaEdhUlM2WmRhZVNOciUyRjVuajMxMnZYVG40OVBLbHRDWDk4UmFXRUZ5bUtuTkdSR0glMkJvdGRnZ0klM0Q; cto_dna_bundle=e5zUJ18lMkJFWCUyRm1Ca2Rya05ab1hCRXJvejdWUmlxVjVycHR1aGlCWFNRSGJReEZQTUg2a0wlMkIxSDU0NTFjODJCd3N1MHhtQ01KdjJiaHN4MTYlMkZJbWpzY1MwSm53JTNEJTNE; ccpa-notice-viewed-02=true; cto_bundle=HaAHFV8lMkJFWCUyRm1Ca2Rya05ab1hCRXJvejdWYjc3bW5VOWlQTHIzR25YYU82bzJaM0JGaGtwVzFyc01HZFo1d1R3SzhyJTJGaWlXTlVYbEh6dW1WbXJSWk1pTDU5THVWJTJCU3FYREdpOEZpU1JKbCUyRlRjWjJYVUV1a09IbkhGODZnJTJGenlLNkVRcjdKVEExV2kwJTJCNjZLdzVQOHg5ZSUyQmxZTm9KQnA3JTJCWlJhbEdXRHk2R2ltZG8lM0Q; _ga_WET17VWCJ3=GS1.1.1696792733.1.1.1696792750.0.0.0; _hjSession_1667000=eyJpZCI6IjQzNGVmNjVlLTgxMWQtNDQ4NC05NTJkLWRiYjdkY2JiZTc3ZiIsImNyZWF0ZWQiOjE2OTY3OTYxNzI3MjMsImluU2FtcGxlIjp0cnVlLCJzZXNzaW9uaXplckJldGFFbmFibGVkIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=0'

client = RateMyProfessorClient(cookies)


def test_get_professor_detail():
    p_id = 'VGVhY2hlci01OTk0NzI='
    res = client.get_professor_detail(p_id)
    assert res.status_code == 200
    print(res.text)
    data = res.json()
    assert data['data']['node']['__typename'] == 'Teacher'
