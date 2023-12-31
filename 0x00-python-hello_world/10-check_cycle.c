#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * check_cycle - function that check singly linked list
 * @list: the pointer
 * Return: return 0
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	while (fast != NULL && slow != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
