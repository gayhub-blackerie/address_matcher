#coding=utf-8
#2019_9_24
#created_by_blackerie
import sys,IPy
address_list=[]

def match(ip):
    print(offered_add(ip))
    with open("address_get.txt","w+") as f:
        address_list.append(offered_add(ip))
        for i in address_list:
            f.write(i+"\n")

def main():
    find_address()

def find_address():
    try:
        for i in open(sys.argv[1]):
            i=i.strip()
            if "http://" in i:
                i=i.replace("http://","")
            elif "https://" in i:
                i=i.replace("https","")        
            if ":" in i :
                ip=i.split(":")[0]   
                #print(ip) 
                #port=i.split(":")[1]
                match(ip)
            else:
                ip=i
                match(ip)              
    except Exception as e:
        print(str(e))           

########## assects ######
def offered_add(ip):
#192.168.
        if ip in IPy.IP('192.168.0.0-192.168.0.255'):
            return 'A区域'
        if ip in IPy.IP('192.168.1.0-192.168.1.255'):
            return 'B区域'
        if ip in IPy.IP('192.168.2.0-192.168.2.255'):
            return 'C区域'
        return ip+' is not in range'
    except Exception as e:
        print(str(e))
if __name__ == '__main__':
    main()