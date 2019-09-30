#include "lists.h"
/**
  * print_dlistint - function that prints elements of list
  * @h: pointer to head node
  * Return: number of nodes
  */
size_t print_dlistint(const dlistint_t *h)
{
	size_t counter;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		h = h->next;
		counter++;
	}
	return (counter);
}
