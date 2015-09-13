#include<stdio.h>
#include<stdlib.h>

int main(void) {
	char word[500];
	int n, i;
	int score_best = -1;
	int score, midscore;
	while(1) {
		n = scanf("%s", word);
		if (n != 1)
			break;
		score = 0;
		midscore = 0;
		for(i = 0; i < 31; i++) {
			int diff = word[i+1] - word[i];
			if (diff == 0) {
				midscore++;
			} else {
				if (midscore > score)
					score = midscore;
				midscore = 0;
			}
		}
		if (midscore > score)
			score = midscore;
		//printf("%d %s\n", score, word);
		if (score > score_best) {
			fprintf(stderr, "%d %s\n", score, word);
			score_best = score;
		}
	}
	return 0;
}


