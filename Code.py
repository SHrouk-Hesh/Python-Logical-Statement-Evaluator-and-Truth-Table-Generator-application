"""Team Members:
Shrouk Hesham, ID:19106271 """
import os
import itertools
import sys
def POneQuestionOne():
    import itertools
    import sys
    def menu():
        print ("Python Logical Statment evaluator and Truth Table Generator")
        print ("*****************************************************")
        print ("1. View the instructions for use.")
        print ("2. Create a Truth Table")
        print ("3. Exit!")
        choice = input ("Please select your option >> ")
        if choice=="1":
            instructions ()
        elif choice=="2":
            truth_table ()
        elif choice =="3":
            print ("Program Terminated!")
            sys.exit()
        else:
            print ("That is an invalid option! ")
            menu()
    def instructions ():
        print ("****************************************************")
        print ("Welcome to the Truth Table Generator. This app will allow you\n\to evaluate any logical statement with up to FIVE inputs (a,b, c,d,e). The \nuser can specify the number of inputs then write a logical statement in PYTHON \n\and the app will, for each combination of input, evalua te if the statement returns \n\TRUE Or FALSE. ")
        print ("EXAMPLE OF STATEMENTS AND HOW TO WRITE THEM IN PYTHON*******************************")
        print ("A AND B should be written as 'a and b'")
        print ("A AND B (NOT C)-'a and b and (not c)")
        print (" (A OR (NOT B)) AND (NOT c)-(a or (not b) ) and (not c)")
        print ("All input is converted to lower-case. Do not use marks! ")
        print ("Limitations of use***********************")
        print ("1. The app will not allow reference to inputs that have not been created i.e. ")
        print ("if you have selected 3 inputs and you refer to 'd' in your logical statement. ")
        print ("2. Ensure correct use of parentheses (inner statements are evaluated first) . ")
        print ("3. The app is limi ted to 5 inputs. ")
        print ("4.The app will print the evaluation of the logical statement in the next. ")
        print ("5. If your statement cannot be evaluated, check syntax and use of bracke ts. ")
        Mymenu=input ("Press enter to return to the menu >>")
        menu ()
       
    def truth_table ():
        while True:
            try:
                inps=int (input ("Please enter the number of inputs you want 1 -5 >>» "))
                if inps <1 or inps>5:
                    print ("1 input minimum,5 max")
                else:
                    break
            except:
                ValueError
                print ("You must input a number between 1 and 5")
        truths = list (itertools .product ([False, True], repeat=inps) )
        statement = input ("Please input the logical statement e.g. (a and b) not a >>»")
        statement = statement.lower()
        print("A AND B OR C")
        print("A\t\tB\t\tC\t\tD\t\tF")
        print("-"*20*inps)
       
        for item in truths:
            pos=0
            if inps== 1:
                a=item[0]
            elif inps ==2:
                a,b=item[0],item[1]
            elif inps==3:
                a,b,c=item[0],item [1],item[2]
            elif inps==4:
                a,b,c,d=item[0],item [1],item[2],item[3]
            elif inps==5:
                a,b,c,d,e=item[0],item [1],item[2],item[3],item[4]
                pos=0
            while pos <inps:
                print(item [pos],end= "\t\t")
                pos+=1
            try:
                truth= (eval(statement))
                print (truth)
            except:  
                print ("Unable to evaluate. Check statement")
        Mymenu=input("Press enter to return to the menu >>")
        menu()
    menu()
def PTwoQuestionOne():
    # Insert the first proposition in the first line, the second proposition in the second line and insert the logical connective in the third line - 1 to conjunction, 2 to disjunction, 3 to Implication, 3 to Biconditional, 4 to Exclusive Or.
    P=0
    Q=0
    prop1 = str(input("Insert the first proposition: \n"))
    prop2 = str(input("Insert the second proposition: \n"))
    condition= (eval(input("Do you wwant to not p or not q (True\False)  : \n ")))
    if condition== False:
        fun = int(input("Insert the logical connective p(1 to conjunction, 2 to disjunction, 3 to Implication, 3 to Biconditional, 4 to Exclusive Or): \n"))
        if (fun) == 1:
            print ("\nFirst proposition (P): ",prop1,"\nLogical Connective Symbol: ^\nSecond proposition (Q): ", prop2,"\nCompound proposition: P^Q\nIn this case, the compound proposition will be TRUE only if both simple propositions are true, according to the truth table below.\n\n  Truth Table\n| P | Q | P^Q|\n|---|---|----|\n| T | T | T  |\n|---|---|----|\n| T | F | F  |\n|---|---|----|\n| F | T | F  |\n|---|---|----|\n| F | F | F  |")
        elif (fun) == 2:
            print ("\nFirst proposition (P): ",prop1,"\nLogical Connective Symbol: v\nSecond proposition (Q): ", prop2,"\nCompound proposition: PvQ\nIn this case, the compound proposition will be FALSE only if both simple propositions are false, according to the truth table below.\n\n  Truth Table\n| P | Q | PvQ|\n|---|---|----|\n| T | T | T  |\n|---|---|----|\n| T | F | T  |\n|---|---|----|\n| F | T | T  |\n|---|---|----|\n| F | F | F  |")
        elif (fun) == 3:
            print ("\nFirst proposition (P): ",prop1,"\nLogical Connective Symbol: -> \nSecond proposition (Q): ", prop2,"\nCompound proposition: P->Q\nIn this case, the compound proposition will only be FALSE if the first proposition are true and the second are false, as the truth table below.\n\n  Truth Table\n| P | Q |P->Q |\n|---|---|-----|\n| T | T | T   |\n|---|---|-----|\n| T | F | F   |\n|---|---|-----|\n| F | T | T   |\n|---|---|-----|\n| F | F | T   |")
        elif (fun) == 4:
            print ("\nFirst proposition (P): ",prop1,"\nLogical Connective Symbol: <->\nSecond proposition (Q): ", prop2,"\nCompound proposition: <->Q\nIn this case, the compound proposition will be TRUE only if both propositions have the same logical value, according to the truth table below.\n\n  Truth Table\n| P | Q |P<->Q|\n|---|---|----|\n| T | T | T  |\n|---|---|----|\n| T | F | F  |\n|---|---|----|\n| F | T | F  |\n|---|---|----|\n| F | F | T  |")
        elif (fun) == 5:
            print ("\nFirst proposition (P): ",prop1,"\nLogical Connective Symbol: xor\nSecond proposition (Q): ", prop2,"\nCompound proposition: P xor Q\nIn this case, the compound proposition will only be FALSE if the propositions have the same logical value, according to the truth table below.\n\n  Truth Table\n| P | Q |PxorQ|\n|---|---|----|\n| T | T | F  |\n|---|---|----|\n| T | F | T  |\n|---|---|----|\n| F | T | T  |\n|---|---|----|\n| F | F | F  |")
    elif condition== True:
        choice= (eval(input(" please Enter your choice (1. ~P or 2. ~Q) in the form of '1' or '2' :")))
        if choice == "1":
            fun = int(input("Insert the logical connective p(1 to conjunction, 2 to disjunction, 3 to Implication, 3 to Biconditional, 4 to Exclusive Or): \n"))
            if (fun) == 1:
                print ("\nFirst proposition ~(P): ",prop1,"\nLogical Connective Symbol: ^\nSecond proposition (Q): ", prop2,"\nCompound proposition: ~P^Q\nIn this case, the compound proposition will be TRUE only if both simple propositions are true, according to the truth table below.\n\n  Truth Table\n| P | Q | ~P^Q|\n|---|---|---- |\n| F | T | F  |\n|---|---|----|\n| F | F | F  |\n|---|---|----|\n| T | T | T  |\n|---|---|----|\n| T | F | F  |")
            elif (fun) == 2:
                print ("\nFirst proposition ~(P): ",prop1,"\nLogical Connective Symbol: v\nSecond proposition (Q): ", prop2,"\nCompound proposition: ~PvQ\nIn this case, the compound proposition will be FALSE only if both simple propositions are false, according to the truth table below.\n\n  Truth Table\n| P | Q | ~PvQ|\n|---|---|----|\n| F | T | T  |\n|---|---|----|\n| F | F | F  |\n|---|---|----|\n| T | T | T  |\n|---|---|----|\n| T | F | T  |")
            elif (fun) == 3:
                print ("\nFirst proposition ~(P): ",prop1,"\nLogical Connective Symbol: -> \nSecond proposition (Q): ", prop2,"\nCompound proposition: ~P->Q\nIn this case, the compound proposition will only be FALSE if the first proposition are true and the second are false, as the truth table below.\n\n  Truth Table\n| P | Q |~P->Q |\n|---|---|-----|\n| F | T | T   |\n|---|---|-----|\n| F | F | T   |\n|---|---|-----|\n| T | T | T   |\n|---|---|-----|\n| T | F | F   |")
            elif (fun) == 4:
                print ("\nFirst proposition ~(P): ",prop1,"\nLogical Connective Symbol: <->\nSecond proposition (Q): ", prop2,"\nCompound proposition: <->Q\nIn this case, the compound proposition will be TRUE only if both propositions have the same logical value, according to the truth table below.\n\n  Truth Table\n| P | Q |~P<->Q|\n|---|---|----|\n| F | T | F  |\n|---|---|----|\n| F | F | T  |\n|---|---|----|\n| T | T | T  |\n|---|---|----|\n| T | F | F  |")
            elif (fun) == 5:
                print ("\nFirst proposition ~(P): ",prop1,"\nLogical Connective Symbol: xor\nSecond proposition (Q): ", prop2,"\nCompound proposition: ~P xor Q\nIn this case, the compound proposition will only be FALSE if the propositions have the same logical value, according to the truth table below.\n\n  Truth Table\n| P | Q |~PxorQ|\n|---|---|----|\n| F | T | T  |\n|---|---|----|\n| F | F | F  |\n|---|---|----|\n| T | T | F  |\n|---|---|----|\n| T | F | T  |")            
                  
        elif choice == "2":
            fun = int(input("Insert the logical connective p(1 to conjunction, 2 to disjunction, 3 to Implication, 3 to Biconditional, 4 to Exclusive Or): \n"))
            if (fun) == 1:
                print ("\nFirst proposition (P): ",prop1,"\nLogical Connective Symbol: ^\nSecond proposition ~(Q): ", prop2,"\nCompound proposition: P^~Q\nIn this case, the compound proposition will be TR.UE only if both simple propositions are true, according to the truth table below.\n\n  Truth Table\n| P | ~Q | P ^ ~Q|\n|---|---|---- |\n| T | F |  F |\n|---|---|----|\n| T | T | T  |\n|---|---|----|\n| F | F | F  |\n|---|---|----|\n| F | T | F  |")
            elif (fun) == 2:
                print ("\nFirst proposition (P): ",prop1,"\nLogical Connective Symbol: v\nSecond proposition ~(Q): ", prop2,"\nCompound proposition: Pv~Q\nIn this case, the compound proposition will be FALSE only if both simple propositions are false, according to the truth table below.\n\n  Truth Table\n| P | ~Q | P v ~Q|\n|---|---|----|\n| T | F | T  |\n|---|---|----|\n| T | T | T  |\n|---|---|----|\n| F | F | F  |\n|---|---|----|\n| F | T | T  |")
            elif (fun) == 3:
                print ("\nFirst proposition (P): ",prop1,"\nLogical Connective Symbol: -> \nSecond proposition ~(Q): ", prop2,"\nCompound proposition: P -> ~Q\nIn this case, the compound proposition will only be FALSE if the first proposition are true and the second are false, as the truth table below.\n\n  Truth Table\n| P | Q |P -> ~Q |\n|---|---|-----|\n| T | F | F   |\n|---|---|-----|\n| T | T | T   |\n|---|---|-----|\n| F | F | T   |\n|---|---|-----|\n| F | T | T   |")
            elif (fun) == 4:
                print ("\nFirst proposition (P): ",prop1,"\nLogical Connective Symbol: <->\nSecond proposition ~(Q): ", prop2,"\nCompound proposition: P <-> ~Q\nIn this case, the compound proposition will be TRUE only if both propositions have the same logical value, according to the truth table below.\n\n  Truth Table\n| P | ~Q |P <-> ~Q|\n|---|---|----|\n| T | F | F  |\n|---|---|----|\n| T | T | T  |\n|---|---|----|\n| F | F | T  |\n|---|---|----|\n| F | T | F  |")
            elif (fun) == 5:
                print ("\nFirst proposition (P): ",prop1,"\nLogical Connective Symbol: xor\nSecond proposition ~(Q): ", prop2,"\nCompound proposition: P xor ~Q\nIn this case, the compound proposition will only be FALSE if the propositions have the same logical value, according to the truth table below.\n\n  Truth Table\n| P | Q |P xor ~Q|\n|---|---|----|\n| T | F | T  |\n|---|---|----|\n| T | T | F  |\n|---|---|----|\n| F | F | F  |\n|---|---|----|\n| F | T | T  |")                   
    else:
        print ("Invalid option!")
    print("*************************************************")
    # Insert the first proposition in the first line, the second proposition in the second line and insert the logical connective in the third line - 1 to conjunction, 2 to disjunction, 3 to Implication, 3 to Biconditional, 4 to Exclusive Or.
    P=0
    Q=0
    prop1 = str(input("Insert the first proposition: \n"))
    prop2 = str(input("Insert the second proposition: \n"))
    condition= (eval(input("Do you wwant to not p or not q (True\False)  : \n ")))
    if condition== False:
        fun1 = int(input("Insert the logical connective p(1 to conjunction, 2 to disjunction, 3 to Implication, 3 to Biconditional, 4 to Exclusive Or): \n"))
        if (fun1) == 1:
            print ("\nFirst proposition (P): ",prop1,"\nLogical Connective Symbol: ^\nSecond proposition (Q): ", prop2,"\nCompound proposition: P^Q\nIn this case, the compound proposition will be TRUE only if both simple propositions are true, according to the truth table below.\n\n  Truth Table\n| P | Q | P^Q|\n|---|---|----|\n| T | T | T  |\n|---|---|----|\n| T | F | F  |\n|---|---|----|\n| F | T | F  |\n|---|---|----|\n| F | F | F  |")
        elif (fun1) == 2:
            print ("\nFirst proposition (P): ",prop1,"\nLogical Connective Symbol: v\nSecond proposition (Q): ", prop2,"\nCompound proposition: PvQ\nIn this case, the compound proposition will be FALSE only if both simple propositions are false, according to the truth table below.\n\n  Truth Table\n| P | Q | PvQ|\n|---|---|----|\n| T | T | T  |\n|---|---|----|\n| T | F | T  |\n|---|---|----|\n| F | T | T  |\n|---|---|----|\n| F | F | F  |")
        elif (fun1) == 3:
            print ("\nFirst proposition (P): ",prop1,"\nLogical Connective Symbol: -> \nSecond proposition (Q): ", prop2,"\nCompound proposition: P->Q\nIn this case, the compound proposition will only be FALSE if the first proposition are true and the second are false, as the truth table below.\n\n  Truth Table\n| P | Q |P->Q |\n|---|---|-----|\n| T | T | T   |\n|---|---|-----|\n| T | F | F   |\n|---|---|-----|\n| F | T | T   |\n|---|---|-----|\n| F | F | T   |")
        elif (fun1) == 4:
            print ("\nFirst proposition (P): ",prop1,"\nLogical Connective Symbol: <->\nSecond proposition (Q): ", prop2,"\nCompound proposition: <->Q\nIn this case, the compound proposition will be TRUE only if both propositions have the same logical value, according to the truth table below.\n\n  Truth Table\n| P | Q |P<->Q|\n|---|---|----|\n| T | T | T  |\n|---|---|----|\n| T | F | F  |\n|---|---|----|\n| F | T | F  |\n|---|---|----|\n| F | F | T  |")
        elif (fun1) == 5:
            print ("\nFirst proposition (P): ",prop1,"\nLogical Connective Symbol: xor\nSecond proposition (Q): ", prop2,"\nCompound proposition: P xor Q\nIn this case, the compound proposition will only be FALSE if the propositions have the same logical value, according to the truth table below.\n\n  Truth Table\n| P | Q |PxorQ|\n|---|---|----|\n| T | T | F  |\n|---|---|----|\n| T | F | T  |\n|---|---|----|\n| F | T | T  |\n|---|---|----|\n| F | F | F  |")
    elif condition== True:
        choice= (eval(input(" please Enter your choice (1. ~P or 2. ~Q) in the form of '1' or '2' :")))
        if choice == "1":
            fun1 = int(input("Insert the logical connective p(1 to conjunction, 2 to disjunction, 3 to Implication, 3 to Biconditional, 4 to Exclusive Or): \n"))
            if (fun1) == 1:
                print ("\nFirst proposition ~(P): ",prop1,"\nLogical Connective Symbol: ^\nSecond proposition (Q): ", prop2,"\nCompound proposition: ~P^Q\nIn this case, the compound proposition will be TRUE only if both simple propositions are true, according to the truth table below.\n\n  Truth Table\n| P | Q | ~P^Q|\n|---|---|---- |\n| F | T | F  |\n|---|---|----|\n| F | F | F  |\n|---|---|----|\n| T | T | T  |\n|---|---|----|\n| T | F | F  |")
            elif (fun1) == 2:
                print ("\nFirst proposition ~(P): ",prop1,"\nLogical Connective Symbol: v\nSecond proposition (Q): ", prop2,"\nCompound proposition: ~PvQ\nIn this case, the compound proposition will be FALSE only if both simple propositions are false, according to the truth table below.\n\n  Truth Table\n| P | Q | ~PvQ|\n|---|---|----|\n| F | T | T  |\n|---|---|----|\n| F | F | F  |\n|---|---|----|\n| T | T | T  |\n|---|---|----|\n| T | F | T  |")
            elif (fun1) == 3:
                print ("\nFirst proposition ~(P): ",prop1,"\nLogical Connective Symbol: -> \nSecond proposition (Q): ", prop2,"\nCompound proposition: ~P->Q\nIn this case, the compound proposition will only be FALSE if the first proposition are true and the second are false, as the truth table below.\n\n  Truth Table\n| P | Q |~P->Q |\n|---|---|-----|\n| F | T | T   |\n|---|---|-----|\n| F | F | T   |\n|---|---|-----|\n| T | T | T   |\n|---|---|-----|\n| T | F | F   |")
            elif (fun1) == 4:
                print ("\nFirst proposition ~(P): ",prop1,"\nLogical Connective Symbol: <->\nSecond proposition (Q): ", prop2,"\nCompound proposition: <->Q\nIn this case, the compound proposition will be TRUE only if both propositions have the same logical value, according to the truth table below.\n\n  Truth Table\n| P | Q |~P<->Q|\n|---|---|----|\n| F | T | F  |\n|---|---|----|\n| F | F | T  |\n|---|---|----|\n| T | T | T  |\n|---|---|----|\n| T | F | F  |")
            elif (fun1) == 5:
                print ("\nFirst proposition ~(P): ",prop1,"\nLogical Connective Symbol: xor\nSecond proposition (Q): ", prop2,"\nCompound proposition: ~P xor Q\nIn this case, the compound proposition will only be FALSE if the propositions have the same logical value, according to the truth table below.\n\n  Truth Table\n| P | Q |~PxorQ|\n|---|---|----|\n| F | T | T  |\n|---|---|----|\n| F | F | F  |\n|---|---|----|\n| T | T | F  |\n|---|---|----|\n| T | F | T  |")            
                  
        elif choice == "2":
            fun1 = int(input("Insert the logical connective p(1 to conjunction, 2 to disjunction, 3 to Implication, 3 to Biconditional, 4 to Exclusive Or): \n"))
            if (fun1) == 1:
                print ("\nFirst proposition (P): ",prop1,"\nLogical Connective Symbol: ^\nSecond proposition ~(Q): ", prop2,"\nCompound proposition: P^~Q\nIn this case, the compound proposition will be TRUE only if both simple propositions are true, according to the truth table below.\n\n  Truth Table\n| P | ~Q | P ^ ~Q|\n|---|---|---- |\n| T | F |  F |\n|---|---|----|\n| T | T | T  |\n|---|---|----|\n| F | F | F  |\n|---|---|----|\n| F | T | F  |")
            elif (fun1) == 2:
                print ("\nFirst proposition (P): ",prop1,"\nLogical Connective Symbol: v\nSecond proposition ~(Q): ", prop2,"\nCompound proposition: Pv~Q\nIn this case, the compound proposition will be FALSE only if both simple propositions are false, according to the truth table below.\n\n  Truth Table\n| P | ~Q | P v ~Q|\n|---|---|----|\n| T | F | T  |\n|---|---|----|\n| T | T | T  |\n|---|---|----|\n| F | F | F  |\n|---|---|----|\n| F | T | T  |")
            elif (fun1) == 3:
                print ("\nFirst proposition (P): ",prop1,"\nLogical Connective Symbol: -> \nSecond proposition ~(Q): ", prop2,"\nCompound proposition: P -> ~Q\nIn this case, the compound proposition will only be FALSE if the first proposition are true and the second are false, as the truth table below.\n\n  Truth Table\n| P | Q |P -> ~Q |\n|---|---|-----|\n| T | F | F   |\n|---|---|-----|\n| T | T | T   |\n|---|---|-----|\n| F | F | T   |\n|---|---|-----|\n| F | T | T   |")
            elif (fun1) == 4:
                print ("\nFirst proposition (P): ",prop1,"\nLogical Connective Symbol: <->\nSecond proposition ~(Q): ", prop2,"\nCompound proposition: P <-> ~Q\nIn this case, the compound proposition will be TRUE only if both propositions have the same logical value, according to the truth table below.\n\n  Truth Table\n| P | ~Q |P <-> ~Q|\n|---|---|----|\n| T | F | F  |\n|---|---|----|\n| T | T | T  |\n|---|---|----|\n| F | F | T  |\n|---|---|----|\n| F | T | F  |")
            elif (fun1) == 5:
                print ("\nFirst proposition (P): ",prop1,"\nLogical Connective Symbol: xor\nSecond proposition ~(Q): ", prop2,"\nCompound proposition: P xor ~Q\nIn this case, the compound proposition will only be FALSE if the propositions have the same logical value, according to the truth table below.\n\n  Truth Table\n| P | Q |P xor ~Q|\n|---|---|----|\n| T | F | T  |\n|---|---|----|\n| T | T | F  |\n|---|---|----|\n| F | F | F  |\n|---|---|----|\n| F | T | T  |")                   
    else:
        print ("Invalid option!")
    if fun==fun1:
        print("The two statments are logically equivalent!")
    else:
        print("The two propositions are not logically equivalent!")
def questionTwo():
    import os
    class Specification():
        def __init__(self,specification):
            self.specification=specification
            self.variables=self.get_vars(specification)
            self.operand=self.get_operand(specification)
            self.cleared=False
            self.check_spec()
    
        def check_spec(self):
            #checks validity of the specification entered if typos or another
            if not self.variables:
                print("A specification has no variables")
    
        def get_operand(self,specification):
            #returns a string contaning the operand
            spec_oper=""
            operands=["<->","->","V","^"]
            for operand in operands:
                if operand in specification:
                    spec_oper=operand
                    break  
            return spec_oper
    
        def get_vars(self,specification):
            #returns variables in the specification in the list
            variables=[]
            for letter in specification:
                if letter.isalpha() and letter!="V" and letter not in variables:
                    variables.append(letter)
            if len(variables)>2:
                print("This program is made to deal with two variables only ")
            return variables
    
        def noted_vars(self):
            #returns a list of all variables that are precedded by ~
            vars=[]
            i=0
            for letter in self.specification:
                if letter=="~":
                    vars.append(self.specification[i+1])
                i+=1
            return vars
    
        def nots_count(self):
            #returns the count the number of nots in the specification
            count=0
            for letter in self.specification:
                if letter=="~":
                    count+=1
            return count
    
    def take_input():
        #returns The system in a list of strings
        system=[]
        inp_line=input("Enter your system and end the input by inputing quit:\n")
        while True:
            system.append(inp_line)  
            inp_line=input("")
            if inp_line=="quit":
                break
        return system
    
    def create_objs(system):
        #returns a list of Specification objects
        system_objs=[]
        for spec in system:
            system_objs.append(Specification(spec))
        return system_objs
    
    def intialize_vars(system):
        #returns a dict containing all the variabless initialized to 'n'
        var_val={}
        for specification in system:
            for var in specification.variables:
                var_val[var]="n"
        return var_val
    
    def reverse(bol):
        if bol==True:
            bol=False
        else:
            bol=True
        return bol
    
    def and_operator(spec,var_val):
        spec.cleared=True
        not_vars=spec.noted_vars()
        if len(spec.variables)==1: #p^p OR q^q
            var=spec.variables[0]
            if var_val[var]=="n" and var not in not_vars:
                var_val[var]=True
            elif var_val[var]=="n" and var in not_vars:
                var_val[var]=False
            elif var_val[var]!="n" and var not in not_vars:
                if var_val[var]!=True:
                    print("The system is not Consistent !")
                    exit(0)
            elif var_val[var]!="n" and var in not_vars: # ~p^~p
                if var_val[var]!=False:
                    print("The system is not Consistent !")
                    exit(0)
            return 
        else:
            var1,var2=spec.variables
    
        if var_val[var1]=="n" and var_val[var2]=="n":
            if var1 in not_vars and var2 in not_vars:   
                var_val[var1]=False                     
                var_val[var2]=False
            elif var1 in not_vars and var2 not in not_vars:
                var_val[var1]=False
                var_val[var2]=True
            elif var1 not in not_vars and var2  in not_vars:
                var_val[var1]=True
                var_val[var2]=False
            elif var1 not in not_vars and var2  not in not_vars:
                var_val[var1]=True
                var_val[var2]=True
        elif var_val[var1]=="n" and var_val[var2]!="n":
            if var1 in not_vars and var2 in not_vars:   
                var_val[var1]=False
                if var_val[var2]!=False:
                    print("The system is not Consistent !")
                    exit(0)
            elif var1 in not_vars and var2 not in not_vars:
                var_val[var1]=False
                if var_val[var2]!=True:
                    print("The system is not Consistent !")
                    exit(0)
            elif var1 not in not_vars and var2  in not_vars:
                var_val[var1]=True
                if var_val[var2]!=False:
                    print("The system is not Consistent !")
                    exit(0)
            elif var1 not in not_vars and var2  not in not_vars:
                var_val[var1]=False
                if var_val[var2]!=True:
                    print("The system is not Consistent !")
                    exit(0)
        elif var_val[var1]!="n" and var_val[var2]=="n":
            if var1 in not_vars and var2 in not_vars:   
                var_val[var2]=False
                if var_val[var1]!=False:
                    print("The system is not Consistent !")
                    exit(0)
            elif var1 in not_vars and var2 not in not_vars:
                var_val[var2]=True
                if var_val[var1]!=False:
                    print("The system is not Consistent !")
                    exit(0)
            elif var1 not in not_vars and var2  in not_vars:
                var_val[var2]=False            
                if var_val[var1]!=True:
                    print("The system is not Consistent !")
                    exit(0)
            elif var1 not in not_vars and var2  not in not_vars:
                var_val[var2]=True
                if var_val[var1]!=True:
                    print("The system is not Consistent !")
                    exit(0)
        elif var_val[var1]!="n" and var_val[var2]!="n":
            if var1 in not_vars and var2 in not_vars:  
                if var_val[var1]!=False:
                    print("The system is not Consistent !")
                    exit(0)
                if var_val[var2]!=False:
                    print("The system is not Consistent !")
                    exit(0)
            elif var1 in not_vars and var2 not in not_vars:
                if var_val[var1]!=False:
                    print("The system is not Consistent !")
                    exit(0)
                if var_val[var2]!=True:
                    print("The system is not Consistent !")
                    exit(0)
            elif var1 not in not_vars and var2  in not_vars:
                if var_val[var1]!=True:
                    print("The system is not Consistent !")
                    exit(0)
                if var_val[var2]!=False:
                    print("The system is not Consistent !")
                    exit(0)
            elif var1 not in not_vars and var2  not in not_vars:
                if var_val[var1]!=True:
                    print("The system is not Consistent !")
                    exit(0)
                if var_val[var2]!=True:
                    print("The system is not Consistent !")
                    exit(0)
    
    def or_operator(spec,var_val):
        if len(spec.variables)==1: #pVp or pV~p
            var=spec.variables[0]
            if var_val[var]=="n" and spec.nots_count()==0 :
                var_val[var]=True
                spec.cleared=True
            elif var_val[var]=="n" and spec.nots_count()==2 :
                var_val[var]=False
                spec.cleared=True
            elif var_val[var]!="n"and spec.nots_count()==0 :
                if var_val[var]!=True:
                    print("The system is not Consistent !")
                    exit(0)
            elif var_val[var]!="n"and spec.nots_count()==2:
                if var_val[var]!=False:
                    print("The system is not Consistent !")
                    exit(0)
        else:
            var1,var2=spec.variables
        
        if var1!="n" and var1 not in spec.noted_vars() and var_val[var1]==False:
            if var_val[var2]=="n":
                var_val[var2]=True
                spec.cleared=True
            elif var_val[var2]!=True:
                print("The system is not Consistent !")
                exit(0)
        elif var1!="n" and var1 in spec.noted_vars() and var_val[var1]==True:
            if var_val[var2]=="n":
                var_val[var2]=True
                spec.cleared=True
            elif var_val[var2]!=True:
                print("The system is not Consistent !")
                exit(0)
        elif var2!="n" and var2 not in spec.noted_vars() and var_val[var2]==False:
            if var_val[var1]=="n":
                var_val[var1]=True
                spec.cleared=True
            elif var_val[var1]!=True:
                print("The system is not Consistent !")
                exit(0)
        elif var2!="n" and var2 in spec.noted_vars() and var_val[var2]==True:
            if var_val[var1]=="n":
                var_val[var1]=True
                spec.cleared=True
            elif var_val[var1]!=True:
                print("The system is not Consistent !")
                exit(0)
        elif var_val[var1]==False and var_val[var2]==False:
            if var1 not in spec.noted_vars() and var2 not in spec.noted_vars():
                print("The system is not Consistent !")
                exit(0)
        elif var_val[var1]==False and var_val[var2]==True:
            if var1 not in spec.noted_vars() and var2  in spec.noted_vars():
                print("The system is not Consistent !")
                exit(0)
        elif var_val[var1]==True and var_val[var2]==False:
            if var1 in spec.noted_vars() and var2 not in spec.noted_vars():
                print("The system is not Consistent !")
                exit(0)
        elif var_val[var1]==True and var_val[var2]==True:
            if var1 in spec.noted_vars() and var2  in spec.noted_vars():
                print("The system is not Consistent !")
                exit(0)
            
    def no_operator(spec,var_val):
        spec.cleared=True
        var=spec.variables[0]
        if var_val[var]=="n":
            if not spec.noted_vars():
                var_val[var]=True
            else:
                var_val[var]=False
        elif var not in spec.noted_vars() and var_val[var]!=True:
            print("The system is not Consistent !")
            exit(0)
        elif var in spec.noted_vars() and var_val[var]!=False:
            print("The system is not Consistent !")
            exit(0)
    
    def implication_operator(spec,var_val):
        var1,var2=spec.variables
        noted_vars=spec.noted_vars()
        if var_val[var1]==True and var1 not in noted_vars:
            if var_val[var2]=="n":
                var_val[var2]=True
            elif var_val[var2]!=True:
                print("The system is not Consistent !")
                exit(0)
        elif var_val[var1]==False and var1 in noted_vars:
            if var_val[var2]=="n":
                var_val[var2]=True
            elif var_val[var2]!=True:
                print("The system is not Consistent !")
                exit(0)
        elif var_val[var2]==False and var2 not in noted_vars:
            if var_val[var1]=="n":
                var_val[var1]=False
            elif var_val[var1]!=False:
                print("The system is not Consistent !")
                exit(0)
        elif var_val[var2]==True and var2 in noted_vars:
            if var_val[var1]=="n":
                var_val[var1]=False
            elif var_val[var1]!=False:
                print("The system is not Consistent !")
                exit(0)
    
    def biconditional_operator(spec,var_val):
        if len(spec.variables)==1:
            return
        else:
            var1,var2=spec.variables
        noted_vars=spec.noted_vars()
        if var_val[var1]!="n" and var_val[var2]=="n":
            if var1 not in noted_vars and var2 not in noted_vars:
                var_val[var2]=var_val[var1]
            elif var1 not in noted_vars and var2 in noted_vars:
                var_val[var2]=reverse(var_val[var1])
            elif var1 in noted_vars and var2 not in noted_vars:
                var_val[var2]=reverse(var_val[var1])
            elif var1 in noted_vars and var2  in noted_vars:
                var_val[var2]=var_val[var1]
        elif var_val[var1]=="n" and var_val[var2]!="n":
            if var1 not in noted_vars and var2 not in noted_vars:
                var_val[var1]=var_val[var2]
            elif var1 not in noted_vars and var2 in noted_vars:
                var_val[var1]=reverse(var_val[var2])
            elif var1 in noted_vars and var2 not  in noted_vars:
                var_val[var1]=reverse(var_val[var2])
            elif var1 in noted_vars and var2 in noted_vars: 
                var_val[var1]=var_val[var2]
        elif var_val[var1]!="n" and var_val[var2]!="n":
            if var_val[var1]!=var_val[var2] and var1 not in noted_vars and var2 not in noted_vars:
                print("The system is not Consistent !")
                exit(0)
            if var_val[var1]!=reverse(var_val[var2]) and var1 not in noted_vars and var2 in noted_vars:
                print("The system is not Consistent !")
                exit(0)
            if var_val[var1]!=reverse(var_val[var2]) and var1 in noted_vars and var2 not in noted_vars:
                print("The system is not Consistent !")
                exit(0)
            if var_val[var1]!=var_val[var2] and var1 in noted_vars and var2 in noted_vars:
                print("The system is not Consistent !")
                exit(0)
        
    def printing(var_val):
    
        print("Your Results!")
        for key,val in var_val.items():
            print(f"the variable {key} has value {val}")
        print("--Thank you!--")
    
    system=take_input()
    system=create_objs(system)
    var_val=intialize_vars(system)
    for spec in system:
        if spec.operand=="^" :
            and_operator(spec,var_val)
        elif spec.operand=="":
            no_operator(spec,var_val)
    for i in range(0,len(var_val)):
        for spec in system:
            if spec.cleared==False:
                if spec.operand=="V" :
                    or_operator(spec,var_val)
                elif spec.operand=="<->" :
                    biconditional_operator(spec,var_val)
                elif spec.operand=="->" :
                    implication_operator(spec,var_val)
    printing(var_val)
    #Project()
def questionThree():
    count=0
    n=0
    k=(eval(input("Enter Your number of variables:")))
    if k < 3:
        print(k)
        x=(eval(input("Enter the Domain for Your First variable:")))
        y=(eval(input("Enter The Domain for Your Second variable:")))
        j=(eval(input("Enter the number of queries:")))
        print(" AxEx(x < y) ")
        if x<y:
            print("Yes, The statment is True")
        else:
            print("No, The statment is False:")
        print(" AxEx(x > y) ")
        if x>y:
            print("Yes, The statment is True")
        else:
            print("No, The statment is False")  
    else:
        print("please Your number of variables shouldn't exceed 2")
    while x < y:
        count=count+1
        print("Your counter is x=",count,"Your counter is y=",n)
        break
    while x > y:
        n=n+1
        print("Your counter is y=",n,"Your counter is x=",count )
        break
    while x==y:
        print("Your counter is x=y")
        break
def main():
    print ("Welcome To our Python Project!")
    print ("*****************************************************")
    print ("1. Create a Truth table.")
    print ("2. Create a Truth table for your propositions and determine whether they are logically equivalent or not!")
    print ("3. System Specifications")
    print ("4. queries of a combinations of universal and existential quantifiers")
    print ("5. Exit!")
    choice = input ("Please select your option >> ")
    if choice=="1":
        POneQuestionOne()
    elif choice=="2":
        PTwoQuestionOne()
    elif choice=="3":
        questionTwo()
    elif choice=="4":
        questionThree()
    elif choice =="5":
        print ("Program Terminated!")
        sys.exit()
    else:
        print ("That is an invalid option! ")
main()    
