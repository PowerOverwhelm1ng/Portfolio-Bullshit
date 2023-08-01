from datetime import datetime
from playsound import playsound

def get_alarm_time():
    while True:
        alarm_time = input("Enter your alarm to be set (HH:MM:SS AM/PM): ")
        try:
            alarm_datetime = datetime.strptime(alarm_time, "%I:%M:%S %p")
            return alarm_datetime
        except ValueError:
            print("Invalid input format. Please enter the time in HH:MM:SS AM/PM format.")

def main():
    alarm_datetime = get_alarm_time()
    print("Setting alarm for", alarm_datetime.strftime("%I:%M:%S %p"), "...")
    
    mp3_path = r"C:\Users\tggal\OneDrive\Desktop\alarm.mp3"  # Absolute file path to the MP3
    
    while True:
        now = datetime.now()
        if now >= alarm_datetime:
            print("ALARM! DETECTIVE ARRIVING ON THE SCENE!")
            playsound(mp3_path)  # Use the variable containing the MP3 path here
            break
10:
if __name__ == "__main__":
    main()
