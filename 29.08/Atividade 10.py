#A partir da lista Linguagens, verifique se a Linguagem 'Basic' está na lista e qual sua posição caso esteja. Trate o erro se ocorrer e mostre uma menssagem. 
linguagens=['Java', 'Python', 'C', 'C++', 'PHP']

try: 
    print (" 'Basic'está na lista", linguagens, "?")
    print ("Basic, está na posição: ", linguagens.index('Basic'))
except:  
        print ("Linguagem python não está na lista. ")
        


