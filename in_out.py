from pywinauto import Application
import datetime
import pandas as pd
import sys
sys.path.append('C:/Users/sauds/Desktop/my_project')
from capture import *
from visual import *
import time
import csv
import atexit

# This list is storing data send by arduino sensor
lines = []

#Adding something to txt file to avoid aeeor
with open('C:/Users/sauds/Desktop/my_project/sensor_data.txt', 'w') as file:
    # Write text to the file
    file.write("Start")

# This code is for opening the CoolTerm App to connect with arduino
app = Application(backend="uia").start('C:/Users/sauds/Desktop/my_project/CoolTermWin64Bit/CoolTerm')
# Wait for the app to launch and become responsive
app.wait_cpu_usage_lower(threshold=5, timeout=30)
# Get a reference to the main window
main_window = app.top_window()
# Click on the Connect Button
button = main_window.child_window(title="Connect", control_type="Button")
button.click()

main_window.child_window(title="Connection", control_type="MenuItem").click_input()
main_window.child_window(title="Capture to Text/Binary File", control_type="MenuItem").click_input()







# This minimize the CoolTerm Window
input("Start the connection and enter any key to proceed")


# This function is Loading all the images present in Images folder
Function1()


pre_count =0
while 1:
    
    
    count =0
    Access = ''
    #count number of rows of the txt file
    with open('C:/Users/sauds/Desktop/my_project/sensor_data.txt', 'r') as file:
        for line in file:
           count += 1

    #if the count is greater than previous count then read data from the file
    if count > pre_count:
        with open('C:/Users/sauds/Desktop/my_project/sensor_data.txt', 'r') as file:
            lines = file.readlines()
        Access = lines[-1].strip()
        pre_count = count
        count =0
    

    if Access == 'Entry':

        name, reg, batch, faculty = Function2()
        #current date and time in normal format
        Date = datetime.date.today()
        Date = Date.strftime("%d/%m/%Y")
        Time = datetime.datetime.now().time()
        Time = Time.strftime("%I:%M %p")

        if name != "\\\\\\\\Unknown////////":
            new_row = {'Name': name, 'Reg Number': reg, 'Time IN': Time, 'Date IN': Date,'Time OUT': 'NA', 'Date OUT': 'NA', 'Batch': batch, 'Faculty': faculty}
            #data2 = pd.concat([data2, pd.DataFrame([new_row])], ignore_index=True)

            # Open the CSV file in append mode
            with open('C:/Users/sauds/Desktop/my_project/Students_Data.csv', mode='a', newline='') as file:
                # Define the CSV fieldnames
            
                fieldnames = ['Name', 'Reg Number', 'Time IN', 'Date IN', 'Time OUT', 'Date OUT', 'Batch', 'Faculty']
    
                # Create a DictWriter object
                writer = csv.DictWriter(file, fieldnames=fieldnames)
    
                # Write the header row if the file is empty
                if file.tell() == 0:
                    writer.writeheader()
    
                # Write the new row to the file
                writer.writerow(new_row)
            
        
    elif Access == 'Exit':

        name, reg, batch, faculty = Function3()
        #current date and time in normal format
        Date = datetime.date.today()
        Date = Date.strftime("%d/%m/%Y")
        Time = datetime.datetime.now().time()
        Time = Time.strftime("%I:%M %p")

        if name != "\\\\\\\\Unknown////////":
            new_row = {'Name': name, 'Reg Number': reg, 'Time IN': 'NA', 'Date IN': 'NA','Time OUT': Time, 'Date OUT': Date, 'Batch': batch, 'Faculty': faculty}
            #data2 = pd.concat([data2, pd.DataFrame([new_row])], ignore_index=True)
    

            # Open the CSV file in append mode
            with open('C:/Users/sauds/Desktop/my_project/Students_Data.csv', mode='a', newline='') as file:
                # Define the CSV fieldnames
            
                fieldnames = ['Name', 'Reg Number', 'Time IN', 'Date IN', 'Time OUT', 'Date OUT', 'Batch', 'Faculty']
    
                # Create a DictWriter object
                writer = csv.DictWriter(file, fieldnames=fieldnames)
    
                # Write the header row if the file is empty
                if file.tell() == 0:
                    writer.writeheader()
    
                # Write the new row to the file
                writer.writerow(new_row)
    elif Access == "Terminate":
        app.kill()
        time.sleep(.5)
        with open('C:/Users/sauds/Desktop/my_project/sensor_data.txt', 'r+') as file:
            file.truncate(0)
        cap.release()
        cap2.release()
        sys.exit()
            


    else:
        continue
    visua()