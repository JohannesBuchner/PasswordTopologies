
patterns: patterns.c
	gcc -O3 -std=c99 -Wall -Wextra -pedantic patterns.c -o patterns

%.dic.pat: %.dic patterns
	./patterns < $^ > $@

%.dic.pat.hist: %.dic.pat
	sort $^ |uniq -c|sort -n > $@

%.dic.sort: %.dic
	sort $^ > $@

%.dic.sort.count: %.dic.sort
	uniq -c $^|sort -n > $@
10k-most-common.dic.sort.count: 10k-most-common.dic
	awk '{print 100,$$2;}' < $^ > $@

%.dic.sort.count.5: %.dic.sort.count
	 awk '{if ($$1 >= 5){print $$2;}}' < $^ > $@

%.dic.sort.count.2: %.dic.sort.count
	 awk '{if ($$1 < 5 && $$1 >= 2){print $$2;}}' < $^ > $@

%.dic.sort.count.1: %.dic.sort.count
	 awk '{if ($$1 == 1){print $$2;}}' < $^ > $@


wordlist.5:
	ls *.dic|sed 's,$$,.sort.count.5,g'|xargs make -j3
	cat *.dic.sort.count.5 | python makewordlist.py > $@
wordlist.2:
	ls *.dic|sed 's,$$,.sort.count.2,g'|xargs make -j3
	cat *.dic.sort.count.2 | python makewordlist.py > $@
wordlist.1:
	ls *.dic|sed 's,$$,.sort.count.1,g'|xargs make -j3
	cat *.dic.sort.count.1 | python makewordlist.py > $@
wordlist: wordlist.1 wordlist.2 wordlist.5
	cat $^ | python makewordlist.py > $@
	
#%.dic: %.dic.7z
#	unfoo $^

.PRECIOUS: %.dic.pat

