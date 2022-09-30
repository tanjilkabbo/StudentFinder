from googlesheet.connection import Connection

work_sheet = Connection().connect_worksheet("BanglaStudent")

group_list = work_sheet.col_values(1)
# print(group_list)

from datetime import datetime

now = datetime.now()
print(now)
print(datetime.now().timestamp())


import time

unixtime = int(time.time())
print(unixtime)
# Print with local time
print(datetime.fromtimestamp(unixtime).strftime('%Y-%m-%d %H:%M:%S'))

day_early = 60*60*24
print(day_early)

day_early_time = unixtime - day_early
print(day_early_time)

print(datetime.fromtimestamp(day_early_time).strftime('%Y-%m-%d %H:%M:%S'))


print(input("stop :"))

for i in range(len(group_list)):
    # print(len(group_list))
    print(i)
    sell_Value = work_sheet.row_values(i+1)
    print(sell_Value)
    work_sheet.update_cell(i+1, 3, 2)
