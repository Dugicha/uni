'''
    ნიკა ოთიაშვილი, დავალება 1.1.
    პოულობს c-ს ჯერადების რაოდენობას a-სა და b-ს შორის.
'''

def find_multiples(a, b, c):
    # დავადგინოთ a-სა და b-ს შორის რომელია დიდი და პატარა
    more = a
    less = b
    if more < b:
        more = b
        less = a
    '''
    გაიგებს more-მდე c-ს ჯერადების რაოდენობას, შემდომ (less - 1)-მდე c-ს 
    ჯერადების რაოდენობას და შემდგომ მათ სხვაობას. less-1 საჭიროა, 
    ვინაიდან გვინდა გამოვტოვოთ less როცა იგი თვითონ c-ს ჯერადია
    '''
    mod = -1
    if less < 0 and more > 0 :
        mod = 1
    count = ((more) // c) - ((less + mod) // c)
    return count

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

print("count: {}".format(find_multiples(a, b, c)))