try:
    import tkinter as tk
    import random
    import os
    import datetime
    import urllib.request
    import time
    import requests
    import sqlite3
    import uuid
    import sys
except ImportError:
    print("Please make sure all required libraries are installed.")
    print("For further support please join the discord server: https://discord.gg/E6gkFRMGn2")
    input()
    quit()
sys.set_int_max_str_digits(10000000)
#a = random.randint(12, 30)
#print("Starting main loading...\n")
#for o in range(1, a):
#    os.system("cls")
#    print(f"[{o} / {a-1}]")
#print("Completed main loading...\nSubloading...\n")

times_ran = 0
SCORE = 0
CHECKUP1 = 0
CHECKDOWN1 = 0
CHECKRIGHT1 = 0
CHECKLEFT1 = 0

FEEDBACK_DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1221533046746906705/UmI-FXnuaaGNppGfmYdA7fDeHMN2KUekp43K2vR1dGa6TJ7MDBVAJPpFmyd3QMMHLW9b"
ERROR_DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1221543200746111136/EJij3VCrHVxqwq-bSGwgSnWc8_oXNNP3tcFXcRHDzI62LHSZP5NviUDNv2txY63w-UnL"
CHEATING_DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1223226845097627698/y1su_IsgTtxzsSYDKm8rPnlev4IhVlTZC_p1DsC8ls8YzDcdR4BOVJs753Hy7-FEiyJS"
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
        print("Message failed to send, please report this. https://discord.gg/E6gkFRMGn2 (this link will never expire)")
        print(f"Error: {e}")
        errorReporting(e)
        input()
def startup(msg):
    try:
        payload = {
            "content": f"**{msg}** started the application."
        }
        requests.post(FEEDBACK_DISCORD_WEBHOOK_URL, json=payload)
        print("Discord webhook message sent.")
    except Exception as e:
        print("Message failed to send, please report this. https://discord.gg/E6gkFRMGn2 (this link will never expire)")
        print(f"Error: {e}")
        errorReporting(e)
        input()

def cheatingReporting(message):
    try:
        payload = {
            "content": f"**Cheater found:** (Aim Trainer) \n```{message}```"
        }
        requests.post(CHEATING_DISCORD_WEBHOOK_URL, json=payload)

        # Log Discord webhook message
        print(f"You found the cheat code, you are being reported.")
        print()
    except Exception as e:
        print("Message failed to send, please report this. https://discord.gg/E6gkFRMGn2 (this link will never expire)")
        print(f"Error: {e}")
        errorReporting(e)
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
        print("Message failed to send, please report this. https://discord.gg/E6gkFRMGn2 (this link will never expire)")
        print(f"Error: {e}")
        errorReporting(e)

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
    errorReporting(e)
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
    errorReporting(e)
    input()

db = "Database"
try:
    if os.path.exists(db):
        print("'Database' folder already exists")
    else:
        print("Creating 'Database' folder")
        os.makedirs(db)
        print("'Database' folder created")
except Exception as e:
    print(f"Error: {e}")
    errorReporting(e)
    input()

def get_user_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        if response.status_code == 200:
            return response.json()['ip']
        else:
            return None
    except requests.exceptions.RequestException:
        return None

# Check if the database file exists
if not os.path.exists('Database/userdata.db'):
    # If it doesn't exist and the user is you (based on IP address), create a new database
    print("You are authorized to create a new database.\nCreating a new database...")
    conn = sqlite3.connect('Database/userdata.db')
    c = conn.cursor()
    # Create a table to store user data
    c.execute('''CREATE TABLE IF NOT EXISTS users
                    (userid TEXT PRIMARY KEY, ip TEXT)''')
    conn.commit()
    conn.close()



# Connect to the database
conn = sqlite3.connect('Database/userdata.db')
c = conn.cursor()

# Check if the user has a userid already
c.execute("PRAGMA table_info(users)")
columns = c.fetchall()
column_names = [column[1] for column in columns]
if 'ip' not in column_names:
    # If the 'ip' column doesn't exist, add it
    c.execute('''ALTER TABLE users
                 ADD COLUMN ip TEXT''')
    conn.commit()

# Check if the user has a userid already
c.execute("SELECT userid FROM users WHERE ip=?", (get_user_ip(),))


result = c.fetchone()


if result:
    # If the user already has a userid, retrieve it
    userid = result[0]
else:
    # If not, generate a new userid and insert it into the database
    userid = str(uuid.uuid4())
    # Insert userid along with the user's IP address
    c.execute("INSERT INTO users (userid, ip) VALUES (?, ?)", (userid, get_user_ip()))
    conn.commit()
USER_IP = get_user_ip()
startup(userid)
startup(USER_IP)

bans = ['']
if userid in bans:
    errorReporting(f"{userid} is banned and has tried to use the application.")
    os.system('cls')
    print("You have been banned from using the application.")
    print("Please contact the owner of the application to get unbanned. https://discord.gg/E6gkFRMGn2")
    input()
    os.system('cls')
    print("Application closed.")
    time.sleep(1)
    sys.exit()
else:
    print("\nGone through ban proccess. \nYou are authorized to use the application.")


# Close the connection
conn.close()

# Print the userid and IP address
print(f"\nYour userid is: {userid}\n")
#print("Your IP address is:", get_user_ip())


def download_file(url, save_path):
    try:
        print("Downloading ICO...")
        urllib.request.urlretrieve(url, save_path)
        print(f"File downloaded successfully to: {save_path}")
    except Exception as e:
        errorReporting(e)
        print(f"An error occurred while downloading the file: {e}")

ico_url = "https://raw.githubusercontent.com/Bernso/Icons/main/Dead.ico"
ico_url2 = "https://raw.githubusercontent.com/Bernso/Icons/main/Black.ico"
save_path = os.path.join(Icon, "Dead.ico")  # Full file path including directory
save_path2 = os.path.join(Icon, "Black.ico")  # Full file path including directory
download_file(ico_url, save_path)
download_file(ico_url2, save_path2)

def feedback():
    try:
        user_feedback = input("\nIf you would like any extra support, join the discord: https://discord.gg/E6gkFRMGn2 \nAny feedback? (if you do please type it here)\n")
            
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
        errorReporting(e)
        input()
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
    global CHECKUP1, CHECKDOWN1, CHECKRIGHT1, CHECKLEFT1, SCORE, CHEAT_CODE
    summary = CHECKUP1 + CHECKDOWN1 + CHECKRIGHT1 + CHECKLEFT1
    if summary >= 8:
        SCORE *= random.randint(10, 200000000000000000000000)
        print(f"Your score is now: {SCORE}")
        CHEAT_CODE = "ACTIVE"
    else:
        print("Your have not met the requirements.")
    
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
            errorReporting(e)
            input()
            quit()
    else:
        print("How did you even do this?")
        print("For further support please join the discord server: https://discord.gg/E6gkFRMGn2")
        quit()

def quitv2(SCORE):
    global CHEAT_CODE
    try:
        if SCORE == 1:
            print(f"\nYou scored ONE SINGULAR POINT!\n")
        elif SCORE <= 0:
            print("\nBros aim is terrible 💀")
        elif CHEAT_CODE == "ACTIVE":
            print("Bro really found the cheat code lol")
            cheatingReporting("Someone found the cheat code, they scored: " + str(SCORE) + " points")
        elif SCORE >= 10000:
            print(f"\nBro is training to be a pro")
            cheatingReporting("Someone found the cheat code, they scored: " + str(SCORE) + " points")
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

app = tk.Tk()
app.geometry('500x225')
app.title("Aim Trainer by Bernso")
app.iconbitmap(os.path.join(Icon, "Dead.ico"))
app.config(bg="black")

start_button = tk.Button(app, text="Start", bg='green', bd=0, fg='white', font=("bold", "25"),command=change_button)
start_button.pack(padx=10, pady=10, side="top")
start_button.place(relx=0.5, rely=0.5, anchor="center")

exit_button = tk.Button(app, text="EXIT", bg='black', fg='white',command=lambda: quitv2(SCORE))
exit_button.pack(padx=10, pady=10, side="bottom")

# Function to get user IP address

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
    extra = random.randint(250, 1000)
    for i in range(extra):
        os.system("cls")
        print(f"[{i} / {extra-1}]")
    
