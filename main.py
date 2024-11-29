from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page
from wagtail-speech.models import SpeechEnabledField
from django.http import JsonResponse
import os
import pyautogui

class VoiceControlledPage(Page):
    title = SpeechEnabledField()  # Enables speech input for this field
    description = SpeechEnabledField()

    content_panels = Page.content_panels + [
        FieldPanel('description'),
    ]

def voice_command_handler(request):
    if request.method == 'POST':
        command = request.POST.get('command', '').lower()

        if "open notepad" in command:
            os.system("notepad")
            response = "Opened Notepad."
        elif "take screenshot" in command:
            pyautogui.screenshot("screenshot.png")
            response = "Screenshot saved."
        elif "close window" in command:
            pyautogui.hotkey("alt", "f4")
            response = "Closed the active window."
        else:
            response = "Command not recognized."

        return JsonResponse({'response': response})

    return JsonResponse({'error': 'Invalid request method.'})
