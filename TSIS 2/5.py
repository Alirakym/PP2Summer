n = str(input())
su=0
mu=1

for i in range(0,len(n)):
    su=su+int(n[i])
    mu=mu*int(n[i])

sub=mu-su
print(sub)

