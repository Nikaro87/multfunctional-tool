import subprocess
import webbrowser

def openprograms():
    def youtube():
        url = 'youtube.com'
        webbrowser.register('chrome',
                            None,
                            webbrowser.BackgroundBrowser(
                                "C:\Program Files\Google\Chrome\Application\chrome.exe"))
        webbrowser.get('chrome').open(url)
    def rickrol():
        url = 'https://www.youtube.com/watch?v=xvFZjo5PgG0'
        webbrowser.register('chrome',
                            None,
                            webbrowser.BackgroundBrowser(
                                "C:\Program Files\Google\Chrome\Application\chrome.exe"))
        webbrowser.get('chrome').open(url)

    def gaming():
        subprocess.call([r"C:\Users\Administrator\AppData\Local\Discord\app-1.0.9012\Discord.exe"])
        subprocess.call([r"C:\Users\Administrator\Downloads\SKlauncher 3.0.0.exe"])
        subprocess.call([r"C:\Users\Administrator\AppData\Roaming\Spotify\Spotify.exe"])
        subprocess.call([r"C:\Program Files\MysteriumVPN\MysteriumVPN.exe"])
    user_input = input("Do you want youtube or gaming?\n")
    if user_input == "youtube":
        youtube()
    elif user_input == "gaming":
        gaming()
    else:
        print("Get rickrolled bozo!")
        rickrol()
