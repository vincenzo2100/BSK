#http://www.wechall.net/challenge/training/encodings/url/index.php
code = "%59%69%70%70%65%68%21%20%59%6F%75%72%20%55%52%4C%20%69%73%20%63%68%61%6C%6C%65%6E%67%65%2F%74%72%61%69%6E%69%6E%67%2F%65%6E%63%6F%64%69%6E%67%73%2F%75%72%6C%2F%73%61%77%5F%6C%6F%74%69%6F%6E%2E%70%68%70%3F%70%3D%72%6D%66%65%67%67%6F%68%72%73%70%67%26%63%69%64%3D%35%32%23%70%61%73%73%77%6F%72%64%3D%66%69%62%72%65%5F%6F%70%74%69%63%73%20%56%65%72%79%20%77%65%6C%6C%20%64%6F%6E%65%21 "
list = [code[i:i+2] for i in range(1,len(code),3)]
list2 = [bytes.fromhex(i).decode('utf-8') for i in list ]
answer =""
for i in list2:
    answer+=i
print(answer)