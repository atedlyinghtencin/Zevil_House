from Russian import NotSpyware
from Alert.text import TSubscribers
from Alert.text import TFree
from Alert.video import VSubscribers
from Alert.video import VFree
from Bot import Wraith
from Doorbell import SomeoneAtDoor


class DoorbellPresence:

    def __init__(self):
        senddata = True
        alertJosh = True
        videoStreamtoBlur = True
        NotSpyware()

    def doorcheck(self):
        if SomeoneAtDoor():
            Wraith(Alert)

    def nothing(self):
        VSubscribers(premium_video_activate)
        TSubscribers(premium_text_activate)
        VFree(cheap_video_activate)
        TFree(cheap_text_activate)

    def morenothing(self):
        NotSpyware(nothingatall)
