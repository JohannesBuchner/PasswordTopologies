
patterns: patterns.c
	gcc -O3 -std=c99 -Wall -Wextra -pedantic patterns.c -o patterns

%.dic.pat: %.dic patterns
	./patterns < $^ > $@

%.dic.pat.hist: %.dic.pat
	sort $^ |uniq -c|sort -n > $@

#%.dic: %.dic.7z
#	unfoo $^

