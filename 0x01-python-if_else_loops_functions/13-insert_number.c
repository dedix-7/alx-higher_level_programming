#include "lists.h"
/**
 * insert_node - insert a node to a sorted linked lists
 * @head: address of the head
 * @number: number data part of lits
 * Return: address of node or null on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new, *prev;

	new = malloc(sizeof(listint_t) * 1);
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (head == NULL)
		return (NULL);
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	temp = *head;
	if (new->n < temp->n)/* insert at the eginning */
	{
		new->next = temp;
		*head = new;
		return (new);
	}
	while (temp->next)
	{
		prev = temp;
		if (new->n < temp->next->n)
		{
			new->next = temp->next;
			prev->next = new;
			return (new);
		}
		temp = temp->next;
	}
	if (temp->n <= new->n)
		temp->next = new;
	return (new);
}
