import numpy
import sys
import matplotlib.pyplot as plt

filenames = sys.argv[1:]

common_patterns = set()
full_data = []

fout = open('report.rst', 'w')
fout.write("""Most common password topologies
================================================

.. figure:: patterns.png
	:scale: 66 %
	:alt: Most common password topologies

	The more common topologies found, the less secure the site is to topology
	attacks. Secure sites have users with diverse passwords.



Dataset from http://www.adeptus-mechanicus.com/codex/hashpass/hashpass.php


""")

for filename in filenames:
	print 'parsing', filename
	data = []
	for line in open(filename).readlines():
		try:
			a, b = line.strip().split()
		except Exception as e:
			print 'Parsing problem with "%s"' % line.strip()
		data.append((b, int(a)))
	data = data[::-1]
	ntot = sum([n for a, n in data])
	j = 10
	n = 0
	# go for the top 90%, include the first 10
	# stop when below 5%
	thisdata = []
	for i in range(0, len(data)):
		n += data[i][1]
		# down to low numbers and done half already and is only small fractions now
		if data[i][1] < 10000 and n > ntot * 0.3 and data[i][1] * 10 < ntot:
			#if not (n < ntot * 0.5 and data[i][1] * 40 < ntot and data[i][1] < 10000):
			break
		j = max(4, i)
		print data[i][1]
		common_patterns.add(data[i][0])
	if filename.endswith('.dic.pat.hist'):
		filename = filename[:-len('.dic.pat.hist')]
	fout.write('%s\n%s\n\n%d entries\n\n' % (filename, '-'*len(filename), ntot))
	print 'top', j, 'for', filename
	print data[:j]
	for pat, n in data[:j]:
		fout.write('* %s (%d)\n' % (pat, n))
	fout.write('\n\n')
		
	full_data.append((filename, dict(data)))

fout.close()

noveralltot = sum([sum([data.get(pat, 0) for pat in common_patterns]) for filename, data in full_data])
def total(pat):
	n = sum([data.get(pat, 0) for filename, data in full_data])
	print pat, n * 100. / noveralltot, n, noveralltot
	return n * 100. / noveralltot
common_patterns = sorted(common_patterns, key=total, reverse=True)
colors = 'k,r,b,g,m,c,orange,y,lime'.split(',')
color_alphas = []
for i in range(10):
	for color in colors:
		color_alphas.append((color, 1 - i / 10.))
xticks = []

sorted_data = []
for i, (filename, data_orig) in enumerate(full_data):
	n = 0
	data = dict(data_orig)
	ntot = sum([n for a, n in data.iteritems()])
	j = 0
	thisdata = []
	for pat, (color, alpha) in zip(common_patterns, color_alphas):
		k = data.pop(pat, 0)
		thisdata.append((k , j, pat, color, alpha))
		j += k
	nothers = sum([n for a, n in data.iteritems()])
	sorted_data.append((nothers * 100 / ntot, filename, thisdata, nothers, ntot))
	xticks.append(filename)

sorted_data = sorted(sorted_data)

plt.figure(figsize=(15,8))
for i, (pothers, filename, thisdata, nothers, ntot) in enumerate(sorted_data):
	for k , j, pat, color, alpha in thisdata:
		label = None
		if i == 0:
			label = ('%s (%d%%)' % (pat, total(pat)))
			print label, color, alpha
		plt.bar(left=i, height=k * 100. / ntot, bottom=j * 100. / ntot, color=color, label=label, alpha=alpha)
	#plt.bar(left=i, height=nothers * 100. / ntot, bottom=j * 100. / ntot, color='grey', alpha=0.2)

plt.title('Common Password Topologies')
plt.ylabel('Percent of passwords')
plt.xticks(numpy.arange(len(xticks)) + 0.5, xticks, rotation=90)
plt.legend(loc='upper center', prop=dict(size=10), ncol=6, bbox_to_anchor=(0.5, -0.2))

plt.savefig('patterns.pdf', bbox_inches='tight')
plt.savefig('patterns.png', bbox_inches='tight')
plt.close()


