lst = []
lst_len = len(lst)

subdiv_lst = lst_len//2

if lst_len % 2 == 0:
    lst_1 = lst[:subdiv_lst]
    lst_2 = lst[subdiv_lst:]
    lst_new = [lst_1, lst_2]
    print(lst_new)
elif lst_len % 2 != 0:
    lst_1 = lst[:subdiv_lst+1]
    lst_2 = lst[subdiv_lst+1:]
    lst_new = [lst_1, lst_2]
    print(lst_new)
elif lst_len == 0:
    lst_1 = lst
    lst_new = [lst_1, lst_1]
    print(lst_new)


