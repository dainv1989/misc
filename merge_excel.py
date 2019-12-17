#
# pip packages  : pywin32
# reference     : stackoverflow question ID 44593705
#

from win32com.client import Dispatch
import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

if len(sys.argv) == 3:
    ftarget = dir_path + '\\' + sys.argv[1]
    finput = dir_path + '\\' + sys.argv[2]
else:
    print("invalid command format")
    quit()

xl = Dispatch("Excel.Application")
xl.Visible = False                  # do not make Excel be visible while processing

wb_target = xl.Workbooks.Open(Filename=ftarget)
wb_input = xl.Workbooks.Open(Filename=finput)

#ws1 = wb_input.Worksheets(2)
#ws1.Copy(Before=wb_target.Worksheets(1))
#print("sheet count " + str(wb_target.Worksheets.Count))

print("Found %d sheets in %s workbook" % (wb_input.Worksheets.Count, sys.argv[2]))
for i in range(1, wb_input.Worksheets.Count + 1):
    print(wb_input.Worksheets(i).Name)

print("Found %d sheets in %s workbook" % (wb_target.Worksheets.Count, sys.argv[1]))
for i in range(1, wb_target.Worksheets.Count + 1):
    print(wb_target.Worksheets(i).Name)

#wb_input.Worksheets("KPI").Select
#wb_input.Worksheets("KPI").Cells.Select
wb_input.Worksheets("KPI").Cells.Copy
#wb_target.Worksheets("Lap1").Select
wb_target.Worksheets("Lap1").Paste
#wb_target.Worksheets("Lap1").Paste
print("KPI -> Lap1-VMS done")


wb_target.Close(SaveChanges=True)
wb_input.Close(SaveChanges=False)
xl.Quit()