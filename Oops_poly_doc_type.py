class ide: 
    def execute(self): 
        print("Our programm is executing.") 
    def run(self): 
        print("Execute successfuly.") 
    def compile(self): 
        print("Compilation has been successfully completed.") 
class vscode: 
    def output(self,other): 
        other.execute()
        other.run()
        other.compile() 
v1 = vscode() 
e2 = ide() 
v1.output(e2)  


