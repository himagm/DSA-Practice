def pascal(numRows):
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1],[1,1]]
    else:
        tri = [[1],[1,1]]
        rows = numRows - 2 #len(tri) - remaining rows to add
        col = 3
        j = 1
        while j <= rows:
            # print(rows)
            row = [1] * (col)
            if len(row) %2 == 0:
                mid = len(row) // 2 - 1
            else:
                mid = len(row) // 2
            i = 1
            while i <= mid:
                # print(i)
                row[i] = tri[col-2][i] + tri[col-2][i-1]
                i += 1

            row[-(mid+1):] = row[mid::-1]

            tri.append(row)
            col += 1
            j += 1

        print(tri)

pascal(6)
# print(pascal(2))
# print(pascal(1))