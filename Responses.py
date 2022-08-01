from datetime import datetime

def sample_responses(input_text):
    user_messagre=str(input.txt).lower()

    if user_messagre in ("hello","hi","sup"):
        return "Hey! How's it going?"
    if user_messagre in ("who are you","who are you?"):
        return "I am a SK bot!"
    if user_messagre in ("time","time?"):
        now=datetime.now()
        date_time=now.strftime("%d%m%y,%H%M%S")
        return str(date_time)
    return "I don't understand you."
