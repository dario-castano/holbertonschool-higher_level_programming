#include "lists.h"

/**
 * insert_node - insert node in a ordered linkedlist
 * @head: the head node
 * @number: number to insert
 * Return: Address of the new node, otherwise NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *left = NULL; 
	listint_t *right = NULL;

	if(head == NULL)
		return(NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	right = *head;
	
	if ((left == NULL) && (new_node->n <= right->n))
	{
		new_node->next = right;
		*head = new_node;
		return (new_node);
	}

	right = right->next;
	left = *head; 

	while (right != NULL)
	{
		if ((left->n <= new_node->n) && (new_node->n <= right->n))
		{
			new_node->next = right;
			left->next = new_node;
			return (new_node);
		}
		
		right = right->next;
		left = left->next;
	}
	
	left->next = new_node;
	return (new_node);
}