import smtplib
import RPi.GPIO as GPIO
import time,sched, datetime

schedule = sched.scheduler(time.time, time.sleep)

# Define GPIO Pin location
PIN_TRIGGER = 7
PIN_ECHO = 11

# Uncomment If Using Outlook
#SMTP_SERVER =  'smtp-mail.outlook.com'
SMTP_SERVER =  'smtp.gmail.com'

SMTP_PORT   = 587

# Enter Sender Email and Password
GMAIL_USERNAME = '[SENDER_EMAIL]'              # Sender Email Address
GMAIL_PASSWORD = '[SENDER_PASSWORD]'           # Email Address Password

# Function to compile and send the email
class emailer:
    def sendmail(self,recipient,subject,content):
        
        headers = ["From: "+GMAIL_USERNAME,
                   "Subject: "+subject,
                   "To: "+recipient,
                   "MIME-Version: 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()
        
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
        
        session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n"+ content)
        session.quit()
    
# Functon to recieve email details
def reciever(r_email,r_subject,r_content):
    sender = emailer()
    
    sendTo = r_email
    emailSubject = r_subject
    emailContent = r_content
    
    sender.sendmail(sendTo,emailSubject,emailContent)

# Function to loop and capture data every 0.1 seconds
def cont_run(sec):
    
    # Time needed to capture single data is 0.00001
    GPIO.output(PIN_TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    
    while GPIO.input(PIN_ECHO)==0:
        pulse_start_time = time.time()
        
    while GPIO.input(PIN_ECHO)==1:
        pulse_end_time = time.time()
        
    pulse_duration = pulse_end_time - pulse_start_time
    
    global distance
    distance = round(pulse_duration * 17150, 2)
    print("Distance: ", distance, " cm")
    
    # If the distance lower than 50cm will trigger the alarm
    if distance <= 50:
        record_data()
        reciever('[RECEIVER_EMAIL]',    # Reciever Email Address
                     'Alarm Triggered On Nearby Movement',         # Header of the email
                     'Timestamp: '+ cur_time + ", " + "Approx. Distance: " + str_dist + " cm")      # Content of the email

    else:
        pass
    
    # Looping the data capturing
    schedule.enter(0.1,1,cont_run,(sec,))

# Function to boot up the sensors
def start_up():
    print("Starting the Sensor")
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)

    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    print("Waiting for sensor to setup")
    time.sleep(2)
    print("Starting to Calculate")

# Function for record the timestamp and write to a file
def record_data():
    newtime = time.time()
    
    global cur_time
    cur_time = datetime.datetime.fromtimestamp(newtime).strftime('%Y-%m-%d %H:%M:%S')
    
    global str_dist
    str_dist = str(distance)
    
    f = open("Timestamp.txt","a")
    
    f.write(cur_time+"    "+"Approx. Distance: "+str_dist+" cm"+"\n")

    time.sleep(5)

# Read the file 
content_file = open("/home/pi/Desktop/Timestamp.txt", "r")
global file
for line in content_file:
    file = line
content_file.close()

start_up()
schedule.enter(0.1,1,cont_run,(schedule,))
schedule.run()