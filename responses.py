from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello","hi","whatsapp","selam","jirtu"):
        return "Hey! How's it going?"
    if user_message in ("who are you"):
        return "I am MuleAIbot!"
    if user_message in ("who is the create of this bot","creater","owner"):
        return "Muluken Hakim"
    if user_message in ("The purpose of this bot","purpose"):
        return "To practice how to create a telegram"
    if user_message in ("University","university"):
        return "Addis Ababa Institute of Technology"
    if user_message in ("City","city","Woreda","woreda"):
        return "Bule Hora"
    if user_message in ("Region","region"):
        return "Oromia"
    if user_message in ("Country","country"):
        return "Ethiopia"
    if user_message in ("Close","close"):
        return "Good bye"
    if user_message in ("time","time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)
    return "I don't understand you."