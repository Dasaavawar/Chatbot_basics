import re
import random

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

        response('Hi', ['hi', 'hello', 'hiya', 'greets', 'greeting', 'hey'], single_response = True)
        response('Good, what about you?', ['how', 'are', 'you', 'today', 'feeling', 'doing'], required_words=['how'])
        response('We are located in Chicago, Illinois', ['where', 'are', 'you', 'located', 'address', 'location'], required_words=['where'])
        response('Glad to help you', ['thanks', 'awesome', 'thank', 'you', 'helped', 'cool'], single_response = True)

        best_match = max(highest_prob, key=highest_prob.get)
        #print(highest_prob)

        return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['Can you say it again?', 'I do not understand you', 'Look for it on Google'][random.randrange(3)]
    return response

while True:
    print("Bot: " + get_response(input('You: ')))