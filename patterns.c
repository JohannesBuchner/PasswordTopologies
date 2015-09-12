#include<stdio.h>
#include<stdlib.h>
#include<assert.h>
#include<string.h>



int main(void) {
	char pw[1000];
	int i, n, j = 0;
	
	while(!feof(stdin)) {
		n = scanf("%s", pw);
		if (n == 0) {
			break;
		}
		j = j + 1;
		n = strlen(pw);
		for (i = 0; i < n; i++) {
			if (pw[i] >= 'a' && pw[i] <= 'z')
				pw[i] = 'l';
			else if (pw[i] >= 'A' && pw[i] <= 'Z')
				pw[i] = 'U';
			else if (pw[i] >= '0' && pw[i] <= '9')
				pw[i] = 'd';
			else
				pw[i] = 's';
		}
		printf("%s\n", pw);
	}
	fprintf(stderr, "%d converted\n", j);
	return 0;
}

