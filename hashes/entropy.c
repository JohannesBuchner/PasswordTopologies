#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(void) {
	char word[500];
	int n, i, j;
	double score_best = 1e300;
	double score;
	char chars[16] = "0123456789abcdef";
	int count;
	double prob;
	const double length = 32; // md5
	const double log2 = log(2);
	while(1) {
		n = scanf("%s", word);
		if (n != 1)
			break;
		score = 0;
		for(j = 0; j < 16; j++) {
			count = 0;
			for(i = 0; i < 32; i++) {
				if (word[i] == chars[j])
					count++;
			}
			if (count > 0) {
				prob = count / length; 
				score -= prob * log(prob) / log2;
			}
		}
		
		// printf("%f %s\n", score, word);
		if (score < score_best) {
			fprintf(stderr, "%.3f %s\n", score, word);
			score_best = score;
		}
	}
	return 0;
}


