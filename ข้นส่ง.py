import random
print('------GHP ข้อมูลขนส่งประจำโรงพยาบาลราชวิถี-----')
print("วันจันทร์-พุธ-พฤหัสบดี พิมพ์ 1")
print('วันอังคาร-ศุกร์ พิมพ์ 2')
print('วันเสาร์-อาทิตย์-นักขัตฤกษ์ พิมพ์3')
day=int(input())
if day==1 or day==2:
    round=(random.randint(16,25))
    sum_st=0
    count_st=("=1")
    while True:
        if sum_st==(round-1):
            break
        elif sum_st!=round:
            sum_st+=int(1)
            count_st+=str("+1")

    
if day==1 or day==2:
    n1_store=(random.randint(80,140))
    m_vl=(random.randint(55,70))
    m_store=int(n1_store*m_vl/100)
    l_store=n1_store-m_store
    

if day==1:
    round_ws=(random.randint(15,17))
    count_ws=10
    point_ws=('=8+7+13+5+5+6+11+14+14+16')
    result_ws=point_ws
    while count_ws<round_ws:
        n1_ws=(random.randint(1,3))
        result_ws+=('+')
        result_ws+=str(n1_ws)
        count_ws+=1  
    n1_ws=(random.randint(260,280))
    ws_svl=(random.randint(35,55))
    ws_mvl=(random.randint(25,40))
    s_ws=int(n1_ws*ws_svl/100)
    m_ws=int(n1_ws*ws_mvl/100)
    l_ws=int(n1_ws-s_ws-m_ws)
    
elif day==2:
    round_ws=(random.randint(18,24))
    count_ws=10
    point_ws=('=8+7+13+5+5+6+11+14+14+16')
    result_ws=point_ws
    while count_ws<round_ws:
        n1_ws=(random.randint(1,3))
        result_ws+=('+')
        result_ws+=str(n1_ws)
        count_ws+=1
    n1_ws=(random.randint(290,320))
    ws_svl=(random.randint(35,55))
    ws_mvl=(random.randint(25,40))
    s_ws=int(n1_ws*ws_svl/100)
    m_ws=int(n1_ws*ws_mvl/100)
    l_ws=int(n1_ws-s_ws-m_ws)
     
elif day==3:
    round_ws=(random.randint(5,6))
    count_ws=0
    point_ws=('=')
    result_ws=point_ws
    while count_ws<round_ws:
        n1_ws=(random.randint(3,6))
        result_ws+=('+')
        if count_ws<1:
            result_ws=result_ws[:-1]        
        result_ws+=str(n1_ws)
        count_ws+=1
    n1_ws=(random.randint(140,165))
    ws_svl=(random.randint(35,55))
    ws_mvl=(random.randint(25,40))
    s_ws=int(n1_ws*ws_svl/100)
    m_ws=int(n1_ws*ws_mvl/100)
    l_ws=int(n1_ws-s_ws-m_ws)
       
 
if day==1 or day==2 or day==3:
    count=0
    result=str("")
    result2=str("=")
    while True:
        if count==12:
            break
        else:
            n1=str(random.randint(1,11))
            n2=str(random.randint(1,7))
            n3=str(random.randint(1,4))
            n4=str(random.randint(1,9))
            n5=str(random.randint(1,9))
            n6=str(random.randint(1,8))        
            result=("%s+%s+%s+%s+%s+%s+"%(n1,n2,n3,n4,n5,n6))
            result2+=str(result)
            count+=1  
    result2=result2[:-1]
    
if day==1 or day==2:
    roundcm=(random.randint(5,6))
    ncm=("")
    scm=("=")
    countcm=0
    while countcm<roundcm:
        ncm=str((random.randint(3,5)))
        scm+=ncm
        scm+='+'
        countcm+=1
    scm=scm[:-1]
elif day==3:
    roundcm=(random.randint(3,4))
    ncm=("")
    scm=("=")
    countcm=0
    while countcm<roundcm:
        ncm=str((random.randint(3,4)))
        scm+=ncm
        scm+='+'
        countcm+=1
    scm=scm[:-1]
    count_st=0
    n1_store=0
    m_store=0
    l_store=0
    round=0

print('-----งานเดินเบิกพิเศษคลังยา-----')
print(f'จำนวนรอบเบิกพิเศษ: {round}')    
print(f'จำนวนรอบเบิกพิเศษคลัง: \n{count_st}')
    
print("-----งานเดินยานิวออเดอร์-----")    
print(f'จำนวนรอบยานิว: \n{result2}')

print("-----งานน้ำเกลือ-----")
print(f'จำนวนรอบน้ำเกลือ: {round_ws}')
print(f'จำนวนจุดน้ำเกลือ: \n{result_ws}')
print(f'จำนวนลังน้ำเกลือทั้งหมด: {n1_ws}')
print(f"จำนวนลังไซส์S: {s_ws}")
print(f"จำนวนลังไซส์M: {m_ws}")
print(f"จำนวนลังไซส์L: {l_ws}") 

print("-----งานเดินยาคลัง-----")
print(f'จำนวนลังยาทั้งหมด: {n1_store}')
print(f'จำนวนลังไซส์M: {m_store}')
print(f'จำนวนลังไซส์L: {l_store}')

print('-----งานเดินยาเคมี-----')
print(f'จำนวนรอบเดินยาเคมี: {roundcm}')
print(f'จำนวนจุดยาเคมี: \n{scm}')
