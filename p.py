#asyykkk.jgn recode tolol
#emang gini programnya
num = int(input("TULIS BILANGANYA==>>: "))
#Namnya prima harus lebih dari 1
#belajar dulu sono!!
#tanya anak sd!!
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num, "Ya bener nih itu adalah bilangan prima")
            print(i, "kali", num//i, "=", num)
            break
    else:
        print(num,"Ya bener nih..itu adalah  prima")
# bila bilangan kurang atau sama dengan satu
else:
    print(num, "Ya ampun...Itu bukan bilangan prima")