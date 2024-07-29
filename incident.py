class Security_incident:
    def __init__(self,incident_type,description):
        self.incident_type=incident_type
        self.description=description
    def __str__(self):
        return f"incident_type:{self.incident_type}\n description:{self.description} "
        
class report_incident:
    def __init__(self):
        self.incidents=[]
    def report(self,incident_type,description):
        incident=Security_incident(incident_type,description)
        self.incidents.append(incident)
        print("report added sucessfully")
        
    def show_report(self):
        if not  self.incidents:
            print("no reports")
        else:
            for idx,incident in enumerate(self.incidents,1):
                print(f'incident:{idx}\n {incident}')
                
def main():
    report=report_incident()
    print("report incident tool")
    while True:
        print("1.add report\n 2.show report \n3.exit")
        choice=input("Enter your choice")
        if choice=="1":
            incident_type=input("Enter the incident type")
            description=input("enter the description")
            report.report(incident_type,description)
        elif choice=="2":
            report.show_report()
        else:
             break

if __name__=="__main__":
    main()
        
