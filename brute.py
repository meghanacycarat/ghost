from collections import defaultdict
import time

class BruteForce:
    def __init__(self,max_attempts,time_window):
        self.attempts= defaultdict(lambda:(0,0))
        self.max_attempts=max_attempts
        self.time_window=time_window

    def log(self,ip_address):
        current_time=time.time()
        for ip in list(self.attempts.keys()):
            if current_time - self.attempts[ip][0]  > self.time_window:
                del self.attempts[ip]

            last_time,count=self.attempts[ip_address]
            self.attempts[ip_address]=(current_time,count+1)

            if  self.attempts[ip_address][1] >= self.max_attempts:
                return True
        return False

def main():
    detector=BruteForce(max_attempts=5,time_window=10)
    test_ip={'192.168.1.1','192.168.1.1','192.168.1.1','192.168.1.1','192.168.1.1','192.168.1.1'}

    for ip in test_ip:
        print(f"Logging attempts from {ip}") 
        if detector.log(ip):
            print("Brute force detected from {ip}.too many attempts within {detector.time_window}seconds")
            break
    time.sleep(1)
    if not any(detector.log(ip) for ip in test_ip):
        print("No brute force detected")

if __name__=="__main__":
    main()                     
