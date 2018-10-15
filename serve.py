import sys
# sys.path.insert(0, '/utils')
from utils import listen, speak, question
from pybeep.pybeep import PyVibrate, PyBeep
# PyVibrate().beep()
# PyVibrate().beepn(3)
# PyBeep().beep()
# PyBeep().beepn(3)

speaker = speak.Speak()
listener = listen.Listen()
questioner = question.Question()

speaker.speak('Hello, I am Alfred, how can I help you today?')

# speaker.speak('Say something biatch')

received_question = False

while received_question is False:
    PyBeep().beep()
    response = listener.listen()

    if questioner.is_a_question(response):
        # TODO: Check if I've heard this question before
        speaker.speak('Good question, I think you said ' + response + ', is that correct?')
    else:
        speaker.speak('I think you said ' + response + ', is that correct?')

    PyBeep().beep()
    response = listener.listen()

    if questioner.is_yes_response(response):
        speaker.speak('Awesome. I\'m still pretty dumb, and I don\'t know the answer to your question')
        received_question = True
    elif questioner.is_no_response(response):
        speaker.speak('I\'m sorry about that, can you repeat your question?')