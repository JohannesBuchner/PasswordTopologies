#include<stdio.h>
#include<stdlib.h>

int main(void) {
	char word[500];
	int n, i, j;
	int score_best = 1000;
	int score;
	char chars[16] = "0123456789abcdef";
	int count;
	while(1) {
		n = scanf("%s", word);
		if (n != 1)
			break;
		score = 0;
		for(j = 0; j < 16; j++) {
			count = 0;
			for(i = 0; i < 32; i++) {
				if (word[i] == chars[j]) {
					count = 1;
					break;
				}
			}
			score += count;
		}
		
		// printf("%f %d\n", score, word);
		if (score < score_best) {
			fprintf(stderr, "%d %s\n", score, word);
			score_best = score;
		}
	}
	return 0;
}


