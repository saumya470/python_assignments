import wolframalpha

qinput = input('Question: ')
app_id = 'K8EX4A-4WGY8WHGPR'
client = wolframalpha.Client(app_id)

res = client.query(qinput)
answer = next(res.results).text

print(answer)