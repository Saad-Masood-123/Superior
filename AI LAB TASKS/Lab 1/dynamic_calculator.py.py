def dynamic_cal():
    while True:
        try:
            m = input("Enter math equation to calculate or type 'exit' to quit: ")
            if m.lower() == "exit":
                print("YOur Calculator is existed successfully")
                break
            ali = eval(m)
            print("Your mathematical equation answer is:", ali)
        except Exception as e:
            print("Please enter a valid expression to calculate .Error:",e)
#m= 1+2*3*(4-5//4)-(3//5) 
dynamic_cal()