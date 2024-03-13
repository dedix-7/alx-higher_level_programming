#include "lists.h"
/**
 * check_cycle - checks if a linked lists has a cycle
 * @list: head of the lists
 * Return: 0 if it doesn't 1 if it does
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list->next == NULL)
		return (0);
	slow = list;
	fast = list;
	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;

		if (fast == slow)
			return (1);
	}
	return (0);
}
