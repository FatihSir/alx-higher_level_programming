#include "lists.h"
/**
* check_cycle - a function in C that checks if a singly
* linked list has a cycle in it.
*
* @list: linked list
*
* Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *fast_path = list;
	listint_t *slow_path = list;

	if (!list)
		return (0);
	while (fast_path && slow_path && fast_path->next)
	{
		slow_path = slow_path->next;
		fast_path = fast_path->next->next;
		if (slow_path == fast_path)
			return (1);
	}
	return (0);
}
