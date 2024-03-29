# # A naive Python implementation of LIS problem

ARRAY =[3, -2, 1, 4, 7, 1]

# def lis(self, arr):
# 	n = len(arr)
# 	lis = [1]*n

#         # Compute optimized LIS values in bottom up manner
# 	for i in range(1,n):
#         for j in range(0,i):
#             if arr[i]>arr[j] and lis[i]<lis[j]+1:
#                 lis[i]=lis[j]+1

#         # Return maximum of all LIS values
#     return max(lis)
	
# lis(ARRAY)

def _list_increasing_subsequences(arr):
	n = len(arr)
	lis = [1]*n
	print(lis)
	for i in range(1,n):
		for j in range(0,i):
			print(f'i= {i}')
			print(f'j={j}')
			if arr[i]>arr[j] and lis[i]<lis[j]+1:
				lis[i]=lis[j]+1
			print(lis)

	return print(max(lis))

_list_increasing_subsequences(ARRAY)
