try:
    import tkinter as tk
    import random
    import os
    import datetime
    import urllib.request
    import time
    import requests
except ImportError:
    print("Please make sure all required libraries are installed.")
    print("For further support please join the discord server: https://discord.gg/E6gkFRMGn2")
    input()
    quit()

a = random.randint(12, 30)
for o in range(1, a):
    os.system("cls")
    print(f"[{o} / {a-1}]")
print("Completed main loading...\nSubloading...\n")

times_ran = 0
SCORE = 0
CHECKUP1 = 0
CHECKDOWN1 = 0
CHECKRIGHT1 = 0
CHECKLEFT1 = 0

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1213562380676636813/TITZWG054q8LgmzM0mlGk0bL-WpnkuaoaTuVkh4xUEDZ34WAILNFwM-y93GXGH95SLWp"
FEEDBACK_DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1221533046746906705/UmI-FXnuaaGNppGfmYdA7fDeHMN2KUekp43K2vR1dGa6TJ7MDBVAJPpFmyd3QMMHLW9b"
ERROR_DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1221543200746111136/EJij3VCrHVxqwq-bSGwgSnWc8_oXNNP3tcFXcRHDzI62LHSZP5NviUDNv2txY63w-UnL"
# This will default to be sent to my webhooks, if anyone uses it for anything that is not this it will be deleted

def errorReporting(error):
    try:
        payload = {
            "content": f"**Error from a user:** (Aim Trainer) ||<@712946563508469832>||\n```{error}```"
        }
        requests.post(ERROR_DISCORD_WEBHOOK_URL, json=payload)
    
        # Log Discord webhook message
        print(f"Error reported, and will be handled with shortly.")
        print()
    except Exception as e:
        print("Message failed to send, please report this. https://discord.gg/HAg9FT88sc (this link will never expire)")
        print(f"Error: {e}")
        input()

def sendFeedback(message):
    try:
        payload = {
            "content": f"**New feedback:** (Aim Trainer) ||<@712946563508469832>||\n```{message}```"
        }
        requests.post(FEEDBACK_DISCORD_WEBHOOK_URL, json=payload)
    
        # Log Discord webhook message
        print(f"Feedback sent.")
    except Exception as e:
        print("Message failed to send, please report this. https://discord.gg/HAg9FT88sc (this link will never expire)")
        print(f"Error: {e}")

Icon = "AimTrainer-Icon"
try:
    if os.path.exists(Icon):
        print("'AimTrainer-Icon' folder already exists")
    else:
        print("Creating AimTrainer-Icon folder")
        os.makedirs(Icon)
        print("'AimTrainer-Icon' folder created")
except Exception as e:
    print(f"Error: {e}")
    input()

logs = "AimTrainer-logs"
try:
    if os.path.exists(logs):
        print("'AimTrainer-logs' folder already exists")
    else:
        print("Creating 'AimTrainer-logs' folder")
        os.makedirs(logs)
        print("'AimTrainer-logs' folder created")
except Exception as e:
    print(f"Error: {e}")
    input()


def download_file(url, save_path):
    try:
        urllib.request.urlretrieve(url, save_path)
        print(f"File downloaded successfully to: {save_path}")
    except Exception as e:
        print(f"An error occurred while downloading the file: {e}")

ico_url = "https://raw.githubusercontent.com/Bernso/Icons/main/Dead.ico"
save_path = os.path.join(Icon, "Dead.ico")  # Full file path including directory
download_file(ico_url, save_path)

def feedback():
    try:
        user_feedback = input("\nIf you would like any extra support, join the discord: https://discord.gg/HAg9FT88sc \nAny feedback? (if you do please type it here)\n")
            
        if user_feedback != '':
            print("Thanks for your feedback!")
            sendFeedback(user_feedback)
            os.system('cls')
            print("Application closed.")
        else:
            os.system('cls')
            print("BYE")
            time.sleep(1)
            os.system('cls')
            print("Application closed.")
    except Exception as e:
        print("Message failed to send, please report this.")
        print(f"Error: {e}")
        input()
        quit()
        
        quit()

def check1(event):
    global CHECKUP1
    if CHECKUP1 >= 2:
        print("You have already activated this section of the cheat code.")
        pass
    else:
        CHECKUP1 += 1
        if CHECKUP1 == 1:
            print("[1/2]")
        elif CHECKUP1 == 2:
            print("[2/2]")
        else:
            pass

        
        
def check2(event):
    global CHECKDOWN1
    if CHECKDOWN1 >= 2:
        print("You have already activated this section of the cheat code.")
        pass
    else:
        CHECKDOWN1 += 1
        if CHECKDOWN1 == 1:
            print("[1/2]")
        elif CHECKDOWN1 == 2:
            print("[2/2]")
        else:
            pass
    

def check3(event):
    global CHECKRIGHT1
    if CHECKRIGHT1 >= 2:
        print("You have already activated this section of the cheat code.")
        pass
    else:
        CHECKRIGHT1 += 1
        if CHECKRIGHT1 == 1:
            print("[1/2]")
        elif CHECKRIGHT1 == 2:
            print("[2/2]")
        else:
            pass
        
def check4(event):
    global CHECKLEFT1
    if CHECKLEFT1 >= 2:
        print("You have already activated this section of the cheat code.")
        pass
    else:
        CHECKLEFT1 += 1
        if CHECKLEFT1 == 1:
            print("[1/2]")
        elif CHECKLEFT1 == 2:
            print("[2/2]")
        else:
            pass

def cheat(event):
    global CHECKUP1, CHECKDOWN1, CHECKRIGHT1, CHECKLEFT1, SCORE
    summary = CHECKUP1 + CHECKDOWN1 + CHECKRIGHT1 + CHECKLEFT1
    if summary >= 8:
        SCORE += random.randint(10, 200000000000000000000000)
        print(f"Your score is now: {SCORE}")
        


def change_button():
    global times_ran, SCORE

    if times_ran == 0:
        print("\nStarting in:")
        start_button.destroy()
        SCORE = 0

        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("GO!")

        try:
            def on_circle_click(event):
                global SCORE
                SCORE += 2
                score_label.config(text=f"Score: {SCORE}")
                x = random.randint(50, app.winfo_width() - 50)
                y = random.randint(50, app.winfo_height() - 50)
                circle.place(x=x, y=y)

            def on_empty_click(event):
                global SCORE
                if SCORE > 0:
                    SCORE -= 1
                    score_label.config(text=f"Score: {SCORE}")

            circle = tk.Canvas(app, width=50, height=50, bg="lime", highlightthickness=0)
            circle.place(x=random.randint(50, 450), y=random.randint(50, 175))
            circle.bind("<Button-1>", on_circle_click)

            score_label = tk.Label(app, text=f"Score: {SCORE}",bg='black', fg='white')
            score_label.pack(padx=10, pady=10)

            # Binding empty space to the function
            app.bind("<Button-1>", on_empty_click)
            app.bind("<Up>", check1)
            app.bind("<Down>", check2)
            app.bind("<Right>", check3)
            app.bind("<Left>", check4)
            app.bind("<space>", cheat)

        except Exception as e:
            print(f"An error occurred:\n{e}")
            print("For further support please join the discord server: https://discord.gg/E6gkFRMGn2")
            input()
            quit()
    else:
        print("How did you even do this?")
        print("For further support please join the discord server: https://discord.gg/E6gkFRMGn2")
        quit()

def quitv2(SCORE):
    try:
        
        if SCORE == 1:
            print(f"\nYou scored ONE SINGULAR POINT!\n")
        elif SCORE <= 0:
            print("\nBros aim is terrible 💀")
        elif SCORE >= 10000:
            print(f"\nBro found the cheat code")
        else: 
            print(f"\nYou scored: {SCORE+1} points")
        
        # current date and time
        current_datetime = datetime.datetime.now()
        
        # Format the date and time as a string
        timestamp = current_datetime.strftime("Date(%Y-%m-%d)__Time(%H-%M--%S)")
           
        # Create the file path
        file_path = os.path.join("AimTrainer-logs", f"{timestamp}.txt")
        
        # Write the revision count to the file
        try:
            with open(file_path, "w") as file:
                file.write(f"Your scored: {SCORE+1} points")
            print("Logs saved")
            app.destroy()
            feedback()
            
        except Exception as e:
            print(f"Error: {e}")
            print("For further support please join the discord server: https://discord.gg/E6gkFRMGn2")
            app.destroy()
            input()
            quit()
            
    except Exception as e:
        print(f"An error occured:\n{e}")
        print("For further support please join the discord server: https://discord.gg/E6gkFRMGn2")
        app.destroy()
        input()
        quit()
    #app.destroy() # Was causeing an error when trying to close the app again after quitting
    quit()

app = tk.Tk()
app.geometry('500x225')
app.title("Aim Trainer by Bernso")
app.iconbitmap(os.path.join(Icon, "Dead.ico"))
app.config(bg="black")

start_button = tk.Button(app, text="Start", bg='black', fg='white', font=("bold", "25"),command=change_button)
start_button.pack(padx=10, pady=10, side="top")
start_button.place(relx=0.5, rely=0.5, anchor="center")

exit_button = tk.Button(app, text="EXIT", bg='black', fg='white',command=lambda: quitv2(SCORE))
exit_button.pack(padx=10, pady=10, side="bottom")


if __name__ == "__main__":
    try:
        print("Starting application...")
        app.mainloop()
    except Exception as e:
        print(f"An error occurred:\n{e}")
        print("For further support please join the discord server: https://discord.gg/E6gkFRMGn2")
        input()
        quit()  
    
    feedback()


else:
    print("How did you even do this?")
    extra = random.randint(25, 1000)
    for i in range(extra):
        os.system("cls")
        print(f"[{i} / {extra-1}]")
        