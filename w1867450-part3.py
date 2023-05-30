# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 20210356/w1867450
 
# Date: 2021/12/08

def yes_or_quit(question):
    reply = str(input(question+' (y/q): ')).lower().strip()
    if reply[0] == 'y':
        return 0
    elif reply[0] == 'q':
        return 1
    else:
        return yes_or_quit("Please Enter (y/q) ")

Progress_count = 0
Trailer_count = 0
Retriever_count = 0
Excluded_count = 0

credits_list=[]
progress_outcome_list=[]

while True:
        print()
        while True:
            Pass = input("Please enter your credits at pass:")
            try:
                Pass = int(Pass)
                if 0 <= Pass <= 120 and (Pass%20 == 0):
                    break    
                else:
                    print("Out of range")
                    print()
                    continue
            except ValueError:
                print("Integer required")
                print()
                continue
        while True:
            defer = input("Please enter your credit at defer:")
            try:
                defer = int(defer)
                if 0 <= defer <= 120 and (defer%20 == 0):
                    break
                else:
                    print("Out of range")
                    print()
                    continue
            except ValueError:
                print("Integer required")
                print()
                continue
        while True:
            fail = input("Please enter your credit at fail:")
            try:
                fail = int(fail)
                if 0 <= fail <= 120 and (fail%20 == 0):
                    break
                else:
                    print("Out of range")
                    print()
                    continue
            except ValueError:
                    print("Integer required")
                    print()
                    continue

        total = Pass + defer + fail

        if total > 120 or total == 0:
            print("Total incorrect.")
        
        elif (Pass == 120) and (defer == 0) and (fail == 0):
            print("Progress")
            credits_list = 'Progress -',Pass,",",defer,",",fail,'\n'
            progress_outcome_list.append(credits_list)
            Progress_count+=1
        
        elif (Pass == 100):
            print("Progress(module trailer)")
            credits_list = 'Progress(module trailer) - ',Pass,",",defer,",",fail,'\n'
            progress_outcome_list.append(credits_list)
            Trailer_count+=1
        
        elif (Pass == 80):
            print("Module retriever")
            credits_list = 'Module retriever - ',Pass,",",defer,",",fail,'\n'
            progress_outcome_list.append(credits_list)
            Retriever_count+=1
        
        elif (Pass == 60):
            print("Module retriever")
            credits_list = 'Module retriever - ',Pass,",",defer,",",fail,'\n'
            progress_outcome_list.append(credits_list)
            Retriever_count+=1
        
        elif (Pass == 40) and (fail >= 0 and fail <= 60):
            print("Module retriever")
            credits_list = 'Module retriever - ',Pass,",",defer,",",fail,'\n'
            progress_outcome_list.append(credits_list)
            Retriever_count+=1
        
        elif (Pass == 40) and (fail == 80):
            print("Exclude")
            credits_list = 'Exclude - ',Pass,",",defer,",",fail,'\n'
            progress_outcome_list.append(credits_list)
            Excluded_count+=1
        
        elif (Pass == 20) and (fail == 0 and fail <= 60):
            print("Module retriever")
            credits_list = 'Module retriever - ',Pass,",",defer,",",fail,'\n'
            progress_outcome_list.append(credits_list)
            Retriever_count+=1
        
        elif (Pass == 20) and (fail >= 80 and fail <= 100):
            print("Exclude")
            credits_list = 'Exclude - ',Pass,",",defer,",",fail,'\n'
            progress_outcome_list.append(credits_list)
            Excluded_count+=1
        
        elif (Pass == 0) and (fail >= 0 and fail <= 60):
            print("Module retriever")
            credits_list = 'Module retriever - ',Pass,",",defer,",",fail,'\n'
            progress_outcome_list.append(credits_list)
            Retriever_count+=1
        
        elif (Pass == 0) and (fail >= 80 and fail <= 120):
            print("Exclude")
            credits_list = 'Exclude - ',Pass,",",defer,",",fail,'\n'
            progress_outcome_list.append(credits_list)
            Excluded_count+=1

        print()
        print("Would you like to enter another set of data?")
        if(yes_or_quit("Enter 'y' for yes or 'q' to quit and view results:")):
            break
        
print()
print("---------------------------------------------------------------")
#Horizontal Histogram
print("Horizontal Histogram")
print("Progress",+Progress_count," :",end='')
for i in range(Progress_count):
    print(end = '*')
print()
print("Trailer",+Trailer_count,"  :",end='')
for i in range(Trailer_count):
    print(end = '*')
print()
print("Retriever",+Retriever_count,":",end='')
for i in range(Retriever_count):
    print(end = '*')
print()
print("Excluded",+Excluded_count," :",end='')
for i in range(Excluded_count):
    print(end = '*')

Progression_total = Progress_count + Trailer_count + Retriever_count + Excluded_count
print()
print()
print(Progression_total,"outcomes in total")
print("---------------------------------------------------------------")

print()
print()
#Vertical Histogram
#https://stackoverflow.com/questions/53285446/how-do-i-make-print-vertically-on-python-loops#:~:text=You%20can%20use,Improve%20this%20answer
header = ['Progress',str(Progress_count),'|', 'Trailer',str(Trailer_count),'|', 'Retriever',str(Retriever_count),'|', 'Excluded',str(Excluded_count),'|']
print(' '.join(header))
for x in range(max(Progress_count, Trailer_count, Retriever_count, Excluded_count)):
    print("    {0}           {1}              {2}            {3}".format(
        '*' if x < Progress_count else ' ',
        '*' if x < Trailer_count else ' ',
        '*' if x < Retriever_count else ' ',
        '*' if x < Excluded_count else ' '
    ))
print()
print()
print(Progression_total,"outcomes in total")
print("---------------------------------------------------------------")


print()
print()
#List
for credits_list in progress_outcome_list:
    for i in credits_list:
        print(i,end = '')
