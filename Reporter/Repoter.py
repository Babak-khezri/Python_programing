from datetime import datetime
file = open(r'C:\Users\Babak\Desktop\Report.txt','a')
time = str(datetime.now()).split()
time[1] = time[1].split('.').pop(0) + '\n'
file.write("Date = " + "     Time = ".join(time))
file.close()
