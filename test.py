import sys


def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    for i, v in enumerate(lines):
        l = list(v)
        l = sorted(l)
        flag = False
        ans = []
        z = 0
        for n in l:
            if(n == 0):
                z += 1
                continue
            else:
                ans.append(n)
                for o in range(z):
                    ans.append(0)
                else:
                    z = 0
        StrANS = "".join(ans)
        print(StrANS)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
