#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - checks if a cycle exists
 * @list: pointer to a list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr;

	if (list == NULL)
		return (0);

	if (list->next == NULL)
		return (0);

	ptr = list->next;

	while (ptr != list)
	{
		if (ptr->next == NULL)
			return (0);
		ptr = ptr->next;
	}

	return (1);
}
