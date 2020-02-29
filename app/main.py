from test_script import Myclass

if __name__ == '__main__':
    list1 = [1,2,3]
    list2 = [1,2,3,4]
    m = Myclass(10,5, list1, list2)
    sum = m.add_numbers()
    lst = m.list_length()