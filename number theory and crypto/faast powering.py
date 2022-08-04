# binary expansion
def to_binary(n):
    return bin(n)[2:]

#write binary as power of 2
def to_binary_power(n):
    bin=to_binary(n)
    bin_list=list(bin)
    bin_list.reverse()
    index_list=[]
    for i in range(len(bin_list)):
        if bin_list[i]=='1':
            index_list.append(i)
    return index_list
#tesst to_binadry

n=2
p=9999999999
mod=455
bin=to_binary_power(p)
#calculate bin%mod
def mod_table(n,bin,mod):
    mod_dict={}
    #find max bin
    max_bin=max(bin)        
    for i in range(max_bin+1):
        mod_dict[i]=(n**2**i)%mod
    return mod_dict
# time it
import time
start=time.time()
mod_table=mod_table(n,bin,mod)
val=1
for b in bin:
    val=val*mod_table[b]
    val=val%mod
print(val)
end=time.time()
print(end-start)