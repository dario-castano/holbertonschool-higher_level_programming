#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: the head
 * Return: head of reversed list
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *base;
	listint_t *ptr;

	base = *head;

	if (base == NULL)
		return (NULL);

	while (base->next != NULL)
	{
		ptr = base->next;
		base->next = ptr->next;
		ptr->next = *head;
		*head = ptr;
	}

	return (*head);
}

/**
 * get_middle_node - get the middle of a linkedlist
 * @head: head of the linkedlist
 * Return: Middle node
 */
listint_t *get_middle_node(listint_t **head)
{
	listint_t *slow, *fast;

	if (head == NULL)
		return (NULL);

	slow = *head;
	fast = *head;

	if (slow->next == NULL)
		return (slow);

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	return (slow);
}

/**
 * is_palindrome - checks if a singly linked
 * list is a palindrome
 *
 * @head: head of the list
 *
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *first_half, *second_half;
	listint_t **middle;

	if (*head == NULL)
		return (1);

	first_half = *head;

	if (first_half->next == NULL)
		return (1);

	middle = malloc(sizeof(listint_t *));
	if (middle == NULL)
		return (-1);

	*middle = get_middle_node(head);
	second_half = reverse_listint(middle);

	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
		{
			free(middle);
			return (0);
		}
		first_half = first_half->next;
		second_half = second_half->next;
	}
	free(middle);
	return (1);
}
