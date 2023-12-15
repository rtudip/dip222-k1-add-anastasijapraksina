# 1.uzd

# import pandas
# with open("data.csv","r") as f:
#     next(f)

#     age=[]
#     reg = "Oman"
#     for line in f:
#         row=line.rstrip().split(",")
#         if row[4]==reg:
#             age.append(int(row[6]))
#     print(min(age))
# 2.uzd

# import pandas
# with open("data.csv","r") as f:
#     next(f)

#     ind=[]
#     reg = "Latvia"
#     for line in f:
#         row=line.rstrip().split(",")
#         if row[4]==reg:
#             ind.append(int(row[8]))
#     print(sum(ind))

# 3.uzd
# import pandas
# with open("data.csv","r") as f:
#     next(f)
#     count = []
#     reg = "Latvia"
#     ind ="Telecommunications"
#     for x in f:
#         x=x.rstrip().split(",")
#         if x[4] == reg and x[7]==ind:
#             count.append(x[8])
#     print(count)

# 4.uzd
# import pandas
# with open("data.csv","r") as f:
#     next(f)
#     url=[]
#     reg="Latvia"
#     for line in f:
#         row=line.rstrip().split(",")
#         if row[4]==reg:
#             url.append(row[3])
#     hpp="https://"
#     urlm=[]
#     for saite in url:
#         if hpp in saite:
#             urlm.append(saite)
#     print(len(urlm))

# 5.uzd
# import pandas
# with open("data.csv","r") as f:
#     next(f)
#     url=[]
#     reg="Latvia"
#     for line in f:
#         row=line.rstrip().split(",")
#         if row[4]==reg:
#             url.append(row[3])
#     hpp=".org"
#     urlm=[]
#     for saite in url:
#         if hpp in saite:
#             urlm.append(saite)
#     print(len(urlm))