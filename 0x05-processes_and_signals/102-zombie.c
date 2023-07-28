#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - creates an infinite loop with one second sleep
 *
 * Return: Always 0 (success)
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}


/**
 * main - creates 5 zombie processes
 *
 * Return: Always 0 (success)
 */

int main(void)
{
	pid_t zombie;
	int count;

	for (count = 0; count < 5; count++)
	{
		zombie = fork();
		if (zombie < 0)
		{
			exit(0);
		}
		printf("Zombie process created, PID: %d\n", zombie);
	}

	infinite_while();
	return (0);
}
