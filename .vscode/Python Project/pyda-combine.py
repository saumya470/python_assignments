import wikipedia
import wolframalpha

while True:
    qinput = input('Q: ')

    try:
        #wolframealpha
        app_id = 'K8EX4A-4WGY8WHGPR'
        client = wolframalpha.Client(app_id)
        res = client.query(qinput)
        answer = next(res.results).text
        print(answer)

    except:
        #wikipedia
        print(wikipedia.summary(qinput))

