import pandas as pd
import numpy as np
import matplotlib.pyplot as plt





#The Code is able to show real time visualizatio
def visua():
    data = pd.read_csv('C:/Users/sauds/Desktop/my_project/Students_Data.csv')
    data_frame = pd.DataFrame(data, columns=['Name', 'Reg Number', 'Time IN', 'Date IN', 'Time OUT', 'Date OUT', 'Batch', 'Faculty'])
    count = data_frame.groupby(['Name', 'Reg Number']).size().reset_index(name='Count')
    plt.xlabel('Name of Students',weight='bold')
    plt.ylabel('Number of Entries and exit',weight='bold')
    plt.title('Line Graph',weight='bold')
    plt.bar(count['Name'],count['Count'],color = 'red')
    plt.show()
    plt.close()


