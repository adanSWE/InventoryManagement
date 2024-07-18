#Stocks Sorter:
#Removing an Item from the Inventory:
import os,csv
def remove():
    f = open('STOCKS.csv', 'r', newline = '')
    rdr = csv.reader(f)
    rem = input("Enter item code to remove the following items data: ")
    fnd = 0
    flist = []
    for rec in rdr:
        flist.append(rec) #appends each record(row) in the list 'flist'
    for rec in flist:
        if rem == rec[4]:
            fnd = 1
            flist.remove(rec)
            print('Item has been removed.')
    if fnd == 0:
        print("Item code is invalid!")

    file = open('STOCKS.csv', 'w', newline = '')
    wrtr = csv.writer(file)
    for ele in flist:
        wrtr.writerow(ele)
    file.close()

#Adding an Item to the Inventory:
def add():
    file = open('STOCKS.csv', 'r', newline = '')
    reader_object = csv.reader(file)
    category_code = int(input("Enter category code in which the item has to be appended in: "))
    class_code = int(input("Enter class code in which the item has to be appended in: "))
    file_list = []
    check1 = 0
    check2 = 0
    count = 1
    inum = 0
    sc = 0
    
    for record in reader_object:
        file_list.append(record)
    file_list.pop(0) #To remove the header row in the csv file
    
    for record in file_list:
        if category_code == int(record[0]) and category_code > 0:
            count += 1
            category = record[1]
            check1 = 1
            if class_code == int(record[2]) and class_code > 0:
                CL = record[3]
                check2 = 1
                inum += 1
                inum = str(inum)
                class_code = str(class_code)
                if len(inum) <  2:
                    #print('ok')
                    item_code = class_code+'00'+inum
                    item = input("Enter Item name: ")
                    quantity = int(input("Enter Quantity (DISCLAIMER: MUST BE POSITIVE): "))
                    if quantity < 0:
                        print("Quantity must be positive.")
                        break
                    price = input("Enter Price: ")
                    rec = [category_code, category, class_code, CL, item_code, item, quantity, price]
                    #print(rec)
                    if rec[0] == int(record[0]):
                        #print('w')
                        for record in file_list:
                            if int(record[2]) == int(rec[2]):
                                if int(record[4]) >= int(rec[4]):
                                    item_code = int(item_code)
                                    item_code += 1
                                    item_code = str(item_code)
                                    #print(item_code)
                                    rec = [category_code, category, class_code, CL, item_code, item, quantity, price]
                                    #print(rec)
                                else:
                                    print('ok')
                            
                    file_append = open('STOCKS.csv', 'a', newline = '')
                    rec = [category_code, category, class_code, CL, item_code, item, quantity, price]
                    wrtr = csv.writer(file_append)
                    wrtr.writerow(rec)
                    print("Record has successfully been appended")
                    
                    if item_code == record[4]:
                        print("Sorry This Item Code already exists")
                        break

                        
                if len(inum) == 2:
                    #print('ok')
                    item_code = class_code+'0'+inum
                    item = input("Enter Item name: ")
                    quantity = int(input("Enter Quantity: "))
                    if quantity < 0:
                        print("Quantity must be positive.")
                        break
                    price = input("Enter Price: ")
                    rec = [category_code, category, class_code, CL, item_code, item, quantity, price]
                    #print(rec)
                    if rec[0] == int(record[0]):
                        #print('w')
                        for record in file_list:
                            if int(record[2]) == int(rec[2]):
                                if int(record[4]) >= int(rec[4]):
                                    item_code = int(item_code)
                                    item_code += 1
                                    item_code = str(item_code)
                                    #print(item_code)
                                    rec = [category_code, category, class_code, CL, item_code, item, quantity, price]
                                    #print(rec)
                                else:
                                    print('ok')
                            
                    file_append = open('STOCKS.csv', 'a', newline = '')
                    rec = [category_code, category, class_code, CL, item_code, item, quantity, price]
                    wrtr = csv.writer(file_append)
                    wrtr.writerow(rec)
                    print("Record has successfully been appended")
                    
                    if item_code == record[4]:
                        print("Sorry This Item Code already exists")
                        break
                            
                if len(inum) > 2 and len(inum) <= 3:
                    #print('ok')
                    item_code = class_code+inum
                    item = input("Enter Item name: ")
                    quantity = int(input("Enter Quantity: "))
                    if quantity < 0:
                        print("Quantity must be positive.")
                        break
                    price = input("Enter Price: ")
                    rec = [category_code, category, class_code, CL, item_code, item, quantity, price]
                    #print(rec)
                    if rec[0] == int(record[0]):
                        #print('w')
                        for record in file_list:
                            if int(record[2]) == int(rec[2]):
                                if int(record[4]) >= int(rec[4]):
                                    item_code = int(item_code)
                                    item_code += 1
                                    item_code = str(item_code)
                                    #print(item_code)
                                    rec = [category_code, category, class_code, CL, item_code, item, quantity, price]
                                    #print(rec)
                                else:
                                    print('ok')
                            
                    file_append = open('STOCKS.csv', 'a', newline = '')
                    rec = [category_code, category, class_code, CL, item_code, item, quantity, price]
                    wrtr = csv.writer(file_append)
                    wrtr.writerow(rec)
                    print("Record has successfully been appended")
                    
                    if item_code == record[4]:
                        print("Sorry This Item Code already exists")
                        break
                    
                if len(inum) > 3:
                    print("Sorry Max Number of Item Code is XYZ999, where XYZ represent ClassCode")
                    

    if check1 == 0:
        print("Category has not been found, invalid category code")
    if check2 == 0:
        print("Class has not been found, invalid class code")
    

#Sorting the file after appending a row in the file:
def sort():
    import operator
    file = open('STOCKS.csv', 'r', newline = '')
    reader_object = csv.reader(file)
    temp_list = []
    file_list = []
    
    for rec in reader_object:
        temp_list.append(rec)
    header = temp_list.pop(0)
        
    
    sort = sorted(temp_list, key = operator.itemgetter(4)) #sorts each item by the 4th indexed value in the temp file: itemcode
#NOTE: itemgetter function from operator module fetches out the 4th indexed element
    for rec in sort:
        file_list.append(rec)
        
    file_append = open('STOCKS.csv', 'w', newline='')
    wrtr = csv.writer(file_append)
    wrtr.writerow(header)
    for rec in file_list:
        wrtr.writerow(rec)
        
#Generating a report of all items in excel:       
def stockReport():
    print("The report is generating...")
    os.startfile("stocks.csv") 

#Generating Category-Wise Report of all items:
def categoryReport():
    cat=input("Enter category code: ")
    f=open("STOCKS.csv")
    f.readline()
    rdr=csv.reader(f)
    f1=open("catreport.csv",'w',newline='')
    wrtr=csv.writer(f1)
    hdr="Category Code,Category,Class Code,Class,ItemCode,Item,Quantity (pieces),Price Per Piece (KWD),,\n"
    f1.write(hdr); print("The report is generating...")
    for rec in rdr:
        if rec[0].strip()==cat:
            wrtr.writerow(rec)
    f.close()
    f1.close()
    os.startfile("catreport.csv")  #To Generate the category report in MS-Excel. (or whatever is the default for opening csv files on the desktop)

#Generating Re-Order report:
def reorderReport():
    f=open("STOCKS.csv")
    f.readline()
    rdr=csv.reader(f)
    f1=open("reorderReport.csv",'w',newline='')
    wrtr=csv.writer(f1)
    hdr="Category Code,Category,Class Code,Class,ItemCode,Item,Quantity (pieces),Price Per Piece (KWD),,\n"
    f1.write(hdr); print('The report is generating...')
    for rec in rdr:
        print(rec)
        qty=rec[-4].strip()
        if qty.isdigit() and int(qty)<20:
            wrtr.writerow(rec)
    f.close()
    f1.close()
    os.startfile("reorderReport.csv")
    #To Generate the re-order report in MS-Excel.
    
menu = '''
-------------------------------------
1.) Add an Item to the Inventory.
2.) Remove an Item from the Inventory.
3.) Print Complete Stock Report.
4.) Print Stock Report (Category).
5.) Print Re-order Report.              
0.) Exit.                                            
-------------------------------------
'''

while True:
    print(menu)
    op = int(input("Choose an option (1/2/3/4/5/0): "))
    if op == 1:
        add()
        sort()
    elif op == 2:
        remove()
    elif op == 3:
        stockReport()
    elif op == 4:
        categoryReport()
    elif op == 5:
        reorderReport()
    elif op == 0:
        print('Exiting..')
        break
    


