n, k = map(int, input().split())
vacas = []
indices = {}
max_id = -1

for _ in range(n):
	vacas.append(int(input()))
	
for idc, vaca in enumerate(vacas):
	if vaca not in indices:
		indices[vaca] = []
	indices[vaca].append(idc)
	
for vaca, idc in indices.items():
	if len(idc) < 2: continue
	
	for i in range(len(idc)-1):
		if idc[i+1] - idc[i] <= k:
			max_id = max(max_id, vaca)
			
			
print(max_id)