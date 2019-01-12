def test_list_pre():
    prepare_list = locals()
    for i in range(16):
        prepare_list['list_' + str(i)] = []
        prepare_list['list_' + str(i)].append(('我是第' + str(i)) + '个list')
    print(prepare_list['list_0'])
    print(prepare_list['list_1'])
    print(prepare_list['list_2'])
    print(prepare_list['list_3'])

if __name__ == '__main__':
    test_list_pre()