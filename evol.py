
import random
"""
import tkinter as tk
root=tk.Tk()

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
            command=root.destroy)
        self.hiButton = tk.Button(self)
        self.hiButton["text"]=""
        self.hiButton["command"]=self.hi
        self.canv=tk.Canvas(self,background="#FFF",width=300,height=400)
        self.hiButton.grid(column=0,row=0)
        self.quitButton.grid(column=1,row=0)
        self.canv.grid(column=0,row=1,columnspan=2)
        
    def hi(self):
        self.canv.create_line(random.randrange(300),random.randrange(400),random.randrange(300),random.randrange(400))
                             
app = Application(master=root)
app.master.title('LALAL')
app.mainloop()
"""
class agent():
    def __init__(self,program,mutrate):
        self.p=program
        self.m=mutrate
    def clone(self):
        """returns a copy of the program"""
        return agent(list(self.p),float(self.m))
    def evaluate(self):
        """evaluates itself. current test is counting the number of trues."""
        count=0
        for b in self.p:
            if b:
                count+=1
        return count
    def mutate(self):
        for i in range(len(self.p)):
            if random.random()<self.m:#has a probability of mutrate
                self.p[i]=random.choice((True,False))#random mutation
        if random.random()<.5:
            self.m=self.m*1.25
        else:
            self.m=self.m*.8
def main():
    """evolutionary algorighm for optimizing programs"""
    l=30#length of the program
    N=100#number of agents per generation
    p=30#specifies how many of the worst are removed and how many of the best are cloned
    def randomagent():
        """generates a random program (list of true-falses) and random mutation rate and puts that in an agent"""
        p=[random.choice((True,False)) for  i in range(l)]#generates a random list of true-falses
        return agent(p,random.random())
    agents=[randomagent() for i in range(N)]#generates N random agents
    while True:#keyboard intterupt to break
        agents.sort(key=agent.evaluate)#for agents.evaluate, agents.evaluate(x) will do the same thing as x.evaluate
        print(agent.evaluate(agents[-1]),agent.evaluate(agents[0]),end="   ")
        for i in range(p):
            agents[i]=agents[-i-1].clone()#replaces the ith worst agent with a copy of the i+1th best agent
        for i in range(N):
            agents[i].mutate()

main()
