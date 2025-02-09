import pandas as pd
import matplotlib.pyplot as plt
import sys
print('----------------------------------------------------------------------INDIA_GDP_DATA_PROJECT--------------------------------------------------------------------------')
while True:
  print('\n--------------------Menu--------------------\n1-Quiz\n2-Exploring The Data Using Pandas\n3-To see GDP of India, Per capita usd and percentage of growth of India of particular year\n4-Graphical Representation of India GDP growth\n5-Graphical representation of grwoth rate\n6-Graphical representation of Per capita income\n7-Comparing India of 1961 to India of 2021\n8-Exit\n--------------------------------------------' )
  ch=int(input('Enter Your Choice:'))
  if ch==1:
    #This quiz game ask multiple choice question about India.
    print("Welcome to the Quiz Game!")
    chances = 1
    print("You will have", chances, "chance to answer correctly. \nPlease put the alphabet of the answer\n")
    score = 0
    #QUESTION NUMBER 1
    Question_1 = print("1.In which year did India became an independent country?\n(A) 1947\n(B) 1950\n(C) 1940\n(D) 1946\n\n ")
    answer_1 = "A"

    for i in range(chances):
        answer = input("Answer: ")
        if (answer.upper() == answer_1):
            print("Correct!\n")
            score = score + 1
            break
        else:
            print("Incorrect!\n")
            print("The correct answer is", answer_1, "\n\n")

    #QUESTION NUMBER 2
    Question_2 = print("2.What was the GDP of India when it became independent?\n(A) 2.7 lakh crore\n(B) 100 lakh crore\n(C) 10 crore\n(D) 4.33 lakh crore\n\n ")
    answer_2 = "A"

    for i in range(chances):
        answer = input("Answer: ")
        if (answer.upper() == answer_2):
            print("Correct!\n")
            score = score + 1
            break
        else:
            print("Incorrect!\n")
            print("The correct answer is", answer_2, "\n\n")

    #QUESTION NUMBER 3
    Question_3 = print("3.Who colonised India from 1858 to 1947?\n(A) Americans\n(B) Dutch\n(C) Britishers\n(D) Chinease\n\n ")
    answer_3 = "C"

    for i in range(chances):
        answer = input("Answer: ")
        if (answer.upper() == answer_3):
            print("Correct!\n")
            score = score + 1
            break
        else:
            print("Incorrect!\n")
            print("The correct answer is", answer_3, "\n\n")

    #QUESTION NUMBER 4
    Question_4 = print("4.How much percent of GDP did India constituted to world GDP in 1947?\n(A) 12%\n(B) 6%\n(C) 10%\n(D) 2%\n\n ")
    answer_4 = "D"

    for i in range(chances):
        answer = input("Answer: ")
        if (answer.upper() == answer_4):
            print("Correct!\n")
            score = score + 1
            break
        else:
            print("Incorrect!\n")
            print("The correct answer is", answer_4, "\n\n")

    #QUESTION NUMBER 5
    Question_5 = print("5.Who was the first prime minister of independent India?\n(A) pandit nehru\n(B) wallabh bhai patel\n(C) rahul gandhi\n(D) sonia gandhi\n\n ")
    answer_5 = "A"

    for i in range(chances):
        answer = input("Answer: ")
        if (answer.upper() == answer_5):
            print("Correct!\n")
            score = score + 1
            break
        else:
            print("Incorrect!\n")
            print("The correct answer is", answer_5, "\n\n")

    #QUESTION NUMBER 6
    Question_6 = print("6.What was the India's contribution to total world GDP before its colonization?\n(A) 21.2%\n(B) 17.7%\n(C) 12%\n(D) 24.4%\n\n ")
    answer_6 = "D"

    for i in range(chances):
        answer = input("Answer: ")
        if (answer.upper() == answer_6):
            print("Correct!\n")
            score = score + 1
            break
        else:
            print("Incorrect!\n")
            print("The correct answer is", answer_6, "\n\n")

    #QUESTION NUMBER 7
    Question_7 = print("7.Was India the most populous country in the world in 1950?\n(A) True\n(B) False\n\n ")
    answer_7 = "B"

    for i in range(chances):
        answer = input("Answer: ")
        if (answer.upper() == answer_7):
            print("Correct!\n")
            score = score + 1
            break
        else:
            print("Incorrect!\n")
            print("The correct answer is", answer_7, "\n\n")
        
    if score>= 4:
      print("Well done! Your score was", score)

    if score<=3:
      print("Thank you for playing. Your score was")

    print("Thank you for playing Quiz Game!")
  if ch==2: 
    print('\nExploring The Data Using Pandas')
    df3=pd.read_csv('India_GDP_Data.csv')
    print('\n-----------------Description of dataframe-----------------','\n',df3.describe(),'\n')
    print('-----------------Top five rows of the dataframe-----------------','\n',df3.head(),'\n')
    print('-----------------Last five rows of the dataframe-----------------','\n',df3.tail(),'\n')
    print('-----------------shape of the dataframe-----------------','\n',df3.shape,'\n')
    print('-----------------Size of the dataframe-----------------','\n',df3.size,'\n')
    print('-----------------Dimension of the dataframe-----------------','\n',df3.ndim,'\n')
    print('-----------------Columns of the dataframe-----------------','\n',df3.columns,'\n')
  if ch==3:
    df=pd.read_csv('India_GDP_Data.csv',index_col=['Year'])
    To=int(input('Enter a Year:' ))
    if To<1961:
     print('Enter a Valid number','\n','Valid range is 1961-2021')
    elif To>2021:
       print('Enter a Valid number','\n','Valid range is 1961-2021')
    elif To>=1961:
         print(df.loc[To])

  if ch==4:
    df2=pd.read_csv('India_GDP_Data.csv')
    x=(df2['Year'])
    y=(df2['GDP_In_Billion_USD'])  
    plt.figure(figsize=(25,10))
    plt.subplot(2,2,1)
    plt.plot(x,y,marker='.',mec='r',mfc='k',c='k')

    x=(df2['Year'])
    y=(df2['GDP_In_Billion_USD'])
    plt.figure(figsize=(25,10))
    plt.subplot(2,2,2)
    plt.bar(x,y,color='c''g')
    plt.show()
  if ch==5:
    df2=pd.read_csv('India_GDP_Data.csv')
    x=(df2['Year'])
    y=(df2['Percentage_Growth '])
    plt.figure(figsize=(25,10))
    plt.subplot(2,2,1)
    plt.plot(x,y,marker='.',mec='r',mfc='k',color='k')

    x=(df2['Year'])
    y=(df2['Percentage_Growth '])
    plt.figure(figsize=(25,10))
    plt.subplot(2,2,2)
    plt.bar(x,y,color='g''y''c')
    plt.show()
  if ch==6:
    df2=pd.read_csv('India_GDP_Data.csv')
    x=(df2['Year'])
    y=(df2['Per_Capita_in_USD'])
    plt.figure(figsize=(25,10))
    plt.subplot(2,2,1)
    plt.plot(x,y,marker='.',mec='r',mfc='k',color='k')

    x=(df2['Year'])
    y=(df2['Per_Capita_in_USD'])
    plt.figure(figsize=(25,10))
    plt.subplot(2,2,2)
    plt.bar(x,y,color='g''c')
    plt.show()
  if ch==7:
    #comparing india of 1961 to india of 2021
    y=[39.23,3173.40]
    x=['1961','2021']
    plt.subplot(3,3,1)
    plt.bar(x,y)
    plt.title('GDP OF INDIA OF 1961 AND 2021',color='r')
    plt.xlabel('YEAR',size=12)
    plt.ylabel('GDP_In_Billion_USD',size=8)

    y1=[85,2277]
    x1=['1961','2021']
    plt.subplot(3,3,3)
    plt.bar(x1,y1)
    plt.title('Per Capita(USD) of 1961 and 2021',color='r')
    plt.xlabel('YEAR',size=12)
    plt.ylabel('Per_Capita_in_USD',size=8)

    y2=[3.72,8.95]
    x2=['1961','2021']
    plt.subplot(3,3,7)
    plt.bar(x2,y2)
    plt.title('Gowth rate of 1961 and 2021',color='r')
    plt.xlabel('YEAR',size=12)
    plt.ylabel('percent_growth',size=8)
    plt.show()
  if ch==8:
    print('Thank You')
    sys.exit()
