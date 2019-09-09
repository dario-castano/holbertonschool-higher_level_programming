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

	if (list == NULL)
		return (0);

	if (list->next == NULL)
		return (0);

	ptr_adv1 = list->next;
	ptr_adv2 = list->next->next;

	while (ptr_adv1 != ptr_adv2)
	{
		if (ptr_adv1->next == NULL || ptr_adv2->next->next == NULL)
			return (0);
		ptr_adv1 = ptr_adv1->next;
		ptr_adv2 = ptr_adv2->next->next;
	}

	return (1);
}
