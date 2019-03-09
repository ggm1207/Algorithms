def make_dict(): # ㅋㅋ 드릅다
    alpha = ['0','1','2','3','4','5','6','7','8','9']
    lists = []
    count = 0
    use_list = []
    for i1 in alpha:
        use_list.append(i1)
        for i2 in alpha:
            if i2 in use_list:
                continue
            use_list.append(i2)
            for i3 in alpha:
                if i3 in use_list:
                    continue
                use_list.append(i3)
                for i4 in alpha:
                    if i4 in use_list:
                        continue
                    use_list.append(i4)
                    for i5 in alpha:
                        if i5 in use_list:
                            continue
                        use_list.append(i5)
                        for i6 in alpha:
                            if i6 in use_list:
                                continue
                            use_list.append(i6)
                            for i7 in alpha:
                                if i7 in use_list:
                                    continue
                                use_list.append(i7)
                                for i8 in alpha:
                                    if i8 in use_list:
                                        continue
                                    use_list.append(i8)
                                    for i9 in alpha:
                                        if i9 in use_list:
                                            continue
                                        use_list.append(i9)
                                        for i0 in alpha:
                                            if i0 in use_list:
                                                continue
                                            use_list.append(i0)
                                            # print(use_list)
                                            # print(count)
                                            
                                            count += 1
                                            if (count == 1000000):
                                                print(use_list)
                                                break
                                            use_list.pop()
                                        use_list.pop()
                                    use_list.pop()
                                use_list.pop()
                            use_list.pop()
                        use_list.pop()
                    use_list.pop()
                use_list.pop()
            use_list.pop()
        use_list.pop()

if __name__ == "__main__":
    make_dict()