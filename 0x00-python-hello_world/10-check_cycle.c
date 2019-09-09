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
	listint_t *ptr_adv1;
	listint_t *ptr_adv2;

	ptr_adv1 = list;
	ptr_adv2 = list;

	while (ptr_adv1 != NULL && ptr_adv1->next != NULL)
	{
		ptr_adv1 = ptr_adv1->next;
		ptr_adv2 = ptr_adv2->next->next;

		if (ptr_adv1 == ptr_adv2)
			return (1);
	}

	return (0);
}
