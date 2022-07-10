import torch
import datetime


def block_creat(a):
    block=[]

    a2 = torch.flip(a, dims=[0])
    a3=torch.flip(a, dims=[1])
    a4=torch.flip(a, dims=[0,1])
    a5=a.transpose(0,1)
    a6=torch.flip(a.transpose(0,1), dims=[0])
    a7=torch.flip(a.transpose(0,1), dims=[1])
    a8=torch.flip(a.transpose(0,1), dims=[0,1])
    blockin=[a,a2,a3,a4,a5,a6,a7,a8]
    for additem in blockin:
        addFlag = True
        for item in block:
            # print(tableaddAB.equal(tableaddAB))
            if additem.equal(item):
                addFlag = False
                break
        if addFlag:
            block.append(additem)
    return block


def table_extent():
    extenttable=torch.ones(9,8)
    extenttable[1:8,1:7]=0
    return extenttable


#初始化棋盘
def table_ini():
    table=torch.zeros(8,7)
    table[7,0:4]=1
    table[0:2,6]=1
    #选择月日星期
    table[0,4]=1
    table[5,6]=1
    table[7,6]=1
    return table


def withhole(tableTest,row,col):
    for i in range(9 - row):
        for j in range(8 - col):
            if torch.sum(tableTest[i + 1:i + row + 1, j + 1:j + col + 1]) < (row * col):
                wall = torch.sum(tableTest[i:i + row + 2, j:j + col + 2]) - torch.sum(
                    tableTest[i + 1:i + row + 1, j + 1:j + col + 1]) - tableTest[i, j] - tableTest[i, j + col + 1] - \
                       tableTest[i + row + 1, j] - tableTest[i + row + 1, j + col + 1]
                if wall>(row*2+col*2)-1:
                    return True
    return False


def usefull_table(tablein):
    tableTest=torch.ones(10,9)
    tableTest[1:9, 1:8] = tablein
    #判断是否有一个的封闭区间
    # print(tablein)
    row = 1
    col = 1
    if withhole(tableTest,row,col):
        return False
    row = 2
    col = 1
    if withhole(tableTest,row,col):
        return False
    row = 1
    col = 2
    if withhole(tableTest,row,col):
        return False
    row = 1
    col = 3
    if withhole(tableTest,row,col):
        return False
    row = 3
    col = 1
    if withhole(tableTest,row,col):
        return False
    row = 2
    col = 2
    if withhole(tableTest,row,col):
        return False
    '''
    row = 2
    col = 3
    for i in range(9 - row):
        for j in range(8 - col):
            wall = torch.sum(tableTest[i:i + row + 2, j:j + col + 2]) - torch.sum(
                tableTest[i + 1:i + row + 1, j + 1:j + col + 1]) - tableTest[i, j] - tableTest[i, j + col + 1] - \
                   tableTest[i + row + 1, j] - tableTest[i + row + 1, j + col + 1]
            if wall > (row * 2 + col * 2) - 1:
                if torch.sum(tableTest[i + 1:i + row + 1, j + 1:j + col + 1]) == 0 or (torch.sum(tableTest[i + 1:i + row + 1, j + 1:j + col + 1]) >2 and torch.sum(tableTest[i + 1:i + row + 1, j + 1:j + col + 1]) <6):
                    return False
    row = 3
    col = 2
    for i in range(9 - row):
        for j in range(8 - col):
            wall = torch.sum(tableTest[i:i + row + 2, j:j + col + 2]) - torch.sum(
                tableTest[i + 1:i + row + 1, j + 1:j + col + 1]) - tableTest[i, j] - tableTest[i, j + col + 1] - \
                   tableTest[i + row + 1, j] - tableTest[i + row + 1, j + col + 1]
            if wall > (row * 2 + col * 2) - 1:
                if (torch.sum(tableTest[i + 1:i + row + 1, j + 1:j + col + 1]) == 0) or ((torch.sum(tableTest[i + 1:i + row + 1, j + 1:j + col + 1])) >2 and (torch.sum(tableTest[i + 1:i + row + 1, j + 1:j + col + 1]) <6)):
                    return False
    '''
    # row = 3
    # col = 3
    # for i in range(9 - row):
    #     for j in range(8 - col):
    #         if (torch.sum(tableTest[i + 1:i + row + 1, j + 1:j + col + 1]) != 4) and (
    #                 torch.sum(tableTest[i + 1:i + row + 1, j + 1:j + col + 1]) != 9) and (torch.sum(tableTest[i + 1:i + row + 1, j + 1:j + col + 1]) != 5):
    #             wall = torch.sum(tableTest[i:i + row + 2, j:j + col + 2]) - torch.sum(
    #                 tableTest[i + 1:i + row + 1, j + 1:j + col + 1]) - tableTest[i, j] - tableTest[i, j + col + 1] - \
    #                    tableTest[i + row + 1, j] - tableTest[i + row + 1, j + col + 1]
    #             if wall > (row * 2 + col * 2) - 1:
    #                 # print('执行33 空洞0，', tableTest,tableTest[i + 1:i + row + 1, j + 1:j + col + 1])
    #                 return False
    '''
    row = 4
    col = 4
    for i in range(9 - row):
        for j in range(8 - col):
            wall = torch.sum(tableTest[i:i + row + 2, j:j + col + 2]) - torch.sum(
                tableTest[i + 1:i + row + 1, j + 1:j + col + 1]) - tableTest[i, j] - tableTest[i, j + col + 1] - \
                    tableTest[i + row + 1, j] - tableTest[i + row + 1, j + col + 1]
            if wall > (row * 2 + col * 2) - 1:
                if torch.sum(tableTest[i + 1:i + row + 1, j + 1:j + col + 1]) == 0:
                    print('执行4 4空洞0，',tableTest)
                    return False
                    
    row = 4
    col = 5
    for i in range(9 - row):
        for j in range(8 - col):
            wall = torch.sum(tableTest[i:i + row + 2, j:j + col + 2]) - torch.sum(
                tableTest[i + 1:i + row + 1, j + 1:j + col + 1]) - tableTest[i, j] - tableTest[i, j + col + 1] - \
                   tableTest[i + row + 1, j] - tableTest[i + row + 1, j + col + 1]
            if wall > (row * 2 + col * 2) - 1:
                if torch.sum(tableTest[i + 1:i + row + 1, j + 1:j + col + 1]) == 0:
                    print('执行4 5空洞',tableTest)
                    return False
    row = 5
    col = 4
    for i in range(9 - row):
        for j in range(8 - col):
            wall = torch.sum(tableTest[i:i + row + 2, j:j + col + 2]) - torch.sum(
                tableTest[i + 1:i + row + 1, j + 1:j + col + 1]) - tableTest[i, j] - tableTest[i, j + col + 1] - \
                   tableTest[i + row + 1, j] - tableTest[i + row + 1, j + col + 1]
            if wall > (row * 2 + col * 2) - 1:
                if torch.sum(tableTest[i + 1:i + row + 1, j + 1:j + col + 1]) == 0:
                    print('执行4 5空洞',tableTest)
                    return False
    '''
    return True


def tableupdate(table_in,block,i_in,j_in):
    i=0
    j=0
    i=i_in
    j=j_in
    addblock=torch.zeros(block.shape)
    addblock=block
    table_out=torch.zeros(8,7)
    table_out[:,:]=table_in[:,:]
    # print(addblock.shape,i+addblock.shape[0],j+addblock.shape[1],i,j)
    # print(table.shape,table_out[0:2,4:].shape,block.shape)
    row=i+addblock.shape[0]
    col=j+addblock.shape[1]
    table_out[i:row,j:col]=table_out[i:row,j:col]+addblock
    # print(table_out-table_in)
    return table_out


def Creatblocklist(block):
    blocklist=[]
    for singleblock in block:
        for i in range(8 - singleblock.shape[0] + 1):
            for j in range(7 - singleblock.shape[1] + 1):
                tableout=tableupdate(table000, singleblock, i, j)
                if torch.max(tableout)>1:
                    continue
                else:
                    if usefull_table(tableout):
                        blocklist.append(tableout)
    return blocklist


starttime=datetime.datetime.now()
print(datetime.datetime.now())
table000=table_ini()
bigtable000=table_extent()
a1=torch.tensor([[1,0,0],[1,0,0],[1,1,1]])
block1=block_creat(a1)
# print(len(block1))


a2=torch.tensor([[1,1,1],[1,0,1]]) #5
block2=block_creat(a2)
# print(len(block2))

a3=torch.tensor([[1,1,1],[1,1,0]]) #5
block3=block_creat(a3)
# print(len(block3))

a4=torch.tensor([[1,1,1],[0,1,0],[0,1,0]]) #5
block4=block_creat(a4)
# print(len(block4))


a5=torch.tensor([[0,0,1,1],[1,1,1,0]]) #5
block5=block_creat(a5)
# print(len(block5))

a6=torch.tensor([[0,1,1],[0,1,0],[1,1,0]]) #5
block6=block_creat(a6)
# print(len(block6))


a7=torch.tensor([[1,1,1,1],[0,0,0,1]]) #5
block7=block_creat(a7)
# print(len(block7))

a8=torch.tensor([[1,1,1,1]]) #4
block8=block_creat(a8)
# print(len(block8))

a9=torch.tensor([[1,0],[1,0],[1,1]]) #4
block9=block_creat(a9)
# print(len(block9))

a10=torch.tensor([[1,1,0],[0,1,1]]) #4
block10=block_creat(a10)
# print(len(block10))
print('各种翻转创建成功')

blocklist1=Creatblocklist(block1) #76   63
print('拼图块可以放的可能性',len(blocklist1))
blocklist2=Creatblocklist(block2)#89  67
print('拼图块可以放的可能性',len(blocklist2))
blocklist3=Creatblocklist(block3)#186  157
print('拼图块可以放的可能性',len(blocklist3))
blocklist4=Creatblocklist(block4)#80  61
print('拼图块可以放的可能性',len(blocklist4))
blocklist5=Creatblocklist(block5)#154  122
print('拼图块可以放的可能性',len(blocklist5))
blocklist6=Creatblocklist(block6)#80  63
print('拼图块可以放的可能性',len(blocklist6))
blocklist7=Creatblocklist(block7)#148  128
print('拼图块可以放的可能性',len(blocklist7))
blocklist8=Creatblocklist(block8)#43  42
print('拼图块可以放的可能性',len(blocklist8))
blocklist9=Creatblocklist(block9)#194 170
print('拼图块可以放的可能性',len(blocklist9))
blocklist10=Creatblocklist(block10)#100
print('拼图块可以放的可能性',len(blocklist10))

print('完成blocklist的创建')


iterate=1
a=1
Stopsignal=False
for item1 in blocklist1:
    iterate=iterate+1
    # a=a+1
    # print('迭代1',a/63)
    if Stopsignal:
        break
    for item2 in blocklist2:
        if Stopsignal:
            break
        print(iterate)
        iterate = iterate + 1
        # print('迭代1')
        tableadd = item1 + item2 - table000
        if torch.max(tableadd)>1:
            continue
        # if usefull_table(tableadd) == False:
        #     continue
        for item3 in blocklist3:
            if Stopsignal:
                break
            iterate = iterate + 1
            tableadd = item1 + item2 + item3 - table000 * 2
            if torch.max(tableadd) > 1:
                continue
            if usefull_table(tableadd) == False:
                continue
            for item4 in blocklist4:
                if Stopsignal:
                    break
                iterate = iterate + 1
                tableadd = item1 + item2 + item3 + item4 - table000 * 3
                if torch.max(tableadd) > 1:
                    continue
                if usefull_table(tableadd) == False:
                    continue
                for item5 in blocklist5:
                    if Stopsignal:
                        break
                    iterate = iterate + 1
                    tableadd = item1 + item2 + item3 + item4 + item5 - table000 * 4
                    if torch.max(tableadd) > 1:
                        continue
                    if usefull_table(tableadd) == False:
                        continue
                    for item6 in blocklist6:
                        if Stopsignal:
                            break
                        iterate = iterate + 1
                        tableadd = item1 + item2 + item3 + item4 + item5 + item6 - table000 * 5
                        if torch.max(tableadd) > 1:
                            continue
                        if usefull_table(tableadd) == False:
                            continue
                        for item7 in blocklist7:
                            if Stopsignal:
                                break
                            iterate = iterate + 1
                            tableadd = item1 + item2 + item3 + item4 + item5 + item6 + item7 - table000 * 6
                            if torch.max(tableadd) > 1:
                                continue
                            if usefull_table(tableadd) == False:
                                continue
                            for item8 in blocklist8:
                                if Stopsignal:
                                    break
                                iterate = iterate + 1
                                tableadd = item1 + item2 + item3 + item4 + item5 + item6 + item7 + item8 - table000 * 7
                                if torch.max(tableadd) > 1:
                                    continue
                                if usefull_table(tableadd) == False:
                                    continue
                                for item9 in blocklist9:
                                    if Stopsignal:
                                        break
                                    iterate = iterate + 1
                                    tableadd = item1 + item2 + item3 + item4 + item5 + item6 + item7 + item8 + item9 - table000 * 8
                                    if torch.max(tableadd) > 1:
                                        continue
                                    if usefull_table(tableadd) == False:
                                        continue
                                    for item10 in blocklist10:
                                        iterate = iterate + 1
                                        tableadd = item1 + item2 + item3 + item4 + item5 + item6 + item7 + item8 + item9 + item10 - table000 * 9
                                        if torch.max(tableadd) > 1:
                                            continue
                                        if usefull_table(tableadd) == False:
                                            continue
                                        else:
                                            list = [item1, item2, item3, item4, item5, item6, item7, item8, item9,
                                                    item10]
                                            num = 1
                                            print('最终结果：')
                                            for it in list:
                                                print((it - table000) * num)
                                                num = num + 1
                                            Stopsignal = True
                                            break


endtime = datetime.datetime.now()
print(datetime.datetime.now())
print('程序运行结束,一共消耗时间：', endtime - starttime)